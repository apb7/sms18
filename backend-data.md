## This file consists of the list of urls on our project along with the JSON response that is being sent corresponding to that url.

                    
1:       **URLS(main/urls.py):**'/buystocks/(?P<id>\d+)$' (i.e. /buystocks/stock id)

**VIEW(main/views.py):** BuyStocks
					
**json data:** in case the user is not authenticated:	resp = {'error':'The user is not registered yet.'}

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

