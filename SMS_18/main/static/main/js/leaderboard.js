var url = '/lbdata';

var xhttp = new XMLHttpRequest();

xhttp.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200){
		var data = JSON.parse(this.responseText);
		/*var conversionRate = 64;*/
		var el = document.getElementsByClassName('main')[0];	
		/*document.getElementById('conversionRate').innerHTML = conversionRate;*/
		if ('error' in data){
			alert(data.error);
		}else{
			for (var i = 0; i < 5; i++) {
				el.innerHTML += '<div class="profileLeader"> <div class="leader"><span>'+ (i+1) +' - </span><span>' + data[i].name + '</span></div><div class="balance">'+data[i].net_worth+'</div> </div>';
				if(data[data.length-1].rank == i) {
					document.getElementsByClassName('profileLeader')[i-1].style.color = 'red';
				}
			}
			if(data[data.length-1].rank>5){
				console.log(data[data.length-1])
				el.innerHTML += '<div class="profileLeader currentUser"> <div class="leader"><span>'+data[data.length-1].rank+' - </span><span>' + data[data.length-1].name + '</span></div><div class="balance">'+data[data.length-1].net_worth+'</div> </div>';
				document.getElementsByClassName('currentUser')[0].style.color = 'red';
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
