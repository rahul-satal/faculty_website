from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from website.models import *

name = "shaligram.prajapat@gmail.com"

def login(request):
	if request.method == 'GET':
		return render(request, 'pbas/index.html')
	if request.method == 'POST':
		current_user_object = Userinfo.objects.all().filter(user_id = request.POST['user_id'])
		if current_user_object:
			if current_user_object[0].pwd == request.POST['pwd']:
				#return HttpResponse('login')
				return render(request, 'pbas/yearModal.html')
				#return HttpResponseRedirect(request, 'pbas/yearModal.html')
			 

def signup_action(request):
	if request.POST['userID'] and request.POST['regPass'] and request.POST['confirmPass']:
		''' -----fetching the data from the user and saving it in database---- '''
		data = Userinfo(user_id= request.POST['userID'], pwd = request.POST['regPass'])
		data.save()
		return render(request, 'pbas/index.html')

			 
#return render_to_response('fileupload/upload.html', {'form': c['UploadFileForm']},  RequestContext(request))
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



