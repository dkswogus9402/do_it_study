<?php
if ( isset($_POST['email']) && isset($_POST['name'])  && isset($_POST['message'])) {
 
  $test = "/(content-type|bcc:|cc:|to:)/i";
  foreach ( $_POST as $key => $val ) {
    if ( preg_match( $test, $val ) ) {
      exit;
    }
  }
  
  mail( "000.lunchbox@gmail.com", $_POST['name'], $_POST['message'], "From:" . $_POST['email'] );
 
}
?>