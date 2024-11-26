<?php
// Only process POST requests.
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the form fields and remove whitespace.
    $fullname = strip_tags(trim($_POST["full-name"]));
    $fullname = str_replace(array("\r", "\n"), array(" ", " "), $fullname);
    $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
    $packageType = trim($_POST["package-type"]);
    $passengers = trim($_POST["passengers"]);
    $startDest = trim($_POST["start-dest"]);
    $endDest = trim($_POST["end-dest"]);
    $rideDate = trim($_POST["ride-date"]);
    $rideTime = trim($_POST["ride-time"]);

    // Check that data was sent to the script.
    if (empty($fullname) || empty($packageType) || empty($passengers) || empty($startDest) || empty($endDest) || empty($rideDate) || empty($rideTime) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        // Set a 400 (bad request) response code and exit.
        http_response_code(400);
        echo "Oops! There was a problem with your submission. Please complete the form and try again.";
        exit;
    }

    // Database connection.
    $host = "localhost"; // Replace with your database host.
    $db_name = "your_database"; // Replace with your database name.
    $username = "your_username"; // Replace with your database username.
    $password = "your_password"; // Replace with your database password.

    try {
        $pdo = new PDO("mysql:host=$host;dbname=$db_name", $username, $password);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        // Prepare the SQL query to insert the form data.
        $sql = "INSERT INTO bookings (fullname, email, package_type, passengers, start_dest, end_dest, ride_date, ride_time) 
                VALUES (:fullname, :email, :packageType, :passengers, :startDest, :endDest, :rideDate, :rideTime)";
        $stmt = $pdo->prepare($sql);

        // Bind parameters.
        $stmt->bindParam(':fullname', $fullname);
        $stmt->bindParam(':email', $email);
        $stmt->bindParam(':packageType', $packageType);
        $stmt->bindParam(':passengers', $passengers);
        $stmt->bindParam(':startDest', $startDest);
        $stmt->bindParam(':endDest', $endDest);
        $stmt->bindParam(':rideDate', $rideDate);
        $stmt->bindParam(':rideTime', $rideTime);

        // Execute the query.
        if ($stmt->execute()) {
            // Set a 200 (OK) response code.
            http_response_code(200);
            echo "Thank You! Your ride has been booked.";
        } else {
            // Set a 500 (internal server error) response code.
            http_response_code(500);
            echo "Oops! Something went wrong and we couldn't book your ride.";
        }
    } catch (PDOException $e) {
        // Set a 500 (internal server error) response code.
        http_response_code(500);
        echo "Database error: " . $e->getMessage();
    }
} else {
    // Not a POST request, set a 403 (forbidden) response code.
    http_response_code(403);
    echo "There was a problem with your submission, please try again.";
}
