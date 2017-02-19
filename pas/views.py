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
age_max = 0
age_min = 0
weight_min = 0
weight_max = 0
height_min = 0
height_max = 0
inputdic = []

@csrf_exempt 
def index(request):
    global weight
    global inputdic
    inputdic = []
    weight = []

    train_response()
    # return HttpResponse('Hello from Python!')
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
	for i,j in zip(weight,inputdic):
            result += i * float(j) 

        print(result)
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

def normalize(inputsdic = []):
    global age_min, age_max, weight_min, weight_max, height_min, height_max
    age_min = inputsdic[0][1]
    age_max = inputsdic[0][1]
    weight_min = inputsdic[0][2]
    weight_max = inputsdic[0][2]
    height_min = inputsdic[0][4]
    height_max = inputsdic[0][4]

    for i in range(1,len(inputsdic)):
        if(inputsdic[i][1] < age_min):
            age_min = inputsdic[i][1]
        elif(inputsdic[i][1] > age_max):
            age_max = inputsdic[i][1]
        
        if(inputsdic[i][2] < weight_min):
            weight_min = inputsdic[i][2]
        elif(inputsdic[i][2] > weight_max):
            weight_max = inputsdic[i][2]
        
        if(inputsdic[i][4] < height_min):
            height_min = inputsdic[i][4]
        elif(inputsdic[i][4] > height_max):
            height_max = inputsdic[i][4]

    for i in range(len(inputsdic)):
        inputsdic[i][1] = (inputsdic[i][1] - age_min)/(age_max - age_min)
        inputsdic[i][2] = (inputsdic[i][2] - weight_min)/(weight_max - weight_min)
        inputsdic[i][4] = (inputsdic[i][4] - height_min)/(height_max - height_min)

def train_response():
	global weight
	output = []
	uall = User.objects.all()
        global inputdic
	for u in uall:
   		life = 0
   		gen = 0
                ethnicity = 0
   		if(u.lifestyle == "Sedentary"):
   			life = 0.2
   		elif(u.lifestyle == "Lightly active"):
   			life = 0.4
   		elif(u.lifestyle == "Moderately active"):
   			life = 0.6
   		elif(u.lifestyle == "Very active"):
   			life = 0.8
   		elif(u.lifestyle == "Extremely active"):
   			life = 1.0
   		if(u.gender == "Male"):
   			gen = 1
   		elif(u.gender == "Female"):
   			gen = 0.5

                if(u.ethnicity == "Hispanic or Latino"):
                    ethnicity = 0.15
                elif(u.ethnicity == "White American"):
                    ethnicity = 0.3
                elif(u.ethnicity == "Africans"):
                    ethnicity = 0.45
                elif(u.ethnicity == "Asian Americans"):
                    ethnicity = 0.6
                elif(u.ethnicity == "Native Americans"):
                    ethnicity = 0.75
                elif(u.ethnicity == "Middle Easterners"):                
                    ethnicity = 1.0
                else:
                    ethnicity = 1

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
                inputdic.append([ethnicity, u.age, u.current_weight, life, u.current_height, gen])

        normalize(inputdic)
        #for i in inputdic:
            #print i
	for i in range(0, 6):
		weight.append(random.random())
        #print(weight)

	for x in range(0, 1000):
		totalError = 0
		for i in range(len(output)):
                    out = calculateOutput(-0.4,-0.1 , 0, 0.15, 0.4, inputdic[i])
                    print(out)
                    error = output[i] - out
                    totalError += error
                    for r in range(len(weight)):
                        weight[r] = weight[r] + 0.3 * error * inputdic[i][r] 

def test_response(user):
	global weight
        global inputdic
        global age_min
        global age_max
        global weight_min
        global weight_max
        global height_min
        global height_max
        life = 0
        gen = 0
        ethnicity = 0
        if(user["lifestyle"] == "Sedentary"):
            life = 0.2
        elif(user["lifestyle"] == "Lightly active"):
            life = 0.4
        elif(user["lifestyle"] == "Moderately active"):
            life = 0.6
        elif(user["lifestyle"] == "Very active"):
            life = 0.8
        elif(user["lifestyle"] == "Extremely active"):
            life = 1.0
        if(user["gender"] == "Male"):
            gen = 1
        elif(user["gender"] == "Female"):
            gen = 0.5

        if(user["ethnicity"] == "Hispanic or Latino"):
            ethnicity = 0.15
        elif(user["ethnicity"] == "White American"):
            ethnicity = 0.3
        elif(user["ethnicity"] == "Africans"):
            ethnicity = 0.45
        elif(user["ethnicity"] == "Asian Americans"):
            ethnicity = 0.6
        elif(user["ethnicity"] == "Native Americans"):
            ethnicity = 0.75
        elif(user["ethnicity"] == "Middle Easterners"):                
            ethnicity = 1.0
        else:
            ethnicity = 1

        inputarr = [ethnicity, user["age"], user["current_weight"], life, user["current_height"], gen]
        inputarr[1] = (float(inputarr[1]) - age_min)/(age_max-age_min)
        inputarr[2] = (float(inputarr[2]) - weight_min)/(weight_max-weight_min)
        inputarr[4] = (float(inputarr[4]) - height_min)/(height_max-height_min)
        out = calculateOutput(-0.4, -0.1, 0, 0.15, 0.4, inputarr)

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
