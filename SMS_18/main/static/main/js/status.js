var url = '/gameswitchstatus';

var xhttp = new XMLHttpRequest();

xhttp.onreadystatechange = function() {
	if(this.readyState == 4 && this.status == 200)
		var data = JSON.parse(this.responseText);
		console.log(data);
}

xhttp.open('POST',url, true);
xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded")
xhttp.send("key=9bBo3YmHufzvSYWjbtkURd&email="+sessionStorage.getItem("email"));