var url = 'http://127.0.0.1:8000/userstockdetails';

var xhttp = new XMLHttpRequest();

xhttp.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200){
		var data = JSON.parse(this.responseText);
		for (var i = 0; i < data.length; i++) {
			document.getElementsByClassName('main')[0].innerHTML += '<div class="stock"><div class="profile-details">'+data[i].name+'</div><div class="profile-details">'+data[i].num+'</div><div class="profile-details">'+data[i].price+'</div><div class="profile-details">'+data[i].price*data[i].num+'</div></div>';
		}
	}
}

xhttp.open('GET',url, true);
xhttp.send();
