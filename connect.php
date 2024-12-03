<?php
// Database connection.
$host = "localhost"; // Replace with your database host.
$db_name = "travel_taxi_db"; // Replace with your database name.
$username = "root"; // Replace with your database username.
$password = ""; // Replace with your database password.

try {
    $pdo = new PDO("mysql:host=$host;dbname=$db_name", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Set a 500 (internal server error) response code.
    http_response_code(500);
    echo "Database error: " . $e->getMessage();
}
?>