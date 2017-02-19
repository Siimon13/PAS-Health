from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

from .forms import UserForm, UpdateForm
from .models import User

import numpy as np
import random
# Create your views here.

weight = []

@csrf_exempt 
def index(request):
    global weight
    weight = []
    # return HttpResponse('Hello from Python!')
    train_response()
    for i in weight:
        print(i)
    return render(request, 'index.html')


def render_results(request, message=""): 
    global weight
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
        print(u.current_diet)

    recommended_diet = test_response(user)
    print(recommended_diet)

    print(weight)

    context  = {'user' : user , 'message': message, 'recommended_diet':recommended_diet}
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
            

    return redirect("/")
    
def calculateOutput(threshold1, threshold2, threshold3, threshold4, threshold5, inputdic = []):
	global weight
	result = 0.0
        print(inputdic)
	for i,j in zip(weight,inputdic):
            print i
            print j
            result += i * float(j) 

	if(result <= threshold1):
		return 0
	elif(result <= threshold2):
		return 0.2
	elif(result <= threshold3):
		return 0.4
	elif(result <= threshold4):
		return 0.6
	elif(result <= threshold5):
		return 0.8
	elif(result > threshold5):
		return 1

def train_response():
	global weight
	output = []
	uall = User.objects.all()
	inputdic = []
	for u in uall:
   		life = 0
   		gen = 0
   		if(u.lifestyle == "Sedentary"):
   			life = 1
   		elif(u.lifestyle == "Lightly active"):
   			life = 2
   		elif(u.lifestyle == "Moderately active"):
   			life = 3
   		elif(u.lifestyle == "Very active"):
   			life = 4
   		elif(u.lifestyle == "Extremely active"):
   			life = 5
   		if(u.gender == "Male"):
   			gen = 1
   		elif(u.gender == "Female"):
   			gen = 2
                if(u.current_diet == "Paleo"):
                    output.append(0)
                elif(u.current_diet == "Low-Carb"):
                    output.append(0.2)
                elif(u.current_diet == "Ultra Low-Fat"):
                    output.append(0.4)
                elif(u.current_diet == "Atkins"):
                    output.append(0.6)
                elif(u.current_diet == "Zone Diet"):
                    output.append(0.8)
                elif(u.current_diet == "Fasting"):
                    output.append(1)
                inputdic.append([u.age, u.current_weight, life, u.current_height, gen])

	for i in range(0, 5):
		weight.append(random.random())

	for x in range(0, 1000):
		totalError = 0
		for i in range(len(output)):
                    out = calculateOutput(0.01, 0.03, 0.05, 0.08, 0.1, inputdic[i])
                    error = output[i] - out
                    totalError += error
                    for r, y in zip(weight, inputdic[i]):
    			r += 0.1 * error * y

def test_response(user):
	global weight
	life = 0
   	gen = 0
        if(user["lifestyle"] == "Sedentary"): 
            life = 1
        elif(user["lifestyle"] == "Lightly active"): 
            life = 2
        elif(user["lifestyle"] == "Moderately active"): 
            life = 3
        elif(user["lifestyle"] == "Very active"): 
            life = 4
        elif(user["lifestyle"] == "Extremely active"): 
            life = 5

        if(user["gender"] == "Male"): 
            gen = 1
        elif(user["gender"] == "Female"): 
            gen = 2
        inputdic = [user["age"], user["current_weight"], life, user["current_height"], gen]
        out = calculateOutput(0.01, 0.03, 0.05, 0.08, 0.1, inputdic)

        if(out == 0): 
            return "Paleo"
        elif(out == 0.2): 
            return "Low-Carb"
        elif(out == 0.4): 
            return "Ultra Low-Fat"
        elif(out == 0.6):
            return "Atkins"
        elif(out == 0.8):
            return "Zone Diet"
        elif(out == 1):
            return "Fasting"
        else:
            return "Low-Carb"
