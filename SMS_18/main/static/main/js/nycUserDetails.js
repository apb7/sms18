var url = '/userprimarydetails';


var xhttp = new XMLHttpRequest();

xhttp.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200){
		var data = JSON.parse(this.responseText);
		var conversionRate = 64; 
		if ('error' in data){
			alert(data.error);
		}else{
			document.getElementById("userName").innerHTML ='<b>' + data.username + '</b>';
			document.getElementById("userBalance").innerHTML = (data.user_balance/conversionRate).toFixed(2);
		}
	}
}

xhttp.open('POST',url, true);
xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded")
xhttp.send("key=9bBo3YmHufzvSYWjbtkURd&email="+sessionStorage.getItem("email"));
