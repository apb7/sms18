## This file consists of the list of urls on our project along with the JSON response that is being sent corresponding to that url.

                    
1:       **URLS(main/urls.py):**'/buystocks/(?P<id>\d+)$' (i.e. /buystocks/stock id)

**VIEW(main/views.py):** BuyStocks
					
**json data:** in case the user is not authenticated:	resp = {'error':'The user is not registered yet.'}
				in case user doesn't have sufficient balance: resp = {'error':'Not sufficient balance to proceed the transaction'}

if method = POST(i.e. when the query is submitted.)
	resp = {'message': 'SUCCESS: The user purchased the stock.'}


2:        **URLS(main/urls.py):** '/sellstocks/(?P<id>\d+)$' (i.e. /sellstocks/stock_id)

**VIEW(main/views.py):** SellStocks     
					
**json data:** in case the user is not authenticated:	resp = {'error':'The user is not registered yet.'}

if method = POST and current_stock is None:
												resp = {'error': 'The user does not have any stocks to sell'}   

or if method = POST and no. of untits from user is less than the number_of_stocks:
												resp = {'message': 'SUCCESS: The user sold the stock.'}

and if method = POST and no. of units from user is greater than the number_of_stocks:
												resp = {'message': 'FAILURE: The user does not have enough stocks to sell.'} 


3:    **URLS(main/urls.py):** '/userprimarydetails'

**VIEW(main/views.py):** UserPrimaryDetails

Variables to be sent through POST request: 'email' & 'key'

Returned data contains a list with user details like this:

        {'username': current_user.name ,
        'email-id': current_user.mail_id ,
        'user_balance': current_user.balance ,}
	
If the key doesn't match then: {'error':'The user is not registered yet.'}


4:   **URLS(main/urls.py):** '/stocksprimarydata'

**VIEW(main/views.py):** StocksPrimaryData

Variables to be sent through POST request: 'key'

Returned data contains a list with all stock's details like this:

             {"id" : this_stock.id,
            "name" : this_stock.product_name,
            "price" : this_stock.stock_price,
			"market_type" : this_stock.market_type,
            "price_trend" : this_stock.price_trend}
	
If the key doesn't match then: {'error':'The user is not registered yet.'}

4:   **URLS(main/urls.py):** '/userstockdetails'

**VIEW(main/views.py):** UserStockDetails

Variables to be sent through POST request: 'key' & 'mail'

Returned data contains a list with all stocks info purchased by the given user, like this:

        {"name" : current_stock.product_name,
        "num" : this_stock.number_of_stocks,
        "price" : current_stock.stock_price,
        "price_trend" : this_stock.price_trend}
	
If the key doesn't match then: {'error':'The user is not registered yet.'}

5: **URLS(main/urls.py):** '^stockdata/(?P<id>\d+' i.e, '/stockdata/id'

**VIEW(main/views.py):** StockData

Variables to be sent through POST request: 'key' & 'mail'

Returned data contains info of the stock corresponding to the id, like this:

        {"name" : current_stock.product_name,
        "num" : this_stock.number_of_stocks,
        "price" : current_stock.stock_price,
        "price_trend" : this_stock.price_trend}

If the key doesn't match then: {'error':'The user is not registered yet.'}

6: **URLS(main/urls.py):** '/lbdata' 

**VIEW(main/views.py):** LBdata

Variables to be sent through POST request: 'key' & 'mail'

Returned data contains a list of top 10 users, followed by rank  of current user. Like this:

	[{"name": this_user.name, "net_worth": this_user.net_worth}, {"Rank of current_user": my_pos}]

If the key doesn't match then: {'error':'The user is not registered yet.'}

	
7: **URLS(main/urls.py):** '/getnewspost'

**VIEW(main/views.py):** getnewspost

Variables to be sent through POST request: 'key'  

	If the key doesn't match then: {'error':'The user is not registered yet.'}

Returned data is a list of details of news

            'time_of_post':this_post.time_of_post,
            'Stock':this_post.corresponding_stock.product_name,
            'post_text':this_post.post_text,