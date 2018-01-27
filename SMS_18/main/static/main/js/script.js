/* BUY PAGE */
	var number = 0;
	var amount=0;
	var costPerStock = 50;  // COST OF STOCK; DATA FROM BACKEND FOR EACH STOCK
	var remainingBalance = 1000;

	document.getElementsByClassName('amount')[0].innerHTML  = "&#8377" + " " + amount;
	document.getElementsByClassName("number")[0].innerHTML = number;
	document.getElementsByClassName("balance")[0].innerHTML = "&#8377" + " " + remainingBalance;
	document.getElementsByClassName('stock-price')[0].innerHTML = "&#8377" + " " + costPerStock;


	function plusClick() {												 //FOR INCREMENTING COUNTER				
		if (remainingBalance >= costPerStock) {
			number = number + 1;
			document.getElementsByClassName("number")[0].innerHTML = number;
			amount = costPerStock * number;
			document.getElementsByClassName('amount')[0].innerHTML  = "&#8377" + " " + amount;
			remainingBalance = remainingBalance - costPerStock;
			document.getElementsByClassName("balance")[0].innerHTML = "&#8377" + " " + remainingBalance;
		}
	}

	function minusClick() {
		if (number>0) {
			number = number - 1;
			document.getElementsByClassName("number")[0].innerHTML = number;
			amount = costPerStock * number;
			document.getElementsByClassName('amount')[0].innerHTML  = "&#8377" + " " + amount;
			remainingBalance = remainingBalance + costPerStock;
			document.getElementsByClassName("balance")[0].innerHTML = "&#8377" + " " + remainingBalance;
		}
		else {
			document.getElementsByClassName("number")[0].innerHTML = number;
		} 

	}


/* SELL PAGE */


	var increasedBalance = 1000;
	var stocksOwned = 12;

	document.getElementsByClassName('amount')[0].innerHTML  = "&#8377" + " " + amount;
	document.getElementsByClassName("number")[0].innerHTML = number;
	document.getElementsByClassName("balance")[0].innerHTML = "&#8377" + " " + increasedBalance;
	document.getElementsByClassName('stock-price')[0].innerHTML = "&#8377" + " " + costPerStock;
	document.getElementsByClassName('stocksOwned')[0].innerHTML = stocksOwned;

	function plusClick() {												 //FOR INCREMENTING COUNTER				
		if (number<stocksOwned) {
			number = number + 1;
			document.getElementsByClassName("number")[0].innerHTML = number;
			amount = costPerStock * number;
			document.getElementsByClassName('amount')[0].innerHTML  = "&#8377" + " " + amount;
			increasedBalance = increasedBalance + costPerStock;
			document.getElementsByClassName("balance")[0].innerHTML = "&#8377" + " " + increasedBalance;
		}
	}

	function minusClick() {
		if (number>0) {
			number = number - 1;
			document.getElementsByClassName("number")[0].innerHTML = number;
			amount = costPerStock * number;
			document.getElementsByClassName('amount')[0].innerHTML  = "&#8377" + " " + amount;
			increasedBalance = increasedBalance - costPerStock;
			document.getElementsByClassName("balance")[0].innerHTML = "&#8377" + " " + increasedBalance;
		}
		else {
			document.getElementsByClassName("number")[0].innerHTML = number;
		} 

	}





