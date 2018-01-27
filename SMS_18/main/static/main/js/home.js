
/* HOME PAGE */

var i=0;
while (i<12){
	document.getElementsByClassName("stock")[i].addEventListener("click", function(){
		this.classList.toggle("show");
	});
	i=i+1;
}

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

