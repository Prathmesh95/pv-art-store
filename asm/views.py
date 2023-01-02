from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.contrib.auth.models import User
from django.contrib import messages
from .models import product
from django.contrib.auth  import authenticate,  login, logout
from django.core.mail import send_mail
from cart.cart import Cart


# Create your views here.
def index(request):
    return render(request,'index.html')



#Product
def n1(request):
    error = ""
    Product = product.objects.all()

    data={
        'product':Product
    }

    return render(request, 'n1.html', {'product':Product})





#signup
def handelsignup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous input

        if (pass1 != pass2):
            messages.error(request, " Passwords do not match")
            return redirect('home')

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, " Your login has been successfull")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")





#Login
def handelLogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")

    return HttpResponse("login")




#Logout
def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')




#Contact
def ContactUs(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')


        data = {
            'name' : name,
            'email' : email,
            'subject' : subject,
            'message' : message

        }
        message = '''
        New message: {}
        
        
        From: {}
        '''.format(data['message'],data['email'])
        send_mail(data['subject'],message,'',['regaltos789@gmail.com'])
        return redirect("home")
    return render(request, "home")





# Add to Cart
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')


def cart_add(request, id):
    cart = Cart(request)
    Product = product.objects.get(id=id)
    cart.add(product=Product)
    return redirect("/n1")

def item_clear(request, id):
    cart = Cart(request)
    Product = product.objects.get(id=id)
    cart.remove(Product)
    return redirect("cart_detail")


def item_increment(request, id):
    cart = Cart(request)
    Product = product.objects.get(id=id)
    cart.add(product=Product)
    return redirect("cart_detail")


def item_decrement(request, id):
    cart = Cart(request)
    Product = product.objects.get(id=id)
    cart.decrement(product=Product)
    return redirect("cart_detail")


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")




def cart_detail(request):
    return render(request, 'cart/cart_detail.html')





