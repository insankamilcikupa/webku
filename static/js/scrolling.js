$(window).scroll(function(){
    var scroll = $(window).scrollTop();
    console.log(scroll)

    if(scroll >= 250){
        $("#Nav-ku").addClass("bg-dark");
    }
    else{
        $("#Nav-ku").removeClass("bg-dark");
    }
});