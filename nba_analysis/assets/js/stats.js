var $voteForm = $("form.vote_form");
var $authen = $("ul.authen");

$(document).ready(function(){
  $voteForm.click(function(event){
    event.preventDefault();
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
  });
});