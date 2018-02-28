<?php
$MyUsername = "root";  // enter your username for mysql
$MyPassword = "test";  // enter your password for mysql
$MyHostname = "localhost";  // this is usually "localhost" unless your database resides on a different server


$dbh = mysql_pconnect($MyHostname , $MyUsername, $MyPassword);
$selected = mysql_select_db("myDB",$dbh); //Enter your database name here 
echo "Connected to database";
?>
