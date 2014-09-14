(function(){
   var emailBox = document.getElementById("emailForm");
   var submitButton = document.getElementById("submitEmail");
   submitButton.addEventListener("click", function(){
      sendsignup();
   });

   function sendsignup(){
       if(signup(emailBox.value)){
         $('.signup-container').fadeOut(400);
         $('.thank-you-message').fadeIn(400);
      }
      else{
         console.log("not valid email");
      }
   }

   document.addEventListener("keypress", function(e){
      var key = e.which || e.keyCode;
       if (key == 13) { // 13 is enter
         sendsignup();
       }
   });

})();