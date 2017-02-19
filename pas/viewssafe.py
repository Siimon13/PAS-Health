from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import UserForm, UpdateForm
from .models import User

import numpy as np
import random
# Create your views here.

@csrf_exempt 
def index(request):
    # return HttpResponse('Hello from Python!')
    train_response()
    return render(request, 'index.html')


def render_results(request, message=""): 

    if request.method == 'GET':
        form = UserForm(request.GET)
        
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
            user["current_height"] = form.cleaned_data["current_height"]
            
            user["hashid"] = str(len(user["first_name"] + user["last_name"] + user["age"] + user["ethnicity"])) + str(user["first_name"] + user["gender"])

            query = User.objects.filter(hashid = user["hashid"])

            if len(query) == 0: #Adds user
                u = User(** user)

                u.save()
            else: #Updates user weight
                u = query[0]
                u.current_weight = user["current_weight"]
                u.goal_weight = user["goal_weight"]
                u.current_height = user["current_height"]
                user["current_diet"] = u.current_diet

            print (query)

    uall = User.objects.all()
    for u in uall:
    	print(u.first_name)
    	print(u.last_name)
    	print(u.ethnicity)
    	print(u.age)
    	print(u.lifestyle)
    	print(u.gender)
    	print(u.current_weight)
    	print(u.goal_weight)
    	print(u.current_height)

    context  = {'user' : user , 'message': message}
    template = 'results.html'

    return render(request, template, context)

def update_results(request, message=""): 
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        print (request.POST)

        if form.is_valid():
            u = User.objects.filter(hashid = form.cleaned_data["hashid"])
            u = u[0]

            if form.cleaned_data["options"] != "null":
                u.current_diet = form.cleaned_data["options"]

            u.save()
            print ("Valid")
            print (form.cleaned_data)
            

    return index(request)
    
