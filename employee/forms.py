from django import forms
from employee.models import *

def check_name(value):
    if len(value)<=3:
        raise forms.ValidationError('Name length should be more then 3')

class EmpForm(forms.ModelForm):
    name=forms.CharField(max_length=100,validators=[check_name],widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Emp Name'}))
    
    class Meta:
        model=Employee
        fields=['name','email','mobile','position']
        widgets={
                 'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email'}),
                 'mobile':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Mobile Number'}),
                 'position':forms.Select(attrs={'class':'form-control'})
                 }
        
        
    def __init__(self,*args,**kwargs):
        super(EmpForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label='---Select---'
        self.fields['mobile'].required=False

    
        
