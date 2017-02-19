from django import forms

class UserForm(forms.Form):
    first_name = forms.CharField(max_length = 200, required = False)
    last_name = forms.CharField(max_length = 200, required = False)
    ethnicity = forms.CharField(max_length = 200, required = False)
    age = forms.CharField(max_length = 200, required = False)
    lifestyle = forms.CharField(max_length = 200, required = False)
    gender = forms.CharField(max_length = 200, required = False)
    current_weight = forms.CharField(max_length = 200, required = False)
    goal_weight = forms.CharField(max_length = 200, required = False)
    current_height = forms.CharField(max_length = 200, required = False)
    
