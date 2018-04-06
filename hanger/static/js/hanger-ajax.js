$('#show_it').click(function(){
    $.get('/hanger/showme/', {0}, function(data){
               $('#the_object"').html("Here I am!");
    });
});