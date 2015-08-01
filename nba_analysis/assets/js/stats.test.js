var $voteForm = $("form.vote_form");
$(document).ready(funtion(){
  // $("form.vote_form").click(function(event){
  //   event.preventDefault();
  //   $.ajax({
  //     type: "POST",
  //     url: "",
  //     data:{

  //     }
  //   });
  //   return false;
  // });

  // This is test function for now
  $voteForm.click(function(event){
    event.preventDefault();
    console.log($voteForm.serialize());
  });
});