

# Create your views here.
import datetime

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

# Create your views here.
from FoodApp.models import *


def add_food_details(request):
    return render(request,'add_food_details.html')

def add_food_details_post(request):
     name=request.POST['name']
     description=request.POST['description']
     size=request.POST['size']
     available=request.POST['available']
     price=request.POST['price']
     image=request.FILES['image']

     fs=FileSystemStorage()
     path=fs.save(image.name,image)

     b=Food_Details()
     b.name=name
     b.description=description
     b.size=size
     b.image=path
     b.available=available
     b.price=price
     b.save()
     return redirect('/FoodApp/view_food_details/')

def view_food_details(request):
    a=Food_Details.objects.all()
    return render(request, 'view_food_details.html', {'data':a})

def delete_view_food_details(request,id):
    var=Food_Details.objects.get(id=id)
    var.delete()
    return redirect('/FoodApp/view_food_details/')


def edit(request,id):
    var1=Food_Details.objects.get(id=id)
    return render(request,'edit.html',{'data':var1})


def edit_post(request):
    id = request.POST['id']
    name = request.POST['name']
    description = request.POST['description']
    size = request.POST['size']
    available = request.POST['available']
    price = request.POST['price']

    b = Food_Details.objects.get(id=id)
    if 'image' in request.FILES:
        image = request.FILES['image']

        fs = FileSystemStorage()
        path = fs.save(image.name, image)
        b.image = path

    b.name = name
    b.description = description
    b.size = size
    b.available = available
    b.price=price
    b.save()
    return redirect('/FoodApp/view_food_details/')

def home_page(request):
    var=Food_Details.objects.all()
    var2=category.objects.all()
    return render(request, 'home_page.html',{'data':var,'data2':var2})

def add_category(request):
    return render(request,'category.html')

def category_post(request):
  cate = request.POST['category']
  image= request.FILES['image']

  b = category()

  fs = FileSystemStorage()
  path = fs.save(image.name, image)
  b.image = path

  b.category = cate
  b.save()
  return redirect('/FoodApp/view_category/')

def view_category(request):
    a=category.objects.all()
    return render(request, 'view_category.html',{'data':a})

def delete_category(request,id):
    var=category.objects.get(id=id)
    var.delete()
    return redirect('/FoodApp/view_category/')

def edit_category(request,id):
    var1=category.objects.get(id=id)
    return render(request,'edit_category.html',{'data':var1})


def edit_category_post(request):
    id = request.POST['id']
    categorys = request.POST['category']

    b = category.objects.get(id=id)
    if 'image' in request.FILES:
        image = request.FILES['image']

        fs = FileSystemStorage()
        path = fs.save(image.name, image)
        b.image = path

    b.category = categorys
    b.save()
    return redirect('/FoodApp/view_category/')



def admin_home(request):
    return render(request,'admin_home.html')

def login_page(request):
    return render(request, 'login_page.html')

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_post(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user is not None:

        if user.groups.filter(name='admin').exists():
            login(request, user)
            return redirect('/FoodApp/admin_home/')

        elif user.groups.filter(name='user').exists():
            login(request, user)
            return redirect('/FoodApp/home_page/')

        else:
            return render(request, 'login_page.html', {
                'error': 'User has no assigned role'
            })

    return render(request, 'login_page.html', {
        'error': 'Invalid username or password'
    })





from django.shortcuts import redirect, render



# Create your views here.
def register_user(request):
    return render(request,'user register.html')

from django.contrib.auth.models import User, Group
from django.shortcuts import redirect

def register_user_post(request):

    name = request.POST['name']
    email = request.POST['email']
    place = request.POST['place']
    pin = request.POST['pin']
    qualification = request.POST['qualification']
    phone = request.POST['phone']
    username = request.POST['username']
    password = request.POST['password']

    # Create login user
    user = User.objects.create_user(
        username=username,
        password=password
    )

    # Add to 'user' group
    group = Group.objects.get(name='user')
    user.groups.add(group)

    # Save additional details
    a = user_management_table()
    a.name = name
    a.email = email
    a.place = place
    a.pin = pin
    a.qualification = qualification
    a.phone = phone
    a.LOGIN = user
    a.save()

    return redirect('/FoodApp/login_page/')

def view_user_details(request):
    a = user_management_table.objects.all()
    return render(request,'view_user_details.html',{'data':a})

def user_make_order(request,id):
    a = Food_Details.objects.get(id=id)
    return render(request,'user_make_order.html',{'data':a})

def user_make_order_post(request):
    building_no = request.POST['building_no']
    landmark = request.POST['landmark']
    contact = request.POST['contact']
    foodid = request.POST['foodid']
    shipping_addresspin = request.POST['shipping_address']


    a=Food_Booking()
    a.FOOD=Food_Details.objects.get(id=foodid)
    a.USER=user_management_table.objects.get(LOGIN_id=request.user.id)
    a.building_no=building_no
    a.date=datetime.datetime.now().today().date()
    a.status='ordered'
    a.landmark=landmark
    a.contact=contact
    a.shipping_addresspin=shipping_addresspin
    a.save()
    return redirect('/FoodApp/home_page/')

def view_order_details(request):

    user = user_management_table.objects.get(LOGIN_id=request.user.id)

    orders = Food_Booking.objects.filter(USER=user).order_by('-id')

    return render(request,'view_order_details.html',{'orders': orders})


def admin_view_orders(request):


    orders = Food_Booking.objects.all().order_by('-id')

    return render(request, 'admin_view_order.html', {'orders': orders})



















