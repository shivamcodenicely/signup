
from django.shortcuts import render
from .models import Sign
from django.core.mail import EmailMessage
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import JsonResponse
import random
import json
# Create your views here.

def post_list(request):
    return render(request,
                  'index.html',
                  )


def new1(request):
    if request.method=="POST":
        print("##############################################")
        fname = request.POST.get("first_name")
        lname = request.POST.get("last_name")
        username = request.POST.get("user_name")
        password = request.POST.get("user_password")
        #confirm_password=request.POST.get("confirm_password")
        global email,fname,username,contact
        email = request.POST.get("email")
        contact=request.POST.get("contact_no")

        for x in range(1000,9999):
            global otp
            otp = random.randrange(1000,9999)
            break

            # email = EmailMessage('Subject', otp, to=['email'])
            # print(email)
            # email.send()

            # msg = EmailMessage('subject', otp , to = [])
            # msg.send()

        send_mail('test email', str(otp), 'shivam.mittal38@gmail.com', [email])

        emp=Sign.objects.create(fname=fname,lname=lname,username=username,password=password,email=email,contact=contact)
        emp.save()



        return render(request,
                      'otp.html',{"email":email})
    '''def post(self):
        post = Sign.objects.all()
        return render(post)'''

def Otp(request):
    otp1=request.POST.get("OTP")

    if otp1==str(otp):
        return render(request,"page.html",{"Name":fname,"email":email,"username":username,"contact":contact})
    else:
        print("error")

        return render(request,"otp.html")
def login(request):
    email=request.POST.get("email")
    password = request.POST.get("user_password")
    user=authenticate(email="email",password="user_password")

    if user is not None:
        return render(request,"page.html")
    else:
        return render(request,"login.html")


def authn(request):
     if request.method=="POST":
         data = Sign.objects.all()
         for i in data:
             # print("#################")
             pssword =(i.password)
             email=(i.email)
             name=(i.fname)
             user=(i.username)
             contact=(i.contact)
         get_pwd=request.POST.get('user_password')
         get_email=request.POST.get('email')
         if pssword==get_pwd and email==get_email:
             print("true")
             return render(request, "page.html",{'email':email,'Name':name,'username':user,'contact':contact})

         else:

             return render (request,"login.html")

def validate_username(request):
    email = request.POST.get('email', None)
    print(email)
    data = {
        'is_taken': Sign.objects.filter(email__iexact=email).exists()
    }
    return JsonResponse(data)


