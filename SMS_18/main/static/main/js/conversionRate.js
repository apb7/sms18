var url = '/getconversionrate';

var xhttp = new XMLHttpRequest();

xhttp.onreadystatechange = function() {
	if(this.readyState == 4 && this.status == 200)
		var data = JSON.parse(this.responseText);
		console.log(data);
		document.getElementById('conversionRate').innerHTML = data.conversion_rate;
<<<<<<< HEAD
=======
		alert(conversion_rate);	
>>>>>>> df071b9d73062e6a7c98956dfafb9c9d9c40f3b3
}

xhttp.open('POST',url, true);
xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded")
xhttp.send("key=9bBo3YmHufzvSYWjbtkURd&email="+sessionStorage.getItem("email"));