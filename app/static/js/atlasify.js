$(document).ready(function(){
    $('#button').click(function() {
        var query = $('#query').val();
        var option = $('#option').val();
        var data ={};
        data['query'] = query;
        data ['option'] = option;        
        $.ajax({
            url: '/temp',
            data: JSON.stringify(data),
            dataType: 'json',
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            success: function(response) {
                $("#content").write(response);
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});