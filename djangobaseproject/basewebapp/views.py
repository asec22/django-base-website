from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

# Create your views here.

# The homepage view: Pass any variables into the 
# dict{} in the render command. The render fuction renders the page
# requested by the url request.  Register your urls in the urls.py
# page in app or the project folders. The views are defined as a function.

def home(request):
    return render(request,"main/home.html",{})

#The about page view:

def about(request):
    return render(request,"main/about.html",{})

#The services page view:

def services(request):
    return render(request,"main/services.html",{})

#The contact page view: Enter all your email smtp information 
#in settings.py in the project folders. See your email provider for the information
#on the smtp settings and to activate the protocol in your service.  The first email is your
#email account from which you are sending the eamil, while the second email is the reciever
#of the email.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email to you
            send_mail(
                'New Contact Form Submission',
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                'your_email@company.com',  # Your email
                ['your_email@company.com'],  # Your email
                fail_silently=False
            )

            # Redirect to success page or handle success differently
            return render(request,'main/success.html')  # Assuming you have a success view

    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})