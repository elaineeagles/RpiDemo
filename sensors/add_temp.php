<?php
    // Connect to MySQL
    include("connect.php");
    $snum = $_POST['snum'];
    $sval = $_POST['sval'];
    //$snum = 1;
    //$sval = 5;

     date_default_timezone_set('Europe/London');
    $dateS = date("Y-m-d h:i:sa", time());
    //echo $dateS;
	
	// Prepare the SQL statement
    $SQL = "INSERT INTO myDB.tempdata (snum, sval) VALUES ($snum, $sval)";     
    echo $SQL;
    // Execute SQL statement
    mysql_query($SQL);

    // Go to the review_data.php (optional)
    //header("Location:index.php");
?>
