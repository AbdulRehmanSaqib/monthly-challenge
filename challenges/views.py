from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.loader import render_to_string

monthly_challenges = {
    "january" : "Eat meat for entire month(LOL)",
    "february" : "HELLO",
    "march" :"HELLO",
    "april" :"HELLO",
    "may" :"HELLO",
    "june" :"HELLO",
    "july" : "HELLO",
    "august" : "HELLO",
    "september" : "HELLO",
    "october" :"HELLO",
    "november" : "HELLO",
    "december" : None,
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months" : months,
    })

    for month in months:
        capitalized_month= month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month>len(months):
        return HttpResponseNotFound("<h1>Invalid</h1>")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) 
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text" : challenge_text,
            "month_name" : month
        })
        
    except:
        raise Http404()

   