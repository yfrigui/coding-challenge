from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Link
from .forms import AddLinkForm
from .forms import EditLinkForm

# Create your views here.
def index(request):
	links = Link.objects.order_by('-clicks')
	context = {'links': links,}
	return render(request, 'links/index.html', context)

def add_link(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = AddLinkForm(request.POST)
		# check whether it's valid:
		#print("form: " + form)
		if form.is_valid():
			link_title = form.cleaned_data['link_input']
			link = Link(title=link_title)
			try:
				link.save()
			except: #go back if user tries to add a link that already exists
				links = Link.objects.order_by('-clicks')
				return render(request, 'links/index.html', {'links':links})
			links = Link.objects.order_by('-clicks')
			return render(request, 'links/index.html', {'links':links})
            #return HttpResponseRedirect('/thanks/')
    # if a GET (or any other method) we'll create a blank form
	else:
		form = AddLinkForm()
	links = Link.objects.order_by('-clicks')
	return render(request, 'links/index.html', {'links': links})	

def click(request):
	link_title = request.GET.get('link')
	try:
		link = Link.objects.get(title=link_title)
	except Link.DoesNotExist:
		raise Http404("Link does not exist")
	link.visit() #increments link count
	return HttpResponse("You will be redirected to %s." % link_title)

def delete_link(request):
	link_title = request.GET.get('link')
	try:
		link = Link.objects.get(title=link_title)
	except Link.DoesNotExist:
		raise Http404("Link does not exist")
	link.delete()
	links = Link.objects.order_by('-clicks')
	context = {'links': links,}
	return render(request, 'links/index.html', context)

def begin_edit_link(request):
	link_title = request.GET.get('link')
	try:
		link = Link.objects.get(title=link_title)
	except Link.DoesNotExist:
		raise Http404("Link does not exist")
	context = {'link': link}
	return render(request, 'links/edit_link.html', context)

def finish_edit_link(request):
	link_title = request.GET.get('link')
	try:
		link = Link.objects.get(title=link_title)
	except Link.DoesNotExist:
		raise Http404("Link does not exist")
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = EditLinkForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			new_link_title = form.cleaned_data['new_link_title']
			link.title = new_link_title
			try:
				link.save()
			except: #return if a link already exists with this name
				links = Link.objects.order_by('-clicks')
				return render(request, 'links/index.html', {'links':links})
			links = Link.objects.order_by('-clicks')
			return render(request, 'links/index.html', {'links':links})
	links = Link.objects.order_by('-clicks')
	return render(request, 'links/index.html', {'links': links})	
