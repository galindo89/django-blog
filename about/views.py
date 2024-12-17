from django.shortcuts import render,get_list_or_404,redirect
from django.views import generic
from django.contrib import messages
from .models import About, CollaborateRequest
from .forms import CollaborationForm


# Create your views here.
def about_me(request):
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborationForm()
    
    if request.method == "POST":
        print ("Received POST request")
        collaborate_form = CollaborationForm(data=request.POST)
        if collaborate_form.is_valid():
           collaborate_request=collaborate_form.save(commit=False)
           collaborate_request.save()            
           messages.add_message(
                request, messages.SUCCESS,
                'Collaboration Request submitted successfully'
    )
           return redirect("about")
    

    collaborate_request = CollaborationForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form
        },
    )
    
