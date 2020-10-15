from django import forms

class StudentForm(forms.Form):
    s_name = forms.CharField(max_length=100)