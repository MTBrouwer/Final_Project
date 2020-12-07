from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import PlayerForm, InterestForm, FavoriteCharacterForm
from .models import Player, PlayerInterest, PlayerFavoriteCharacter


@login_required(login_url='login')


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
def view_profile(request):
	# Retrieve all the products and render products.html with the data
	products = Player.objects.all()
	context = {'playerbase' : products}
	return render(request, 'Final_P1/UserProfile.html', context)

def create_profile(request):
	# Create a form instance and populate it with data from the request
	form = PlayerForm(request.POST or None)
	# check whether it's valid:
	if form.is_valid():
		# save the record into the db
		form.save()
		# after saving redirect to view_product page
		return redirect('view_player')
	# if the request does not have post data, a blank form will be rendered
	return render(request, 'Final_P1/Profile-Form.html', {'form': form})

def update_profile(request, id):
    # Get the product based on its id
    product = Player.objects.get(id=id)
    # populate a form instance with data from the data on the database
    # instance=product allows to update the record rather than creating a new record when save method is called
    form = PlayerForm(request.POST or None, instance=product)

    # check whether it's valid:
    if form.is_valid():
        # update the record in the db
        form.save()
        # after updating redirect to view_product page
        return redirect('view_profile')

    # if the request does not have post data, render the page with the form containing the product's info
    return render(request, 'Final_P1/Profile-Form.html', {'playerbase': form, 'product': product})
########################




########################
def index(request):
    return render(request, 'Final_P1/Home.html')
def index2(request):
    return render(request, 'Final_P1/Game.html')
def index3(request):
    return render(request, 'Final_P1/Community.html')
def index4(request):
    return render(request, 'Final_P1/About.html')
def index5(request):
    return render(request, 'Final_P1/Roster.html')
def indexO(request):
    return render(request, 'Final_P1/Roster.html')
def indexF(request):
    return render(request, 'Final_P1/Roster.html')
def indexS(request):
    return render(request, 'Final_P1/Roster.html')
def indexH(request):
    return render(request, 'Final_P1/Roster.html')
def indexR(request):
    return render(request, 'Final_P1/register.html')
def indexProfile(request):
    return render(request, 'Final_P1/UserProfile.html')