var btn = document.getElementById('submit');
var tpl = _.template(document.getElementById('templ-results').innerHTML);
btn.addEventListener("click", function(event) {
	var txt = document.getElementById('txt').value;
	$.post('web/text/', {"txt": txt}, function (data) {		
		document.getElementById('result').innerHTML = tpl(data);
	});
});