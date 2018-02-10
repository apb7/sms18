var url = '/stocksprimarydata';

var xhttp = new XMLHttpRequest();

xhttp.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200){
		var data = JSON.parse(this.responseText);
		if ('error' in data){
			alert(data.error);
		}else{
			for (var i = 0; i < data.length; i++) {
				document.getElementsByClassName('main')[0].innerHTML += '<div class="stock"><div class="shown"><div class="name" id="stockName">'+data[i].name+'</div><div class="price">&#8377 '+data[i].price+'</div></div><div class="hidden"><div class="buy" id="myBtn"> <button onclick="modalOpen('+data[i].id+')">BUY</button> </div><div class="sell" id="myBtn"> <button class="button" onclick="modalOpenS('+data[i].id+')">SELL</button></div></div></div>';
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
}


function openBuy() {
	document.getElementsByClassName("formBuy")[0].style.display = "block";
	console.log("opened");
}

function openSell() {
	document.getElementsByClassName("formSell")[0].style.display = "block";
	console.log("opened");
}

xhttp.open('POST',url, true);
xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded")
xhttp.send("key=9bBo3YmHufzvSYWjbtkURd");

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












