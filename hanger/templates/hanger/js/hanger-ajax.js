$('#show_it').click(function(){
    $.get('/hanger/showme/', {0}, function(data){
               console.log("AJAX starting...")
               $('#the_object"').html("Here I am!");
    });
});