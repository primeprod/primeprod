function myFunction(){
  // Get the checkbox
  var myCheck = document.getElementById("myCheck");
  //   Get the output text
  var text = document.getElementById("text");

  // If the checkbox is checked, display the output text
  if (checkbox_cgv.checked == true){
    text.style.display = "block";
  } else {
    text.style.display = "none";
  }
}
