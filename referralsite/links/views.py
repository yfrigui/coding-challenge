from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Grow the web with referrals!")

def click(request):
	link_title = request.GET.get('link')
	return HttpResponse("You will be redirected to %s." % link_title)
