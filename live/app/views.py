from django.shortcuts import render,HttpResponseRedirect
from app import models
from django.contrib import messages
from .models import*
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
from gtts import gTTS





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
    return render(request,"login/signup.html")

def vendordashboard(request):
    return render(request,"vendor-dashboard.html")


def new_page(request):
    return render(request,"login/signup.html")




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
        
        phonenumber = request.POST.get("phonenumber")
        password = request.POST.get('password')
        request.session['username'] = username
        request.session['email'] = email
        request.session['phonenumber'] = phonenumber
        request.session['password'] = password
        # Check if username already exists
        if Register.objects.filter(username=username).exists():
            error_messages = 'Username already exists.'
            messages.info(request, error_messages)
            return HttpResponseRedirect('login')
        
        else:
            return HttpResponseRedirect('otp')
        

        # return render(request, 'otp.html')

    # Render registration form template for GET request
    return render(request, 'login/signup.html')



def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        print(email)

        # Check if a user with the provided email and password exists
        user = Register.objects.filter(email=email, password=password).first()
        # print("1",user.username)

        if user:
            print("12",user.username)
            # User exists, set session flag and redirect to the home page or any other desired URL
            request.session['is_logged_in'] = True
            request.session['email'] = email
            request.session['username'] =user.username
            request.session.save()
            return HttpResponseRedirect('index')
        else:
            print("123",user)
            # User exists, set session flag and redirect to the home page or any other desired URL
            
            if request.session['email'] != email or request.session['username'] !=user.username :
                error_message = 'Incorrect Username or password. Please try again.'
                messages.info(request, error_message)
                print(error_message)
                return HttpResponseRedirect('signin')
            else:
            # User does not exist or email/password combination is incorrect
            # Set a custom error message
                error_message = 'Username doesn"t exists.'
                messages.info(request, error_message)
                return HttpResponseRedirect('signin')
            # messages.error(request, error_message)
            # return render(request, 'login/signin.html')

    # Render the login page for GET requests
    return render(request, 'login/signin.html')



def logout(request):
    request.session['is_logged_in']=False
    return HttpResponseRedirect('index')




def otp(request):

        username=request.session['username']
        email=request.session['email']
        phonenumber=request.session['phonenumber']
        password=request.session['password']
        message = get_random_string(length=4, allowed_chars='0123456789')
        request.session['message'] = message

        # Assuming you have a default email address set in your Django settings
        recipient_email = settings.DEFAULT_FROM_EMAIL
      
        print(email)
       
        # Send email
        send_mail(
    'OTP Verification',
    f'Hi {username},\n\n'
    f'Thank you for registering on our website! Your One-Time Password (OTP) for verification is: {message}\n\n'
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
        return render(request,"otp.html" ,{"email" : email})








def newlogin(request):
    return render(request,"newlogin.html")




def signin(request):
    return render(request,"login/signin.html")




def verifyotp(request):

    if request.method == 'POST':
        # Get values from the input fields
        otp1 = request.POST.get('otp1', '')
        otp2 = request.POST.get('otp2', '')
        otp3 = request.POST.get('otp3', '')
        otp4 = request.POST.get('otp4', '')
        username=request.session['username']
        email=request.session['email']
        phonenumber=request.session['phonenumber']
        password=request.session['password']

        # Combine the values into one string
        combined_otp = otp1 + otp2 + otp3 + otp4
        message=request.session['message']

        if int(combined_otp) == int(message):
            user = Register.objects.create(username=username, email=email,phonenumber=phonenumber ,password=password).save()
            request.session['is_logged_in']=True
            
            return HttpResponseRedirect('index')
        else:
            messages.error(request, 'Invalid OTP')





def terms(request):
    return render(request,"terms.html")




def plans(request):
    return render(request,"plans.html")




def plans1(request):
    return render(request,"plans1.html")




def doctor(request):
    return render(request,"doctor.html")



def doctorprofile(request):
    return render(request,"doctorprofile.html")