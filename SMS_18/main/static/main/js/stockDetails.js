var url = 'http://127.0.0.1:8000/stocksprimarydata';

var xhttp = new XMLHttpRequest();

xhttp.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200){
		var data = JSON.parse(this.responseText);
		for (var i = 0; i < data.length; i++) {
			document.getElementsByClassName('main')[0].innerHTML += '<div class="stock"><div class="shown"><div class="name" id="stockName">'+data[i].name+'</div><div class="price">&#8377 '+data[i].price+'</div></div><div class="hidden"><div class="buy" id="myBtn"> <button onclick="modalOpen()">BUY</button> </div><div class="sell" id="myBtn"> <button class="button" onclick="modalOpenS()">SELL</button></div></div></div>';
		}
		var j=0;
		while (j<=data.length){
		document.getElementsByClassName("stock")[j].addEventListener("click", function(){
			this.classList.toggle("show");
		});
		j=j+1;
		}
	}
}

function openBuy() {
	document.getElementsByClassName("formBuy")[0].style.display = "block";
	console.log("opened");
}

function openSell() {
	document.getElementsByClassName("formSell")[0].style.display = "block";
	console.log("opened");
}

xhttp.open('GET',url, true);
xhttp.send();

function closeBuy() {
	document.getElementsByClassName("formBuy")[0].style.display = "none";
}


/* HOME PAGE */

/*
var costPerStock = 50;
var stocksOwned=0;

var j=0;
while (j<12) {
		if (stocksOwned == 0){
		document.getElementsByClassName('button')[j].disabled = true;
		document.getElementsByClassName('button')[j].classList.add('disabled');
		j++;
	}
}

*/






//sidenav

function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}	








