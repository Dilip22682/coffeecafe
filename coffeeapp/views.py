from django.shortcuts import render
from coffeeapp.models import coffee_details,chai_details
from django.core.paginator import Paginator
from coffeeapp.forms import coffeeform
from django.db.models import Q
from django.db.models import Sum
from django.contrib.auth.models import User
from .models import coffee_details,Cart,Order,OrderItem


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("coffee")    
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "html/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

def register_user(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request,'html/register.html')


# def coffeeList(request):
#     fm=coffee_details.objects.all().order_by('id')
#     paginator=Paginator(fm,8)
#     page_number=request.GET.get('pg')
#     fm=paginator.get_page(page_number)
#     return render(request,'html/coffee.html',{'fm':fm})

def coffeeList(request):

    fm = coffee_details.objects.all().order_by('id')

    paginator = Paginator(fm, 8)
    page_number = request.GET.get('pg')
    fm = paginator.get_page(page_number)

    cart_count = 0
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).aggregate(
            total=Sum('quantity')
        )['total'] or 0

    context = {
        'fm': fm,
        'cart_count': cart_count
    }

    return render(request, 'html/coffee.html', context)


@login_required
def orders(request):

    user_orders = Order.objects.filter(user=request.user).order_by('-created_at')

    return render(request,'html/orderpage.html',{
        'orders':user_orders
    })

def orderDetails(request,id=0):
    fm=coffee_details.objects.get(id=id)
    # print(fm)
    form = coffeeform(instance=fm)
    return render(request,'html/orderpage.html',{'form':form})
 
def search_coffee_item(request):
    if request.method == 'POST':
        query = request.POST.get('q')   
        print("query:",query)
        results = coffee_details.objects.filter(
            Q(coffee_name__icontains=query) |
            Q(coffee_description__icontains=query)
        )
    else:
        results = coffee_details.objects.all()
        
    return render(request, 'html/search_item.html', {'results': results})


def add_to_cart(request,id):

    coffee = get_object_or_404(coffee_details,id=id)

    cart_item,created = Cart.objects.get_or_create(
        user=request.user,
        coffee=coffee
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('coffee')

@login_required
def cart_view(request):

    # cart_items = Cart.objects.filter(user=request.user)

    # total = 0
    # cart_count=0

    # for item in cart_items:
    #     cart_count+=item
    #     total += item.total_price()

    # return render(request,'html/Cart.html',{'cart_items':cart_items,'total':total})



    cart_items = Cart.objects.filter(user=request.user)

    cart_count = 0
    total_price = 0

    for item in cart_items:
        cart_count += item.quantity
        total_price += item.quantity * item.coffee.coffee_price

    context = {
        "cart_items": cart_items,
        "cart_count": cart_count,
        "total_price": total_price
    }

    return render(request, "html/cart.html", context)
   

def cart_count(request):
    if request.user.is_authenticated:
        count = Cart.objects.filter(user=request.user).count()
    else:
        count = 0

    return {"cart_count": count}    
    

def checkout(request):

    cart_items = Cart.objects.filter(user=request.user)

    total = sum(item.total_price() for item in cart_items)

    if request.method == "POST":

        payment = request.POST.get('payment_method')

        order = Order.objects.create(
            user=request.user,
            payment_method=payment,
            total_amount=total)

        for item in cart_items:

            OrderItem.objects.create(
                order=order,
                coffee=item.coffee,
                quantity=item.quantity,
                price=item.coffee.coffee_price
            )

        cart_items.delete()

        return redirect('orders')

    return render(request,'html/checkout.html',{
        'cart_items':cart_items,
        'total':total
    })
    
 

def remove_cart(request, id):
    item = get_object_or_404(Cart, id=id)
    item.delete()
    return redirect('cart')