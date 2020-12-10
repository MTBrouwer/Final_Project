from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import studentInfoForm, studentInterestForm, clubForm
from .models import studentInfo, favorite, clubs
from django.shortcuts import render


########################
def register_view(request):
    # This function renders the registration form page and create a new user based on the form data
    if request.method == 'POST':
        # We use Django's UserCreationForm which is a model created by Django to create a new user.
        # UserCreationForm has three fields by default: username (from the user model), password1, and password2.
        # If you want to include email as well, switch to our own custom form called UserRegistrationForm
        form = UserCreationForm(request.POST)
        # check whether it's valid: for example it verifies that password1 and password2 match
        if form.is_valid():
            form.save()
            # if you want to login the user directly after saving, use the following two lines instead, and redirect to index
            # user = form.save()
            # login(user)
            # redirect the user to login page so that after registration the user can enter the credentials
            return redirect('login')
    else:
        # Create an empty instance of Django's UserCreationForm to generate the necessary html on the template.
        form = UserCreationForm()
    return render(request, 'Final_P1/register.html', {'form': form})

def login_view(request):
    # this function authenticates the user based on username and password
    # AuthenticationForm is a form for logging a user in.
    # if the request method is a post
    if request.method == 'POST':
        # Plug the request.post in AuthenticationForm
        form = AuthenticationForm(data=request.POST)
        # check whether it's valid:
        if form.is_valid():
            # get the user info from the form data and login the user
            user = form.get_user()
            login(request, user)
            # redirect the user to index page
            return redirect('index')
    else:
        # Create an empty instance of Django's AuthenticationForm to generate the necessary html on the template.
        form = AuthenticationForm()
    return render(request, 'Final_P1/Login.html', {'form': form})

def logout_view(request):
    # This is the method to logout the user
    logout(request)
    # redirect the user to index page
    return redirect('index')
########################
# CRUD COMMANDS
@login_required(login_url='login')
def view_profile(request):
    student = studentInfo.objects.all()
    context = {'students': student}
    return render(request, 'Final_P1/Home.html', context)

def view_students(request):
    students=studentInfo.objects.all()
    context = {'students': students}
    return render (request, 'Final_P1/Community.html', context)
def create_profile(request):
    if request.method == 'POST':
        form = studentInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
        else:
            form = studentInfoForm()
            context = {'form': form}
            return render(request, 'Final_P1/Profile-Form.html', context)


def update(request, id):
    student = studentInfo.objects.get(id=id)
    # Place created at variable here
    form = studentInfoForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {'form': form}
    return render(request, 'add.html', context)


def delete(request, id):
    student = studentInfo.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('index')
    context = {'students': student}
    return render(request, 'delete.html', context)

########################
def AddPlayerForm(request):
    if request.method == 'POST':
        form = studentInfoForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('index')
    else:
        form = studentInfoForm()
        context = {'form': form}
        return render(request, 'Final_P1/Profile-Form.html', context)

def InterestForm(request):
    if request.method == 'POST':
        form = studentInterestForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('index')
    else:
        form = studentInterestForm()
        context = {'form': form}
        return render(request, 'Final_P1/Profile-Form.html', context)
    #form = studentInfoForm()
   # form2 = studentInterestForm()
    #form3 = clubForm()
   # context = {'form': form,}#'#form2': form2,'form3': form3}
    #return render(request,'Final_P1/Profile-Form.html',context)

def favorite(request):
    if request.method == 'POST':
        form = clubForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('index')
    else:
        form = clubForm()
        context = {'form': form}
        return render(request, 'Final_P1/Profile-Form.html', context)





#FavoriteCharacterForm
########################
def index(request):
    return render(request, 'Final_P1/Home.html')
def game(request):
    return render(request, 'Final_P1/Game.html')
def community(request):
    student = studentInfo.objects.all()
    context = {'students': student}
    return render(request, 'Final_P1/Community.html', context)
    return render(request, 'Final_P1/Community.html',context)
def about(request):
    return render(request, 'Final_P1/About.html')
def ProfileForm(request):
    return render(request, 'Final_P1/Profile-Form.html')
def indexR(request):
    return render(request, 'Final_P1/register.html')
def indexProfile(request):
    return render(request, 'Final_P1/UserProfile.html')