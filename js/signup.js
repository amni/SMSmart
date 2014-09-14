(function(){
   var emailBox = document.getElementById("emailForm");
   var submitButton = document.getElementById("submitEmail");
   submitButton.addEventListener("click", function(){
      console.log(emailBox.value);
      if(signup(emailBox.value)){
         console.log("signed up!");
      }
      else{
         console.log("not valid email");
      }

   });

})();