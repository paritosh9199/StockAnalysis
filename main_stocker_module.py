from stocker import Stocker 
import os
import datetime
from datetime import date

import csv 
import sys
 


#long process here
import time
import sys
def main():
    while True:
        print("========================================================")
        print("select one of the following choices \n")
        print("========================================================")
        print("1. plot the stock history of a certain company")
        print("2. create a prediction model of stocks")
        print("3. See major changes that happened in a stock over a period of time")
        print("4. Predict the value of stock over a period of time for a company")
        print("5. Predict the value of stock anytime in the future")
        print("6. Check the Company codes")
        print("========================================================")

        i = int(input())

        if i==1:
            stockPlotter()

        elif i==2:
            stockPrediction()

        elif i==3:
            stockChangePoint()

        elif i==4:
            stockValueOverTime()
        
        elif i==5:
            stockValueInFuture()

        elif i==6:
            readCsv()
        
        else:
            print("wrong input")
            #function callback

def stockPlotter():
    print("enter the code for the company you want to check the stocks of:")
    companyCode = input()
    st = Stocker(companyCode)
    st.plot_stock()

def stockPrediction():
    print("enter the code for the company you want to check the predictions of:")
    companyCode = input()
    st = Stocker(companyCode)
    st.create_prophet_model()

def stockChangePoint():
    print("enter the code for the company you want to check the predictions of:")
    companyCode = input()
    st = Stocker(companyCode)
    st.changepoint_date_analysis()

def stockValueOverTime():
    print("enter the code for the company you want to check the predictions of:")
    companyCode = input()
    print("Enter the start Date(SYNTAX: YYYY-MM-DD)")
    start_date = input(datetime.date)
    print("Enter the end Date(SYNTAX: YYYY-MM-DD)")
    end_date = input(datetime.date)
    print("Enter number of shares")
    nshares = int(input())
    st = Stocker(companyCode)
    st.buy_and_hold(start_date,end_date,nshares)

def stockValueInFuture():
    print("enter the code for the company you want to check the predictions of:")
    companyCode = input()
    print("Enter the No. of Days you want to predict the stocks for:")
    n = int(input())
    st = Stocker(companyCode)
    st.create_prophet_model(n)

def readCsv():
    f = open(sys.argv[1],  'r')
    reader1 = csv.reader(f)
    for row in reader1:
        if (row[1]!=""):
            print (row[0],"======",row[1])
    f.close()


main()



