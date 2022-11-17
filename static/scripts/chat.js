var count = 0
var elem = document.getElementById('content');
elem.scrollTop = elem.scrollHeight;
function refresh(){
    $.ajax({url: "../static/messages.txt", success: function(result){
        var data = JSON.parse(result)
        if (count == 0){
            for (const x in data){
                $(".messages").append('<div class="message"><p>'+JSON.stringify(data[x])+'</p></div>')
            }
        }

        if (count < Object.keys(data).length && count != 0){
            $(".messages").append('<div class="message"><p>'+JSON.stringify(data[Object.keys(data).length])+'</p></div>')
            elem.scrollTop = elem.scrollHeight;
        }
        count = document.getElementsByClassName("message").length
    }});
}

function get_values(){
    var user = $('#user').val();
    var message = $('#message').val();
    var data_send = {user, message}
    var data_json = JSON.stringify(data_send);

    $.ajax({
        url: '/send_message',
        type: 'POST',
        contentType: "application/json",
        data: data_json,
        dataType: "json",
        success: function(response){
            console.log(response);
        },
        error: function(err) {
            console.log(err);
        }
    })
}

function form_func(event){
    event.preventDefault();
    get_values();
    return false;
}

refresh();

setInterval(function(){
    refresh()
}, 1000);
