from django.shortcuts import render
import requests
import pandas as pd
# Create your views here.

def index(request):
    baseurl = 'https://api.covid19india.org/data.json'
    para = {}
    data = requests.get(baseurl).json()
    df = pd.DataFrame(data['cases_time_series'])
    date = df['date'].iloc[-1]
    dailyconfirmed = df['dailyconfirmed'].iloc[-1]
    dailydeceased = df['dailydeceased'].iloc[-1]
    dailyrecovered = df['dailyrecovered'].iloc[-1]
    totalconfirmed = df['totalconfirmed'].iloc[-1]
    totaldeceased = df['totaldeceased'].iloc[-1]
    totalrecovered = df['totalrecovered'].iloc[-1]
    total = [('date', date), ("today's confirmed:",dailyconfirmed), ("today's deceased:",dailydeceased), ("today's recovered:",dailyrecovered), ("total confirmed:",totalconfirmed), ('total deceased:',totaldeceased), ('total recovered:',totalrecovered)]
    #print(df)
    return render(request, 'tracker/index.html',{
        "total": total
    })
