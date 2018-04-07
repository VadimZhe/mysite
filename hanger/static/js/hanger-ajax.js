$('#show_it').click(function(){
    console.log("AJAX starting...")
    $.get('/hanger/showme/',0, function(data){
        $('#target').html("You clicked!");
    });
});