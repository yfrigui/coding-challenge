from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Link

# Create your views here.
def index(request):
	links = Link.objects.order_by('-clicks')
	context = {'links': links,}
	return render(request, 'links/index.html', context)

def click(request):
	link_title = request.GET.get('link')
	try:
		link = Link.objects.get(title=link_title)
	except Link.DoesNotExist:
		raise Http404("Link does not exist")
	link.visit()
	return HttpResponse("You will be redirected to %s." % link_title)
