var url = '/stocksprimarydata';

var xhttp = new XMLHttpRequest();

xhttp.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200){
		var data = JSON.parse(this.responseText);
		/*var conversionRate = 64;
		document.getElementById('conversionRate').innerHTML = conversionRate;*/
		if ('error' in data){
			alert(data.error);
		}else{
			var k=0;
			var dataIndian = [];
			for (var c=0; c<data.length; c++) {
				if(data[c].market_type == "BSE" || data[c].market_type == "Both") {
					dataIndian[k] = data[c];
					k++;
					}
				}	
			for (var i = 0; i < dataIndian.length; i++) {
				document.getElementsByClassName('main')[0].innerHTML += '<div class="stock"><div class="shown"><div class="name" id="stockName">'+dataIndian[i].name+'</div><div class="price">&#8377 <span>' + dataIndian[i].price + ' </span><span class="increasePrice"> &#x25B2; </span><span class="decreasePrice"> &#x25BC; </span></div></div><div class="hidden"><div class="buy" id="myBtn" name="buy"> <button onclick="modalOpen('+dataIndian[i].id+')">BUY</button> </div><div class="sell" id="myBtn" name="sell"> <button class="button" onclick="modalOpenS('+dataIndian[i].id+')">SELL</button></div></div></div>';
				if(dataIndian[i].price_trend>0) {
					document.getElementsByClassName("increasePrice")[i].style.display = "inline";
				}
				else if (dataIndian[i].price_trend<0) {
					document.getElementsByClassName("decreasePrice")[i].style.display = "inline";
				}
			}
				
				
			var j=1;
			while (j<=dataIndian.length){
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












