// Get the modal
	var modal = document.getElementById('myModal');
	var modals = document.getElementById('myModals');
	var sidenav = document.getElementById('mySidenav');
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
	    if (event.target == modal || event.target == modals|| event.target == sidenav ) {
	        modal.style.display = "none";
	        modals.style.display = "none";
	        sidenav.style.display = "none";
	    }
	}




//sidenav

function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}	