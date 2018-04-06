$('#show_it').click(function(){
    $.get('/hanger/showme/', {0}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
    });
});