var $voteForm = $("form.vote_form");
$(document).ready(function(){

  $voteForm.click(function(event){
    event.preventDefault();
    var data = $(this).serializeArray();
    var csrf = data[0].value;
    var player_id = data[1].value;
    var voteType = data[2].value;
    var prevVote = data[3].value;
    console.log(player_id);
    console.log(voteType);
    console.log(prevVote);

    //Changing previous voting state
    var $prevVoteManip = $(this).children('input[name="prevVote"]'); 
    if(prevVote == 'no'){
      $prevVoteManip.attr("value","yes");

      //changing image of the arrow
      if(voteType == "up") $(this).children('input[id="vote_button"]').attr("src", "/static/img/upvote_clicked.png");
      else $(this).children('input[id="vote_button"]').attr("src", "/static/img/downvote_clicked.png");
    }

    else{
      $prevVoteManip.attr("value","no");
      
      //changing image of the arrow
      if(voteType == "up") $(this).children('input[id="vote_button"]').attr("src", "/static/img/upvote.png");
      else $(this).children('input[id="vote_button"]').attr("src", "/static/img/downvote.png");
    }
  });
});