from copy import copy, deepcopy
from itertools import permutations
from django.views.generic import TemplateView
from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .models import Section, Course, Departemant



class AboutPageView(TemplateView):
    template_name = "about.html"

def HomePage(request):
    departemants = []
    for item in Departemant.objects.all():
        d = {}
        d["name"] = item.name
        d["courses"] = item.courses.filter(status=True).order_by("-credits")

        departemants.append(d)
    notice = request.session.get("notice")
    return render(request, "home.html", {
        "departemants" : departemants,
        "notice" : notice
    })

def Suggest(request):

    "Here is your scheduling algorithm"

    return render(request, "suggest.html", {
        "tables": tables,
        "search" : search,
        "message" : message
    })
