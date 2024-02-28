from django.shortcuts import render,HttpResponseRedirect
from app import models
from django.contrib import messages
from .models import*
# Create your views here.
def index(request):
    # uid=request.session['username']

    return render(request,"index-2.html")


def cart(request):
    return render(request,"cart.html")



def checkout(request):
    return render(request,"checkout.html")



def shop(request):
    return render(request,"shop-list-sidebar.html")


def blog(request):
    return render(request,"blog-grid.html")

def blogdetails(request):
    return render(request,"blog-details.html")


def vendor(request):
    return render(request,"vendor.html")


def contact(request):
    return render(request,"contact-us.html")


def vendorprofile(request):
    return render(request,"vendor-profile.html")


def compare(request):
    return render(request,"compare.html")

def login(request):
    return render(request,"login/index12.html")

def vendordashboard(request):
    return render(request,"vendor-dashboard.html")


def new_page(request):
    return render(request,"login/demologin.html")




def register(request):
    if request.method == 'POST':
        # Get form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        request.session['emaill'] = email
        phonenumber=request.POST.get("phonenumber")
        password = request.POST.get('password')

        # Check if username already exists
        if Register.objects.filter(username=username).exists():
            error_messages = 'Username already exists.'
            messages.info(request, error_messages)
            return HttpResponseRedirect('login')

        # Generate verification code
        # verification_code = generate_verification_code()

        # Save user to database with verification code
        user = Register.objects.create(username=username, email=email,phonenumber=phonenumber ,password=password).save()
# verification_code=verification_code
        # Send registration email with verification link
        # subject = 'Welcome to Our Website - Verify Your Email'
        # verification_link = f'http://yourwebsite.com/verify/{verification_code}/'
        # message = f"""
        #     Hi {username},

        #     Thank you for registering on our website! Please click the following link to verify your email address:

        #     {verification_link}

        #     If you didn't register on our website, please ignore this email.

        #     Regards,
        #     Your Website Team
        #     """
        # send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

        # Add success message using Django messages framework
        messages.success(request,
                         'Successfully registered! An email has been sent to your email address for verification.')

        return HttpResponseRedirect('login')

        # Render registration form template for GET request
    return render(request, 'login/index12.html')




def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if a user with the provided email and password exists
        user = Register.objects.filter(email=email, password=password).first()

        if user:
            # User exists, set session flag and redirect to the home page or any other desired URL
            request.session['is_logged_in'] = True
            request.session['email'] = email
            request.session['username'] =user.username
            request.session.save()
            return HttpResponseRedirect('index')
        else:
            # User does not exist or email/password combination is incorrect
            # Set a custom error message
            error_message = 'Incorrect Username or password. Please try again.'
            messages.error(request, error_message)
            return render(request, 'login/index12.html')

    # Render the login page for GET requests
    return render(request, 'login/index12.html')



def logout(request):
    request.session['is_logged_in']=False
    return HttpResponseRedirect('index')




def otp(request):
    email=request.session['emaill']
    return render(request,"otp.html")
    # return render(request,"otp.html" ,{"email" : email})