from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Tweet
from django.template import loader



def index(request):
    return render(request,'index.html')

def view2(request):
    return render(request,'tubuyaki_list.html')

def post(request):
    message = request.POST['message']
    name = request.POST['name']
    tweet = Tweet(message=message,  name=name)
    tweet.save()
    return HttpResponseRedirect(reverse('tubuyakis:view'))

def view(request):
    tweet_list = Tweet.objects.all()
    context = {'tweet_list':tweet_list}
    template = loader.get_template('view.html')
    return HttpResponse(template.render(context,request))
