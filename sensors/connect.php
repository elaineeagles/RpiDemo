<?php
$MyUsername = "";  // enter your username for mysql
$MyPassword = "";  // enter your password for mysql
$MyHostname = "";  // this is usually "localhost" unless your database resides on a different server


$dbh = mysql_pconnect($MyHostname , $MyUsername, $MyPassword);
$selected = mysql_select_db("YOUR DATA BASE NAME",$dbh); //Enter your database name here 
?>