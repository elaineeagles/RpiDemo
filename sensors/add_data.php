<?php
    // Connect to MySQL
    include("connect.php");
    $snum = $_GET['snum'];
    $sval = $_GET['sval'];

     date_default_timezone_set('Europe/London');
    $dateS = date("Y-m-d h:i:sa", time());
    //echo $dateS;
	
	// Prepare the SQL statement
    $SQL = "INSERT INTO myDB.sensordata (snum, sval, date) VALUES ($snum, $sval, '$dateS')";     

    // Execute SQL statement
    mysql_query($SQL);

    // Go to the review_data.php (optional)
    header("Location:index.php");
?>