from django.http import HttpResponse
from django.shortcuts import render
from website.models import *

name = "shaligram.prajapat@gmail.com"


def login(request):
	#user_list = Userinfo.objects.all()
	if request.method == 'GET':
		return render(request, 'pbas/index.html')
	if request.method == 'POST':
		current_user_object = Userinfo.objects.all().filter(user_id = request.POST['user_id'])
		if current_user_object:
			if current_user_object[0].pwd == request.POST['pwd']:
				return render(request, 'pbas/yearModal.html')
			 
def home_page(request):
	return render(request, 'pbas/home.html')

def myfriends(request):
	myfriends_list = Myfriend.objects.all()
	context = {'myfriends_list':myfriends_list}
	return render(request, 'website/myfriends.html', context)

def myfriends(request):
	myfriends_list = Myfriend.objects.all()
	context = {'myfriends_list':myfriends_list}
	return render(request, 'website/myfriends.html', context)

def myfriends(request):
	myfriends_list = Myfriend.objects.all()
	context = {'myfriends_list':myfriends_list}
	return render(request, 'website/myfriends.html', context)

def myfriends(request):
	myfriends_list = Myfriend.objects.all()
	context = {'myfriends_list':myfriends_list}
	return render(request, 'website/myfriends.html', context)

def myfriends(request):
	myfriends_list = Myfriend.objects.all()
	context = {'myfriends_list':myfriends_list}
	return render(request, 'website/myfriends.html', context)
	
def myfriends(request):
	myfriends_list = Myfriend.objects.all()
	context = {'myfriends_list':myfriends_list}
	return render(request, 'website/myfriends.html', context)								   


def myfriends(request):
	myfriends_list = Myfriend.objects.all()
	context = {'myfriends_list':myfriends_list}
	return render(request, 'website/myfriends.html', context)



