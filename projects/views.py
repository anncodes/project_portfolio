from django.shortcuts import render, redirect
from projects.models import Project
from django.core.mail import EmailMessage
from django.http import HttpResponse
from projects.forms import ContactForm
from django.conf import settings


def project_index(request):
	projects = Project.objects.all()

	form = ContactForm()
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			sender_name = form.cleaned_data["sender_name"]
			from_email = form.cleaned_data["from_email"]
			message = form.cleaned_data["message"]
		
		EmailMessage(
				'Contact form submission from {}'.format(sender_name), 
				message,
				 'form-response@afullstack.ch',
				  ["annm.gepulle@gmail.com"],
				  [],
				  reply_to=[from_email]
				  ).send()
		
		return redirect("success/")

	context = {
	    'projects': projects,
		'form':form
	}
	return render(request, 'project_index.html', context)


def project_detail(request, pk):
	project = Project.objects.get(pk=pk)
	context = {
		'project': project
	}
	return render(request, 'project_detail.html', context)


		

def successView(request):
	return HttpResponse("Success! Thank you for your message.")