function xhrPost(url, params, callback) {
	var xhr = new XMLHttpRequest();
	xhr.open("POST", url, true);
	xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhr.onload = callback;
	xhr.send(params);
}

var btn = document.getElementById('submit');
var tpl = _.template(document.getElementById('templ-results').innerHTML);
btn.addEventListener("click", function(event) {
	var txt = document.getElementById('txt').value;
	console.log(txt);
	var params = "txt="+txt;
	xhrPost('web/text/', params, function () {		
		var data = JSON.parse(this.responseText);
		document.getElementById('result').innerHTML = tpl(data);
	});
});