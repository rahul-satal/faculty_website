from django.http import HttpResponse
from django.shortcuts import render
from website.models import *

name = "shaligram.prajapat@gmail.com"

def pbas_index(request):
	return render(request, 'pbas/index.html')

def login(request):
	user_list = Userinfo.objects.all()
	context = {'user_list':user_list}
	return render(request, 'pbas/index.html', context)




	'''
	if request.method == 'GET':
		return render(request, 'pbas/index.html')
	else:
		'' -----fetching the data from the user and saving it in database---- ''
		data = contactus(user_id= request.POST['user_id'], pwd= request.POST['pwd'])
		data.save()
		return HttpResponseRedirect('#')	
'''
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



