var url = '/getnewspost';

var xhttp = new XMLHttpRequest();

xhttp.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200){
		var data = JSON.parse(this.responseText);
		var conversionRate = 64;
		/*document.getElementById('conversionRate').innerHTML = conversionRate;*/
		if ('error' in data){
			alert(data.error);
		}
		else {
			for (var i=0; i<data.length; i++) {
					console.log(data);
					document.getElementsByClassName('main')[0].innerHTML += '<div class="profileLeader"><span class="balance1">' +  data[i].post_text + '</span><span class="balance2">'+data[i].time_of_post+'</div';
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
