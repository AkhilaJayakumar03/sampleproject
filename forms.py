from django import forms

class reform(forms.Form):
    username=forms.CharField(max_length=30)
    email=forms.EmailField()
    phone=forms.IntegerField()
    password=forms.CharField(max_length=20)
    confirmpassword=forms.CharField(max_length=20)


class logform(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=20)



class empform(forms.Form):
    employee_name=forms.CharField(max_length=30)
    employee_id=forms.IntegerField()
    company_name=forms.CharField(max_length=30)
    email=forms.EmailField()
    department=forms.CharField(max_length=30)

class searchform(forms.Form):
    employee_name=forms.CharField(max_length=30)
    employee_id=forms.IntegerField()


class imgform(forms.Form):
    imgname=forms.CharField(max_length=30)
    imgfile=forms.ImageField()


class audioform(forms.Form):
    audname=forms.CharField(max_length=40)
    audimg=forms.ImageField()
    audfile=forms.FileField()


class videoform(forms.Form):
    videoname=forms.CharField(max_length=30)
    videofile=forms.FileField()