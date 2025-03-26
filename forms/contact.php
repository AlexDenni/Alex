<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

// Load PHPMailer classes
require 'src/PHPMailer.php';
require 'src/SMTP.php';
require 'src/Exception.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get form data
    $name = $_POST['name'];
    $email = $_POST['email'];
    $message = $_POST['message'];

    // Create a new PHPMailer instance
    $mail = new PHPMailer(true);

    try {
        // SMTP settings for Gmail
        $mail->isSMTP();
        $mail->Host = 'smtp.gmail.com';
        $mail->SMTPAuth = true;
        $mail->Username = 'reilypre@gmail.com'; // Replace with your Gmail address
        $mail->Password = 'cghb vfaa ksug sfzo';    // Replace with your Gmail App Password
        $mail->SMTPSecure = 'tls';
        $mail->Port = 587;

        // Email details
        $mail->setFrom($email, $name);           // Sender’s email and name (from the form)
        $mail->addAddress('reilypre@gmail.com'); // Your Gmail where messages will go
        $mail->Subject = "New Contact Form Message from $name";
        $mail->Body = "Name: $name\nEmail: $email\nMessage:\n$message";

        // Send the email
        $mail->send();
        echo "Message sent successfully! I’ll get back to you soon.";
    } catch (Exception $e) {
        echo "Sorry, there was an error sending your message: " . $mail->ErrorInfo;
    }
}
?>