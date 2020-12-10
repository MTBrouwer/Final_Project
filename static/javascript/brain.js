$(document).ready(function(){
  // Write your JavaScript code here
    console.log("The page is ready!");
$("#StudentForm" ).click(function() {
           disableStudentForm();
    });
$("#InterestForm" ).click(function() {
            disableInterestForm();
    });
$("#FavoriteForm" ).click(function() {
           disableFavoriteForm();
    });
});
