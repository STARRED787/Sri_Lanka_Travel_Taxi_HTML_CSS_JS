<?php
// Include the database connection
require('connect.php');

// Only process POST requests
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the form fields and sanitize inputs
    $fullname = strip_tags(trim($_POST["full-name"]));
    $fullname = str_replace(["\r", "\n"], [" ", " "], $fullname);
    $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
    $packageType = htmlspecialchars(trim($_POST["package-type"]));
    $passengers = htmlspecialchars(trim($_POST["passengers"]));
    $startDest = htmlspecialchars(trim($_POST["start-dest"]));
    $endDest = htmlspecialchars(trim($_POST["end-dest"]));
    $rideDate = htmlspecialchars(trim($_POST["ride-date"]));
    $rideTime = htmlspecialchars(trim($_POST["ride-time"]));

    // Validate required fields
    if (
        empty($fullname) || empty($packageType) || empty($passengers) ||
        empty($startDest) || empty($endDest) || empty($rideDate) ||
        empty($rideTime) || !filter_var($email, FILTER_VALIDATE_EMAIL)
    ) {
        http_response_code(400);
        echo "Oops! There was a problem with your submission. Please complete the form and try again.";
        exit;
    }

    try {
        // Prepare the SQL query to insert the form data
        $sql = "INSERT INTO bookings (fullname, email, package_type, passengers, start_dest, end_dest, ride_date, ride_time) 
                VALUES (:fullname, :email, :packageType, :passengers, :startDest, :endDest, :rideDate, :rideTime)";
        $stmt = $pdo->prepare($sql);

        // Bind parameters
        $stmt->bindParam(':fullname', $fullname);
        $stmt->bindParam(':email', $email);
        $stmt->bindParam(':packageType', $packageType);
        $stmt->bindParam(':passengers', $passengers);
        $stmt->bindParam(':startDest', $startDest);
        $stmt->bindParam(':endDest', $endDest);
        $stmt->bindParam(':rideDate', $rideDate);
        $stmt->bindParam(':rideTime', $rideTime);

        // Execute the query
        if ($stmt->execute()) {
            http_response_code(200);
            echo "Thank You! Your ride has been booked.";
        } else {
            http_response_code(500);
            echo "Oops! Something went wrong and we couldn't book your ride.";
        }
    } catch (PDOException $e) {
        // Handle database errors
        http_response_code(500);
        echo "Database error: " . $e->getMessage();
    }
} else {
    // Not a POST request, set a 403 (forbidden) response code
    http_response_code(403);
    echo "There was a problem with your submission, please try again.";
}
