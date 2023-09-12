from django import forms
from .models import profile

GENDER_CHOICES = [
      ('MALE', "Male"),
      ('FEMALE', "female")
     

]
Interest_Choice = [
       ('HTML', 'html'),
       ('CSS', 'css'),
       ('Javascript','javascript'),
       ('PHP', 'PHP')

   ]


class profileForm(forms.ModelForm):
    gender = forms.ChoiceField(choices= GENDER_CHOICES, widget = forms.RadioSelect())
    skills = forms.MultipleChoiceField(choices=Interest_Choice)
    dob = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = profile
        fields = ['name', 'dob', 'gender', 'pin', 'phone', 'mail', 'state', 'skills', 'img']     

        label = {'name':'NAME', 'dob':'Birthdate', 'Gender':'Identifier', 'pin':'PIN Code', 'phone':'Mobile Number', 'mail':'G-MAIL ID (Only)', 'state':'REGION', 'skills':'INTERESTS', 'img':'Profile Image'}      
   
        widgets = {

               'name' : forms.TextInput(),
                'dob' : forms.DateInput(),
                'gender' : forms.Select(),
                'pin' : forms.NumberInput(),
                'phone' : forms.NumberInput(),
                'mail' : forms.EmailInput(),
                'state' : forms.Select(),
                'skills' : forms.CheckboxSelectMultiple(),
                
        }