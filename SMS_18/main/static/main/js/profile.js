var url = '/userstockdetails';

var xhttp = new XMLHttpRequest();

xhttp.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200){
		var data = JSON.parse(this.responseText);
		if ('error' in data){
			alert(data.error);
		}else{
			for (var i = 0; i < data.length; i++) {
				document.getElementsByClassName('main')[0].innerHTML += '<div class="stock"><div class="profile-details">'+data[i].name+'</div><div class="profile-details">'+data[i].num+'</div><div class="profile-details">'+data[i].price+'</div><div class="profile-details">'+data[i].price*data[i].num+'</div></div>';
			}
		}
	}
}

xhttp.open('POST',url, true);
xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded")
xhttp.send("key=9bBo3YmHufzvSYWjbtkURd&email="+sessionStorage.getItem("email"));

function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}	
