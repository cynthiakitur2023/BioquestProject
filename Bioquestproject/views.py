from django.shortcuts import render, redirect
from .models import Customers
from .forms import Category,Product
from .models import Categories,Products
from django.contrib import messages
from  django.contrib.auth.decorators import login_required
from django import template
from django.contrib.auth.models import Group
register = template.Library()

@login_required
def add(request):
    categories = Categories.objects.all()
    if request.method == 'POST':
        form = Category(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,f'Category added successfully')
            return redirect('display')
    else:
        form = Category()

    return render(request,'products.html',{'form':form,'title':'Add category','categories':categories})

@login_required()
def add_products(request):
    categories = Categories.objects.all()
    products = Products.objects.all()
    if request.method == 'POST':
        form = Product(request.POST,request.FILES)
        if form.is_valid():

            form.save()
            messages.success(request,f'Product added successfully')
            image_name = str(form.cleaned_data['image'].name)
            category_id = request.POST.get('variety')
            description = request.POST.get('description')
            name = request.POST.get('name')
            product = Products(name=name, variety=category_id, description=description, image=image_name, photoname=image_name)
            product.save()
            return redirect('add_products')
    else:
        form = Product()

    return render(request,'admin-add-products.html',{'form':form,'title':'Add product','categories':categories,'products':products})



# def show(request):
#     products = Categories.objects.all()
#     return render(request, 'admin-add-products.html', {'products': products})

def display(request):
    categories = Categories.objects.all()
    return render(request,'products.html',{'categories':categories})




def category_products(request,id):
    categories = Categories.objects.all()
    products = Products.objects.filter(variety=id)
    return render(request,'categoryproducts.html',{'products':products,'categories':categories})

def filterprodut(request):
    name = request.POST.get('name')
    products = Products.objects.filter(name__icontains=name)
    return render(request,'filtered.html',{'products':products})


# def my_view(request):
#         form = MyForm()
#         return render(request, 'admin-add-products.html', {'form': form})

def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        query = Customers(name=name, email=email, phone=phone )
        query.save()
        return redirect("contact")


def contactpage(request):
    categories = Categories.objects.all()
    return render(request, 'contact.html', {'categories': categories})


@login_required()
def deleteData(request, id):
    d = Customers.objects.get(id= id)
    d.delete()
    return redirect("contact")
    return render(request, "contact.html")


def homepage(request):
    categories = Categories.objects.all()
    return render(request, 'index.html', {'categories':categories} )




def aboutpage(request):
    categories = Categories.objects.all()
    return render(request, 'about.html', {'categories':categories} )






def productpage(request):
    categories = Categories.objects.all()
    return render(request, 'products.html', {'categories': categories})

def singleproduct(request, id):
    categories = Categories.objects.all()
    product = Products.objects.get(id =id)
    return render(request, 'singleproduct.html', {'product': product,'categories': categories})

@login_required
def contactlist(request):
    categories = Categories.objects.all()
    data = Customers.objects.all()
    return render(request, 'Contactlist.html', {'categories': categories ,"data": data})


@register.simple_tag
def admin_button(user):
    admin_group = Group.objects.get(name='admin')
    return user.groups.filter(name=admin_group).exists()



