function changeBg(img_name) {
    $('.intro-header').css('backgroundImage', function () {
      $('.intro-header').delay(3000).animate({
          backgroundColor: 'rgb(255,255,255)'
      }, 3000);
        return "url('img/" + img_name + ".jpg')";
    });
};

function addTextBubble(text_input, is_user) {
  if (is_user){
    $('.text').hide(); 
    setTimeout(function () {
    $('.user-text').text(text_input);
    $('.user-text').show();}, 200); 
  } else {
    $('.smsmart-text').text(text_input);
    $('.smsmart-text').show(); 
  }
};


(function callTransitions() {
    var interval = 5000, 
        index = 0,
        is_user = true, 
        img_arr = [{user_text_image: 'directions', response_text_image: 'map'}, {user_text_image: 'directions', response_text_image: 'map'}, {user_text_image: 'directions', response_text_image: 'map'}],
        text_message_arr = [{user_text: "maps: directions from Duke Chapel to Wannamaker Drive", response_text: '1. Turn Left\n2. Then go right\n3. You arrived at the destination'}, {user_text: "maps: directions from Duke Chapel to Wannamaker Drive", response_text: '1. Turn Left\n2. Then go right\n3. You arrived at the destination'}, {user_text: "maps: directions from Duke Chapel to Wannamaker Drive", response_text: '1. Turn Left\n2. Then go right\n3. You arrived at the destination'}];
    function makeTransition() {
      changeBg();  
      img_object = img_arr[index % text_message_arr.length]; 
      text_message_object = text_message_arr[index % text_message_arr.length]; 

      if (is_user) {
        changeBg(img_object.user_text_image);
        setTimeout('addTextBubble(text_message_object.user_text, true)', 500);
      } else {
        changeBg(img_object.response_text_image); 
        setTimeout('addTextBubble(text_message_object.response_text, false)', 500);
      }
      is_user = !is_user 
      index+=1; 
    }
    makeTransition(); 
    setInterval(makeTransition, interval); 
})(); 

