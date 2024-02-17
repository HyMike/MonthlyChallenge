from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse



months_dict = {
    "January": "January is named after Janus, the Roman god of beginnings, transitions, and endings. It is often associated with New Year's resolutions and is the coldest month in the Northern Hemisphere.",
    "February": "February is the only month that can pass without a full moon. It is the shortest month of the year and is associated with Valentine's Day and Black History Month.",
    "March": "March is named after Mars, the Roman god of war. It is the beginning of spring in the Northern Hemisphere and is associated with the March equinox. March is also known for St. Patrick's Day.",
    "April": "April's name is derived from the Latin word 'aperire,' which means 'to open,' reflecting the opening of flowers and trees in spring. It is known for April Fools' Day and Earth Day.",
    "May": "May is named after Maia, the Roman goddess of spring and growth. It is associated with May Day, Mother's Day, and Memorial Day in the United States.",
    "June": "June is named after Juno, the Roman goddess of marriage and the well-being of women. It is the beginning of summer in the Northern Hemisphere and is associated with weddings and Father's Day.",
    "July": "July is named after Julius Caesar, the Roman general and statesman who was born in this month. It is the hottest month in the Northern Hemisphere and is associated with Independence Day in the United States.",
    "August": "August was originally named Sextilis in Latin, as it was the sixth month of the Roman calendar. It was later renamed in honor of Augustus Caesar. August is associated with the end of summer and back-to-school season.",
    "September": "September's name comes from the Latin word 'septem,' meaning 'seven,' as it was the seventh month of the Roman calendar. It marks the beginning of autumn in the Northern Hemisphere and is associated with Labor Day.",
    "October": "October's name comes from the Latin word 'octo,' meaning 'eight,' as it was the eighth month of the Roman calendar. It is known for Halloween and Breast Cancer Awareness Month.",
    "November": "November's name comes from the Latin word 'novem,' meaning 'nine,' as it was the ninth month of the Roman calendar. It is associated with Thanksgiving in the United States and Movember, a month-long event involving the growing of mustaches to raise awareness of men's health issues.",
    "December": "December's name comes from the Latin word 'decem,' meaning 'ten,' as it was the tenth month of the Roman calendar. It is known for Christmas, Hanukkah, and New Year's Eve celebrations."
}

# Create your views here.
# def index(request):
#     return HttpResponse("This works!")

# def february(request):
#     return HttpResponse('this is valentine month!')
def monthlyInt(request, months):
    if months > 12 or months < 0:
        return HttpResponseNotFound("This is not a valid month!")
    month_list = list(months_dict.keys())
    month_url = month_list[months - 1]
    reverse_url = reverse("months_path", args=[month_url])
    return HttpResponseRedirect(reverse_url)

    
def monthly(request, months):
    months = months.capitalize()
    try: 
        challenge_txt = months_dict[months]
    except:
        return HttpResponseNotFound("There is not a valid month!")
    return HttpResponse(challenge_txt) 
    
def index(request): 
    month_list = list(months_dict.keys())
    html_months = ""
    for month in month_list:
        html_months += f"<li>{month}</li>"

    return HttpResponse(html_months)

