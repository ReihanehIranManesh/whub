from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from .models import MY_CHOICES, Category, Country, Do, Dont, Comment, Review
from django.db.models import Q

import datetime

def index(request):
    if not request.user.is_authenticated:
        return render(request, "whub/login.html", {"message": None})
    context = {
        "user": request.user,
        "reviews" : Review.objects.all().order_by('-votes'),
        "dos" : Do.objects.all(),
        "donts" : Dont.objects.all(),
        "comments" : Comment.objects.all(),
    }
    return render(request, "whub/home.html", context)


def user(request):
    if not request.user.is_authenticated:
        return render(request, "whub/login.html", {"message": None})
    context = {
        "user": request.user,
        "reviews" : Review.objects.all().order_by('-votes'),
        "dos" : Do.objects.all(),
        "donts" : Dont.objects.all(),
        "comments" : Comment.objects.all(),
    }
    return render(request, "whub/user.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "whub/login.html", {"message": "Your username and password do not match. Try again."})

def logout_view(request):
    logout(request)
    return render(request, "whub/login.html", {"message": "You just logged out."})

def register(response):
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("index"))
	else:
		form = RegisterForm()

	return render(response, "whub/register.html", {"form":form})

def review(request):
    if not request.user.is_authenticated:
        return render(request, "whub/login.html", {"message": None})
    context = {
        "user": request.user,
        "categories" : MY_CHOICES,
        "countries" : Country.objects.all()
    }
    return render(request, "whub/review.html", context)

def do(request):
    if request.method == 'GET':
        r = Review.objects.get(pk=Review.objects.all().count())
        d = Do(text=request.GET['text'], review= r)
        d.save()
        return HttpResponse('success')
    else:
        return HttpResponse("unsuccesful")

def dont(request):
    if request.method == 'GET':
        r = Review.objects.get(pk=Review.objects.all().count())
        d = Dont(text=request.GET['text'], review= r)
        d.save()
        return HttpResponse('success')
    else:
        return HttpResponse("unsuccesful")

def comment(request):
    if request.method == 'GET':
        array = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
        now = datetime.datetime.now()
        min = str(now.minute)
        if len(min) == 1:
            min = "0" + min
        r = Review.objects.get(pk=request.GET['rid'])
        c = Comment(text=request.GET['text'], cdatetime= array[now.month - 1] + " " + str(now.day) + " , " + str(now.year) + " " + str(now.hour) + ":" + min, review=r, user= request.user)
        c.save()
        return HttpResponse('success')
    else:
        return HttpResponse("unsuccesful")

def reviewcard(request):
    if request.method == 'GET':
        c = Category(name=request.GET['categories'])
        c.save()
        array = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
        now = datetime.datetime.now()
        min = str(now.minute)
        if len(min) == 1:
            min = "0" + min
        nowtime = array[now.month - 1] + " " + str(now.day) + " , " + str(now.year) + " " + str(now.hour) + ":" + min
        us = request.user
        count = Country.objects.get(pk=request.GET['country'])
        r = Review(user = us, category = c, title=request.GET['title'], text=request.GET['text'], image= request.GET['image'], cdatetime= nowtime , city=request.GET['city'], country= count, votes= request.GET['votes'])
        r.save()
        return HttpResponse('success')
    else:
        return HttpResponse("unsuccesful")

def upvote(request):
    if request.method == 'GET':
        review = Review.objects.get(pk=request.GET['revid'])
        review.votes = review.votes + 1
        review.save()
        return HttpResponse('success')
    else:
        return HttpResponse("unsuccesful")

def downvote(request):
    if request.method == 'GET':
        review = Review.objects.get(pk=request.GET['revid'])
        review.votes = review.votes - 1
        review.save()
        return HttpResponse('success')
    else:
        return HttpResponse("unsuccesful")

def search(request):
    if request.is_ajax():
        key = request.GET['key']
        array = ["Place of interest", "Transportation", "Food", "Events", "Culture", "Residency"]
        lowerkey = key.lower()
        temp = lowerkey[0].upper() + lowerkey[1:len(lowerkey)]
        value = ""
        for i in range(len(array)):
            if lowerkey in array[i] or temp == array[i]:
                value = value + str(i + 1) + ","

        if value != "" :
            review = Review.objects.filter(Q(title__contains=key) | Q(text__contains=key) | Q(city__contains=key) | Q(country__name__contains=key) | Q(category__name__contains=value[0:len(value) - 1])).order_by('-votes')
        else :
            review = Review.objects.filter(Q(title__contains=key) | Q(text__contains=key) | Q(city__contains=key) | Q(country__name__contains=key)).order_by('-votes')

        context = {
        "user": request.user,
        "reviews" : review,
        "dos" : Do.objects.all(),
        "donts" : Dont.objects.all(),
        "comments" : Comment.objects.all(),
        }
        return render(request, "whub/home.html", context)



def searchuser(request):
    if request.is_ajax():
        key = request.GET['key']
        array = ["Place of interest", "Transportation", "Food", "Events", "Culture", "Residency"]
        lowerkey = key.lower()
        temp = lowerkey[0].upper() + lowerkey[1:len(lowerkey)]
        value = ""
        for i in range(len(array)):
            if lowerkey in array[i] or temp == array[i]:
                value = value + str(i + 1) + ","

        if value != "" :
            review = Review.objects.filter(Q(title__contains=key) | Q(text__contains=key) | Q(city__contains=key) | Q(country__name__contains=key) | Q(category__name__contains=value[0:len(value) - 1])).order_by('-votes')
        else :
            review = Review.objects.filter(Q(title__contains=key) | Q(text__contains=key) | Q(city__contains=key) | Q(country__name__contains=key)).order_by('-votes')

        context = {
        "user": request.user,
        "reviews" : review,
        "dos" : Do.objects.all(),
        "donts" : Dont.objects.all(),
        "comments" : Comment.objects.all(),
        }
        return render(request, "whub/user.html", context)
