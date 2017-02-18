from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import UserForm
# Create your views here.

@csrf_exempt 
def index(request):
    # return HttpResponse('Hello from Python!')
    if request.method == 'POST':
        form = UserForm(request.POST)
        
        if form.is_valid():
            user = {}
            user["first_name"] = form.cleaned_data["first_name"]
            user["last_name"] = form.cleaned_data["last_name"]
            user["ethnicity"] = form.cleaned_data["ethnicity"]
            user["age"] = form.cleaned_data["age"]
            user["lifestyle"] = form.cleaned_data["lifestyle"]
            user["gender"] = form.cleaned_data["gender"]
            user["current_weight"] = form.cleaned_data["current_weight"]
            user["goal_weight"] = form.cleaned_data["goal_weight"]
            

            print user
            return renderresults(request, user)
            
    return render(request, 'index.html')


def renderresults(request, user=[], message=""):
    context  = {'user' : user , 'message': message}
    template = 'results.html' 

    return render(request, template, context)
