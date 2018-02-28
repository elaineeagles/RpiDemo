<?php
    // Connect to MySQL
    include("connect.php");

    // Prepare the SQL statement
      date_default_timezone_set('Europe/London');
     $dateS = date("Y-m-d h:i:sa", time());
    //echo $dateS;
    $SQL = "INSERT INTO YOUR-DATABASE-NAME.data (date,temperature,humidity,pressure) VALUES ('$dateS','".$_GET["temp"]."','".$_GET["hum"]."','".$_GET["pr"]."')";     

    // Execute SQL statement
    mysql_query($SQL);

    // Go to the review_data.php (optional)
    header("Location:http://www.it-computer.co.uk/index.php");
?>