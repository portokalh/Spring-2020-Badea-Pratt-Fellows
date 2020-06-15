<?php

  // Create database connection
$db = mysqli_connect("localhost", "root", "", "image_upload");
if(!$db)
die("no db");
if(!mysqli_select_db($db,"image_upload"))
die("No database selected.");

$myspec = $_GET['gender']; // $id is now defined

echo "<a href=\"new_write_out.php?gender=".$myspec."\">Save to CSV</a><br>";
$CSVfp = fopen("mycsv.csv", "r");
if($CSVfp !== FALSE) {
print "<PRE>";
echo "Animal ID\tBrunno\tDate\t\tGenotype\tSex\tAge\n\n";
while(! feof($CSVfp)) {	
	$data = fgetcsv($CSVfp, 1000, ",");
	if ($data[4] == $myspec) {
		echo $data[0]."\t".$data[1]."\t".$data[2]."\t".$data[3]."\t".$data[4]."\t".$data[5]."\t";
		echo "<a href\"insert proper neuroglancer link here (will vary based on cors_pyserver.py)\" src=\"".$data[0]."\" width=\"200\" height=\"200\"> \n\n";
	}
}
}
fclose($CSVfp);
/*
if (move_uploaded_file($_FILES["file"]["tmp_name"], $uploadfile)) 
{
$handle = fopen("$uploadfile", "r");
while (($data = fgetcsv($handle, 1000, ",")) !== FALSE)
{
$import="INSERT into images(id,image,image_text,link) values('$data[0]','$data[1]','$data[2]','$data[3]')";
mysqli_query($db,$import) or die(mysql_error());
}
fclose($handle);
print "Import done";
}
*/

?>