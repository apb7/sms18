//sidenav

function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}

//form submit

function buyStocks() {

	var http = new XMLHttpRequest();
	/*e.preventDefault();*/
	var data = "key=9bBo3YmHufzvSYWjbtkURd&email="+sessionStorage.getItem("email");
	data += "&units="+document.getElementById("purchaseAmount").value;
	http.onreadystatechange = function() {
	 	if(http.readyState == 4 && http.status == 200) {
	 		data = JSON.parse(http.responseText);
			if ('error' in data){
				alert(data.error);
			}else{
		 		alert(data.message);
		 	}
		}
	}	
	http.open("POST", '/buystocks/'+stockId, true);
	http.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
	http.send(data);

};

function sellStocks() {
	var http = new XMLHttpRequest();
	/*e.preventDefault();*/
	var data = "key=9bBo3YmHufzvSYWjbtkURd&email="+sessionStorage.getItem("email");
	data += "&units="+document.getElementById("sellAmount").value;
	http.onreadystatechange = function() {
	 	if(http.readyState == 4 && http.status == 200) {
	 		data = JSON.parse(http.responseText);
			if ('error' in data){
				alert(data.error);
			}else{
		 		alert(data.message);
		 	}
		}
	}	
	http.open("POST", '/sellstocks/'+stockId, true);
	http.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
	http.send(data);

}
