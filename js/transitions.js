function changeBg(img_name) {
    $('.intro-header').css('backgroundImage', function () {
        return "url('img/" + img_name + ".jpg')";
    });
};

function addTextBubble(text_input, is_user) {
  if (is_user){
    $('.text').hide(); 
    setTimeout(function () {
    $('.user-text').html(text_input);
    $('.user-text').show();}, 200); 
  } else {
    $('.smsmart-text').html(text_input);
    $('.smsmart-text').show(); 
  }
};


(function callTransitions() {
    var interval = 5000, 
        index = 0,
        is_user = true, 
        img_arr = [{user_text_image: 'map', response_text_image: 'directions'}, {user_text_image: 'receipts', response_text_image: 'restaurant'}, {user_text_image: 'cab', response_text_image: 'goldengate'}],
        text_message_arr = [{user_text: "maps: directions from E Evelyn Ave to Castro Street", response_text: '1. Head west on E Evelyn Ave toward Ferry Morse Way after 0.6 miles <br> 2. Turn left onto Calderon Ave after 0.5 miles <br> 3. Turn right onto Church St after 0.4 miles'}, {user_text: "yelp: find coffee shops on castro street", response_text: 'Red Rock Coffee <br> 3.5 Stars <br> 201 Castro Street'}, {user_text: "venmo: pay Ben 60.00 for taxi to Golden Gate Bridge", response_text: 'You just paid Ben 60.00 for a taxi to Golden Gate Bridge'}];
    function makeTransition() {
      img_object = img_arr[index % text_message_arr.length]; 
      text_message_object = text_message_arr[index % text_message_arr.length]; 

      if (is_user) {
        changeBg(img_object.user_text_image);
        setTimeout('addTextBubble(text_message_object.user_text, true)', 500);
      } else {
        changeBg(img_object.response_text_image); 
        setTimeout('addTextBubble(text_message_object.response_text, false)', 500);
        index+=1; 
      }
      is_user = !is_user 
    }
    makeTransition(); 
    setInterval(makeTransition, interval); 
})(); 

