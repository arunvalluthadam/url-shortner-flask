function makeid()
{
    var text = "";
    var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

    for( var i=0; i < 5; i++ )
        text += possible.charAt(Math.floor(Math.random() * possible.length));

    return text;
}
// --------------------------------------------------------------

$(function() {
	$("#submit_btn").click(function() {
		var long_url = $("#longurl").val();
		var code_url = makeid();
		$.post('/add', {long_url: long_url, short_url: code_url},function(data) {
			$("#show_long").html(data.long_url);
			$("#show_short").html("http://localhost:5000/"+data.short_url);
		});
	});
});

