<?php 


$myspec = $_GET['gender']; // $id is now defined


    $file = "mycsv.csv";
    $f = fopen($file, "r");
    $i = 0;

    $file2 = str_replace(".csv", "_new.csv", $file);
    $f2 = fopen($file2,"a");

    while(! feof($f)) { 
        $record = fgetcsv($f, 1000, ",");
        foreach($record as $field) {
            if ($record[4] == $myspec) {
                echo $field . "<br>";
            }
        }

        $i++;
    }

    fwrite($f2,fread($f, filesize($file)));

    fclose($f);
    fclose($f2);

?>
