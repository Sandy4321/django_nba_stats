var $voteForm = $("form.vote_form");
var $authen = $("input.authen")[0];

//the lightbox in this is compleeteeeellyyy wrong but id rather be working on other stuff than fixing this. i will fix this later.
//Problem: hard coded styles so that everything is centered correctly on a large screen but not responsive on mobile.
function displayOverlay(){
  var $overlay = $('<div id="overlay" class="row"></div>');
  var $msg1 = $('<div class="span12"><h1 id="lightbox-text" class="text-center">you need to be logged in to vote!</h1></div>');
  var $msg2 = $('<div class="span12"><p id="lightbox-text" class="text-center">Please login with Facebook or Google+</p></div>');
  var $socialIcons = $('<div class="span3 offset3"><a href="/login/facebook/?next=/stats/"><img class="lightbox-icon1" src="/static/img/facebookicon.png" alt="facebookicon"></a><a href="/login/google-oauth2/?next=/stats/"><img class="lightbox-icon2" src="/static/img/googleicon.png" alt="googleicon"></a></div>');
  $overlay.append($msg1);
  $overlay.append($msg2);
  $overlay.append($socialIcons);
  $overlay.lightbox_me({
    centered: true
  });
}

$(document).ready(function(){
  $voteForm.click(function(event){
    event.preventDefault();
    if($authen.value == 'false'){
      console.log("you must log in to vote");
      displayOverlay();
    }
    else{
      var data = $(this).serializeArray();
      var csrf = data[0].value;
      var player_id = data[1].value;
      var voteType = data[2].value;
      var prevVote = data[3].value;
      var count = 0;

      //if user clicked on upvote
      if(voteType == "up")
      {
        //getting downvote info (need a better way to do this)
        var $downData = $(this).next().next();
        var $downDataArray = $downData.serializeArray();
        var prevDownVote = $downDataArray[3].value;
        if(prevDownVote == "yes"){
          count += 1
          $downData.children('input[name="prevVote"]').attr("value","no");
          $downData.children('input[id="vote_button"]').attr("src", "/static/img/downvote.png");
        }

        var $prevVoteManip = $(this).children('input[name="prevVote"]');
        if(prevVote == 'no'){
          count += 1
          $prevVoteManip.attr("value","yes");
          $(this).children('input[id="vote_button"]').attr("src", "/static/img/upvote_clicked.png");
        }
        else{
          count -= 1
          $prevVoteManip.attr("value","no");
          $(this).children('input[id="vote_button"]').attr("src", "/static/img/upvote.png");
        }
        var changeNumber = parseInt($(this).next().text()); //base 10
        changeNumber += count;
        $(this).next().text(changeNumber)
      }
      //if user clicked on downvote
      else
      {
        var $upData = $(this).prev().prev();
        var $upDataArray = $upData.serializeArray();
        var prevUpVote = $upDataArray[3].value;
        if(prevUpVote == "yes"){
          count -= 1
          $upData.children('input[name="prevVote"]').attr("value","no");
          $upData.children('input[id="vote_button"]').attr("src", "/static/img/upvote.png");
        }

        var $prevVoteManip = $(this).children('input[name="prevVote"]');
        if(prevVote == 'no'){
          count -= 1
          $prevVoteManip.attr("value","yes");
          $(this).children('input[id="vote_button"]').attr("src", "/static/img/downvote_clicked.png");
        }

        else{
          count += 1
          $prevVoteManip.attr("value","no");
          $(this).children('input[id="vote_button"]').attr("src", "/static/img/downvote.png");
        }
        var changeNumber = parseInt($(this).prev().text()); //base 10
        changeNumber += count;
        $(this).prev().text(changeNumber)
      }
      $.ajax({
        type: "POST",
        url:"/stats/userrank/vote/",
        data:{
          'csrfmiddlewaretoken': csrf,
          'player_id': player_id,
          'voteType': voteType,
          'count': count
        },
        success: function(){
          console.log("Vote was submitted");
        }
      });
    }
  });
});