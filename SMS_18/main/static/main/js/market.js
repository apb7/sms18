//sidenav

function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}

//form submit

function buyStocks() {
if(document.getElementById("purchaseAmount").value>0) {
	var http = new XMLHttpRequest();
	/*e.preventDefault();*/
	var data = "key=9bBo3YmHufzvSYWjbtkURd&email="+localStorage.getItem("email");
	data += "&units="+document.getElementById("purchaseAmount").value;
	var i;
	/*while (i <= document.getElementsByClassName('modal').length) {
		if(document.getElementById("purchaseAmount")<0) {
			document.getElementsByClassName('myButton')[i].disabled = true;
		}
	}*/
	http.onreadystatechange = function() {
	 	if(http.readyState == 4 && http.status == 200) {
	 		data = JSON.parse(http.responseText);
			if ('error' in data){
				document.getElementsByClassName('errorText')[0].innerHTML = data.error;
				/*setTimeout(function(){window.location.reload();},500)*/
			}else{
		 		/*alert(data.message);*/
		 		setTimeout(function(){window.location.reload();},10)
		 	}
		}
	}
	http.open("POST", '/buystocks/'+stockId, true);
	http.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
	http.send(data);
}
else(alert('Enter positive integer value (Nice try, Genius!)'));
};

function sellStocks() {
    if(document.getElementById("sellAmount").value>0) {
	var http = new XMLHttpRequest();
	/*e.preventDefault();*/
	var data = "key=9bBo3YmHufzvSYWjbtkURd&email="+localStorage.getItem("email");
	data += "&units="+document.getElementById("sellAmount").value;
	var i;
	/*while (i <= document.getElementsByClassName('modal').length) {
		if(document.getElementById("sellAmount")<0) {
			document.getElementsByClassName('myButton')[i].disabled = true;
		}
	}*/
	http.onreadystatechange = function() {
	 	if(http.readyState == 4 && http.status == 200) {
	 		data = JSON.parse(http.responseText);
			if ('error' in data){
				document.getElementsByClassName('errorText')[1].innerHTML = data.error;
				/*setTimeout(function(){window.location.reload();},500)*/
			}else{
		 		/*alert(data.message);*/
		 		setTimeout(function(){window.location.reload();},10)
		 	}
		}
	}
	http.open("POST", '/sellstocks/'+stockId, true);
	http.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
	http.send(data);
}
else (alert('Enter positive integer value (Nice try, Genius!)'));
}
