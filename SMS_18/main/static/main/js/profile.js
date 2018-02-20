var url = '/userstockdetails';

var xhttp = new XMLHttpRequest();

xhttp.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200){
		var data = JSON.parse(this.responseText);
		/*console.log(data);
		var conversionRate = 64;
		document.getElementById('conversionRate').innerHTML = conversionRate;*/
		if ('error' in data){
			alert(data.error);
		}else{
			for (var i = 0; i < data.length; i++) {
				if(data[i].market_type == "BSE" || data[i].market_type == "Both") {
					if((data[i].average_price-data[i].price) >= 0 )
						document.getElementsByClassName('main')[0].innerHTML += '<div class="stock"><div class="profile-details">'+data[i].name+'</div><div class="profile-details">'+data[i].num+'</div><div class="profile-details"><div>&#8377 <span>'+data[i].average_price+'</span><span class="percentChange"> ' + ((data[i].price-data[i].average_price)/data[i].price).toFixed(0)*100 + '%</span></div></div><div class="profile-details">&#8377 <span>'+data[i].average_price*data[i].num+'</span></div></div>';
					else
						document.getElementsByClassName('main')[0].innerHTML += '<div class="stock"><div class="profile-details">'+data[i].name+'</div><div class="profile-details">'+data[i].num+'</div><div class="profile-details"><div>&#8377 <span>'+data[i].average_price+'</span><span class="percentChangeDown"> ' + ((data[i].price-data[i].average_price)/data[i].price).toFixed(0)*100 + '%</span></div></div><div class="profile-details">&#8377 <span>'+data[i].average_price*data[i].num+'</span></div></div>';
					}
				else {
					if((data[i].average_price-data[i].price) >= 0 ) 
						document.getElementsByClassName('main')[0].innerHTML += '<div class="stock"><div class="profile-details">'+data[i].name+'</div><div class="profile-details">'+data[i].num+'</div><div class="profile-details"><div><span>$'+data[i].average_price+'</span><span class="percentChange"> '+((data[i].price-data[i].average_price)/data[i].price).toFixed(0)*100+'%</div></div><div class="profile-details">$'+(data[i].average_price*data[i].num).toFixed(1)+'</div></div>';
					else
					document.getElementsByClassName('main')[0].innerHTML += '<div class="stock"><div class="profile-details">'+data[i].name+'</div><div class="profile-details">'+data[i].num+'</div><div class="profile-details"><div><span>$'+data[i].average_price+'</span><span class="percentChangeDown"> '+((data[i].price-data[i].average_price)/data[i].price).toFixed(0)*100+'%</div></div><div class="profile-details">$'+(data[i].average_price*data[i].num).toFixed(1)+'</div></div>';
				}
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
