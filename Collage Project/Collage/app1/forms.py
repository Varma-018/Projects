from django import forms
from .models import Department, HOD, Professor, Students

class Department_Registration(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'code']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Department Name'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Department Code'}),
        }

class HOD_Registration(forms.ModelForm):
    class Meta:
        model = HOD
        fields = ['name', 'Department', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter HOD Name'}),
            'Department': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
        }

class Professor_Registration(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['name', 'phone', 'Department', 'Subject']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Professor Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'Department': forms.Select(attrs={'class': 'form-control'}),
            'Subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Subject'}),
        }

class Student_Registration(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'Register_ID', 'Department', 'HOD']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Student Name'}),
            'Register_ID': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Registration ID'}),
            'Department': forms.Select(attrs={'class': 'form-control'}),
            'HOD': forms.Select(attrs={'class': 'form-control'}),
        }
