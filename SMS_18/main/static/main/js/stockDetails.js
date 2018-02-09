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

// Get the modal
	var modal = document.getElementById('myModal');
	var modals = document.getElementById('myModals');
	// Get the button that opens the modal
	var btn = document.getElementById("myBtn");

	// Get the <span> element that closes the modal
	var span = document.getElementById("close");
	var spans = document.getElementById("closes");
	// When the user clicks the button, open the modal 
	function modalOpen() {
	    modal.style.display = "block";
	}

	function modalOpenS() {
		modals.style.display = "block";
	}

	// When the user clicks on <span> (x), close the modal
	span.onclick = function() {
	    modal.style.display = "none";
	}
	spans.onclick = function() {
	    modals.style.display = "none";
	}

	// When the user clicks anywhere outside of the modal, close it
	window.onclick = function(event) {
	    if (event.target == modal || event.target == modals) {
	        modal.style.display = "none";
	        modals.style.display = "none";
	    }
	}






