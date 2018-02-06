var url = 'http://127.0.0.1:8000/stockdata/';
var url2 = 'http://127.0.0.1:8000/userprimarydetails';

var data;
var costPerStock;
var remainingBalance;
var number = 0;
var amount = 0;

var urls = window.location.href.split("/");

var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200){
		data = JSON.parse(this.responseText);
		costPerStock = data.price;
		document.getElementById("stockName").innerHTML = data.name;
		document.getElementById("stockPrice").innerHTML = "&#8377" + " " + costPerStock;
		if(urls[urls.length-2] == "sell") document.getElementById("stocksOwned").innerHTML = data.num;
	}
}
xhttp.open('GET',url+urls[urls.length-1], true);
xhttp.send();


var xhttp2 = new XMLHttpRequest();
xhttp2.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200){
		var data = JSON.parse(this.responseText);
		remainingBalance = data.user_balance;
		document.getElementsByClassName("balance")[0].innerHTML = "&#8377" + " " + remainingBalance;
		if(urls[urls.length-2] == "buy") document.getElementById("stocksOwned").innerHTML = data.num;
	}
}
xhttp2.open('GET',url2, true);
xhttp2.send();


function plusClick() {
	if (remainingBalance >= costPerStock) {
		if(urls[urls.length-2] == "buy" || number < data.num){
			number++;
			document.getElementById("number").value = number;
			amount = costPerStock * number;
			document.getElementById('amount').value  = amount;
			if(urls[urls.length-2] == "buy"){
				remainingBalance -= costPerStock;
			}
			if(urls[urls.length-2] == "sell"){
				remainingBalance += costPerStock;
			}
			document.getElementsByClassName("balance")[0].innerHTML = "&#8377" + " " + remainingBalance;
		}
	}
}

function minusClick() {
	if (number>0) {
		console.log("minus");
		number--;
		document.getElementById("number").value = number;
		amount = costPerStock * number;
		document.getElementById('amount').value  = amount;
		if(urls[urls.length-2] == "buy"){
			remainingBalance += costPerStock;
		}
		if(urls[urls.length-2] == "sell"){
			remainingBalance -= costPerStock;
		}
		document.getElementsByClassName("balance")[0].innerHTML = "&#8377" + " " + remainingBalance;
	}
}
