import csv
import datetime
import json
import random

with open('Day1.csv',"r") as csvfile:
    mycsv=csv.reader(csvfile,delimiter=',', quotechar='"')
    timelist=[]
    #stocks=mycsv[0]
    boo=True
    matrix=[]
    for row in mycsv:
        matrix.append(row)
        try:
            timelist.append(tuple(map(int,row[1].split(":"))))
        except:
            pass
    #print(matrix)
    stocks=matrix[0]
    #print(timelist)
    stocks=stocks[2:-1]
    #print(stocks)
    timedifflist=[]
    for i in range(len(timelist)-1):
        diff=(timelist[i+1][0]-timelist[i][0],timelist[i+1][1]-timelist[i][1])
        timediff=diff[0]*60+diff[1]
        timedifflist.append(timediff)
    
    #print(timedifflist)

    output_dictionary={}
    koffset=2
    ioffset=2
    currency=19
    for k in range(len(stocks)):
        stock_price=[]
        for i in range(len(timedifflist)):
            #print("for stock"+stocks[k])
            price=int(matrix[i+ioffset][k+koffset])
            price1=int(matrix[i+ioffset+1][k+koffset])
            delta=(price1-price)
            #print("price is"+price.__str__())
            for j in range(timedifflist[i]):
                try:
                    a=random.randrange(0,price//100)
                    stock_price.append(price+int(a))
                except:
                    stock_price.append(price)
        stock_price.append(int(matrix[i+ioffset+1][k+koffset]))
        #print(stock_price)
        #print(len(stock_price))
        output_dictionary[stocks[k]]=stock_price
    print(json.dumps(output_dictionary,indent=4,sort_keys=True))