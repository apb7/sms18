var url = '/stocksprimarydata';


var xhttp = new XMLHttpRequest();

xhttp.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200){
		var data = JSON.parse(this.responseText);
		var conversionRate = 64;
		console.log(data);
		/*document.getElementById('conversionRate').innerHTML = conversionRate;*/
		if ('error' in data){
			alert(data.error);
		}else{
			var k=0;
			var dataNYM = [];
			for (var c=0; c<data.length; c++) {
				if(data[c].market_type == "NYM" || data[c].market_type == "Both") {
					dataNYM[k] = data[c];
					k++;
					}
				}	
			for (var i = 0; i < dataNYM.length; i++) {
				document.getElementsByClassName('main')[0].innerHTML += '<div class="stock"><div class="shown"><div class="name" id="stockName">'+dataNYM[i].name+'</div><div class="price">&#36 <span>' + dataNYM[i].price + ' </span><span class="increasePrice"> &#x25B2; </span><span class="decreasePrice"> &#x25BC; </span></div></div><div class="hidden"><div class="buy" id="myBtn"> <button onclick="modalOpen('+dataNYM[i].id+')">BUY</button> </div><div class="sell" id="myBtn"> <button class="button" onclick="modalOpenS('+dataNYM[i].id+')">SELL</button></div></div></div>';
				if(dataNYM[i].price_trend>0) {	
					document.getElementsByClassName("increasePrice")[i].style.display = "inline";
				}
				else if (dataNYM[i].price_trend<0) {
					document.getElementsByClassName("decreasePrice")[i].style.display = "inline";
				}
			}
				
				
			var j=1;
			while (j<=dataNYM.length){
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