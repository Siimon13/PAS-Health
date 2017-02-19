from django import forms

diets = ["Paleo", "Low-Carb", "Ultra Low-Fat", "Dukan", "Atkins", "HCG", "Zone Diet", "Fasting"]

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
    current_diet = forms.CharField(max_length = 200, required = False)

class UpdateForm(forms.Form):
    options = forms.CharField(max_length = 200, required = False)
    hashid = forms.CharField(max_length = 200, required = False)
    # value = forms.ModelChoiceField(queryset=diets, widget=forms.widgets.RadioSelect() )
