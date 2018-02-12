var url = '/stocksprimarydata';


var xhttp = new XMLHttpRequest();

xhttp.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200){
		var data = JSON.parse(this.responseText);
		var conversionRate = 64;
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
				document.getElementsByClassName('main')[0].innerHTML += '<div class="stock"><div class="shown"><div class="name" id="stockName">'+dataNYM[i].name+'</div><div class="price">&#36 '+dataNYM[i].price/64+'</div></div><div class="hidden"><div class="buy" id="myBtn"> <button onclick="modalOpen('+dataNYM[i].id+')">BUY</button> </div><div class="sell" id="myBtn"> <button class="button" onclick="modalOpenS('+dataNYM[i].id+')">SELL</button></div></div></div>';
				console.log(dataNYM[i].market_type);
			}
				
				
			var j=0;
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