var url = '/gameswitchstatus';

var xhttp = new XMLHttpRequest();

xhttp.onreadystatechange = function() {
	if(this.readyState == 4 && this.status == 200)
		var data = JSON.parse(this.responseText);
		console.log(data);
		var i=0;
		if(data.status_of_game = 'closed') {
			while(i<100) {
				function modalOpen() {
					alert('Market is currently down');
			}
			i++;
		}
	}
}

xhttp.open('POST',url, true);
xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded")
xhttp.send("key=9bBo3YmHufzvSYWjbtkURd&email="+sessionStorage.getItem("email"));