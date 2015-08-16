from django.http import HttpResponse
from django.shortcuts import render
from .models import *



def index(request):
	gen_info1 = GenInfo.objects.all()
	teacher_list = Myteacher.objects.all()
	context = {'teacher_list':teacher_list,'gen_info1':gen_info1}
	return render(request, 'website/index.html', context)

def index(request):
	profile = Profile.objects.all()
	context = {'profile':profile}
	return render(request, 'website/header.html', context)
