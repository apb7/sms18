var loginForm = document.getElementsByClassName("email-login")[0];

		loginForm.onsubmit = function(e) {
		
		var http = new XMLHttpRequest();	
		e.preventDefault();
		var data['username'] = loginForm.username.value;

	}
        http.open("POST", 'action', true);
		http.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
		http.send(data);