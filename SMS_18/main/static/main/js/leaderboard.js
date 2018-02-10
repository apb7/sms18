var url = '/lbdata';

var xhttp = new XMLHttpRequest();

xhttp.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200){
		var data = JSON.parse(this.responseText);
		if ('error' in data){
			alert(data.error);
		}else{
			for (var i = 0; i < data.length; i++) {
				document.getElementsByClassName('main')[0].innerHTML += '<div class="profileLeader"> <div class="leader">'+data[i].name+'</div><div class="balance">'+data[i].net_worth+'</div> </div>';
			}
		}
	}
}

xhttp.open('POST',url, true);
xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded")
xhttp.send("key=9bBo3YmHufzvSYWjbtkURd");



function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}	
