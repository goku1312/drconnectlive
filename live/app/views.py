from django.shortcuts import render,HttpResponseRedirect
from app import models
from django.contrib import messages
from .models import*
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
# 





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




# def register(request):
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

       
        # user = Register.objects.create(username=username, email=email,phonenumber=phonenumber ,password=password).save()

            
        message =  get_random_string(length=4, allowed_chars='0123456789')
        request.session['message']=message
            
        
        # Assuming you have a default email address set in your Django settings
        recipient_email = settings.DEFAULT_FROM_EMAIL
      
        print(email)
        print(recipient_email)
       
        # Send email
        send_mail(
    'Send registration email with verification link',
    'Welcome to Our Website - Verify Your Email',
    f'''
Hi {username},

Thank you for registering on our website! Your verification code is: {message}

If you didn't register on our website, please ignore this email.

Regards,
Your Website Team
''',
    settings.DEFAULT_FROM_EMAIL,
    [email],
     
    
)

        # Return a success response
            
        messages.success(request,
                         'Successfully registered! An email has been sent to your email address for verification.')

        return render(request,'otp.html')

        # Render registration form template for GET request
    return render(request, 'login/index12.html')


def register(request):
    if request.method == 'POST':
        # Get form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        request.session['emaill'] = email
        phonenumber = request.POST.get("phonenumber")
        password = request.POST.get('password')

        # Check if username already exists
        if Register.objects.filter(username=username).exists():
            error_messages = 'Username already exists.'
            messages.info(request, error_messages)
            return HttpResponseRedirect('login')
        

        

        message = get_random_string(length=4, allowed_chars='0123456789')
        request.session['message'] = message

        # Assuming you have a default email address set in your Django settings
        recipient_email = settings.DEFAULT_FROM_EMAIL
      
        print(email)
       
        # Send email
        send_mail(
    'OTP Verification',
    f'Hi {username},\n\n'
    f'Thank you for registering on our website! Your One-Time Password (OTP) for verification is: <b>{message}</b>\n\n'
    f'If you didn\'t register on our website, please ignore this email.\n\n'
    f'Regards,\n'
    f'Your Website Team',
    settings.DEFAULT_FROM_EMAIL,
    [email],
    fail_silently=False,
)

        # Return a success response
        messages.success(request,
                         'Successfully registered! An email has been sent to your email address for verification.')

        return render(request, 'otp.html')

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





# def otp(request):
#  try:
#         email = request.session['email']
#         username = request.session['username']
#         message = request.session['message']
#         print(message)
#         otp = request.POST.get('otp')
#         print(otp)
        

#         if int(otp) == int(message):
#             existing_login =Register.objects.filter(username=username).first()

# # Assuming 'email' is the field representing the email
#             if existing_login:
#     # If the username exists, update the email
#                 existing_login.email = email  # Replace 'new_email' with the email you want to set
#                 existing_login.save()
            
#             return HttpResponseRedirect('login')
#         else:
#             messages.error(request, 'Invalid OTP')
# except Exception as e:
#     messages.error(request, f'Error in OTP verification: {e}')

#     return render(request,"otp.html")
    