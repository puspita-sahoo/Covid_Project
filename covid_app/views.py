import json
from django.shortcuts import render
import requests


def home(request):
    res = requests.get("https://api.covid19api.com/total/country/india")
    date_wise = res.json()
    return render(request, "home.html", {'date_wise': date_wise})


def graph(request, days=365, charttype = 'bar'):

    res = requests.get("https://api.covid19api.com/total/country/india")
    data = res.json()
    print(days, charttype)
    # if days==None:
    # days = 365
    data_days = data[-days:]  # filters last 30 days data

    chart_x_dates = []
    chart_y_Confirmed = []
    chart_y_Deaths = []
    chart_y_Recovered = []

    for date_data in data_days:
        # print("D: ", )
        chart_x_dates.append(date_data['Date'])
        chart_y_Confirmed.append(date_data["Confirmed"])
        chart_y_Deaths.append(date_data["Deaths"])
        chart_y_Recovered.append(date_data["Recovered"])

    covid_data = {
        "dates": chart_x_dates,
        "confirmed": chart_y_Confirmed,
        "deaths": chart_y_Deaths,
        "recoveres": chart_y_Recovered,   
    }
    print(charttype)
    return render(request, "graph.html",
                  {"covid_data": json.dumps(covid_data), "chart_type": charttype})
