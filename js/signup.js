(function(){
   var emailBox = document.getElementById("emailForm");
   var submitButton = document.getElementById("submitEmail");
   submitButton.addEventListener("click", function(){
      console.log(emailBox.value);
      if(signup(emailBox.value)){
         $('.signup-container').fadeOut(400);
         $('.thank-you-message').fadeIn(400);
      }
      else{
         console.log("not valid email");
      }

   });

})();