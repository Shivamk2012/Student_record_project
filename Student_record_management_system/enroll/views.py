from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .import models
from .forms import SearchForm
from .models import Student

# Register new
def sign_up(request):
 if request.method == "POST":
  fm = SignUpForm(request.POST)
  if fm.is_valid():
   messages.success(request, 'Account Created Successfully !!')
   fm.save()
   return HttpResponseRedirect('/view-student/')
 else:
  fm = SignUpForm()
 return render(request, 'enroll/signup.html', {'form':fm})

# Login View Function
def user_login(request):
  if not request.user.is_authenticated:
    if request.method == "POST":
      fm = AuthenticationForm(request=request, data=request.POST)
      if fm.is_valid():
        uname = fm.cleaned_data['username']
        upass = fm.cleaned_data['password']
        user = authenticate(username=uname, password=upass)
        if user is not None:
          login(request, user)
          messages.success(request, 'Logged in successfully !!')
          if user.get_username()=='admin':
            return HttpResponseRedirect('/view-student/')
          else:
            return HttpResponseRedirect('/profile/')
    else:
      fm = AuthenticationForm()
    return render(request, 'enroll/userlogin.html', {'form':fm})
  else:
    return HttpResponseRedirect('/profile/')


# Profile / student dashboard
def user_profile(request):
  if request.user.is_authenticated:
    students=models.Student.objects.filter(username=request.user)
    return render(request, 'enroll/profile.html', {'name': request.user,'students':students})
  else:
    return HttpResponseRedirect('/login/')

# Logout
def user_logout(request):
  logout(request)
  return HttpResponseRedirect('/')


# view students / student list screen
def viewstudents(request):
  if request.user.is_authenticated:
    students=models.Student.objects.all()
    #username=request.session['username']
    return render(request,'enroll/view_students.html',{"students":students})
  else:
    return HttpResponseRedirect('/login/')


# This function will search
def searchStudent(request):
    form=SearchForm()
    return render(request,'enroll/search_student.html',{'form':form})

def search(request):
    form=SearchForm(request.POST)
    students=models.Student.objects.filter(first_name=form.data['first_name'])
    return render(request,'enroll/search_student.html',{'form':form,'students':students})

# This Function will Update/Edit
def update_data(request, id):
 if request.method == 'POST':
  pi = Student.objects.get(pk=id)
  fm = SignUpForm(request.POST, instance=pi)
  if fm.is_valid():
   fm.save()
 else:
  pi = Student.objects.get(pk=id)
  fm = SignUpForm(instance=pi)
 return render(request, 'enroll/edit_student.html', {'form':fm})


#first login page+css
def first_login(request):
  return render(request,'enroll/first_login_page.html')


# This Function will Delete
def delete_data(request, id):
 if request.method == 'POST':
  return render(request,'enroll/delete.html',{'pi':id})

# confirm delete
def confirm_delete(request,id):
    pi=Student.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect('/view-student/')
