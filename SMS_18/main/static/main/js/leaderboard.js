var url = 'http://127.0.0.1:8000/lbdata';

var xhttp = new XMLHttpRequest();

xhttp.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200){
		var data = JSON.parse(this.responseText);
		for (var i = 0; i < data.length; i++) {
			document.getElementsByClassName('main')[0].innerHTML += '<div class="profileLeader"> <div class="leader">'+data[i].name+'</div><div class="balance">'+data[i].net_worth+'</div> </div>';
		}
	}
}

xhttp.open('GET',url, true);
xhttp.send();
