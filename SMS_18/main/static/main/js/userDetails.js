var url = 'http://127.0.0.1:8000/userprimarydetails';

var xhttp = new XMLHttpRequest();

xhttp.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200){
		var data = JSON.parse(this.responseText);
		document.getElementById("userName").innerHTML ='<b>' + data.username + '</b>';
		document.getElementById("userBalance").innerHTML = data.user_balance;
	}
}

xhttp.open('GET',url, true);
xhttp.send();
