var signup = (function(){
   var db = new Firebase("https://getsmsmart.firebaseio.com/");
   var emails = db.child("earlyEmail");
   var existingSignups = [];

   //Add contains function for old browsers
   Array.prototype.contains = function(obj) {
    var i = this.length;
      while (i--) {
        if (this[i] === obj) {
            return true;
        }
      }
      return false;
   };

   function validateEmail(email){
      var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(email);
   }

   emails.on('value', function (snapshot) {
     var signups = snapshot.val();
     existingSignups = [];
     for(var id in signups){
       existingSignups.push(signups[id].email);
     }
     console.log(existingSignups);
   }, function (errorObject) {
     console.log('The read failed: ' + errorObject.code);
   });

   //emails.push({email: });
   return function(emailAddress){
      if(validateEmail(emailAddress)){
         if(!existingSignups.contains(emailAddress)){
             emails.push({email: emailAddress});
         }
         else{

         }

         return true;
      }
      return false;
   };
})();

