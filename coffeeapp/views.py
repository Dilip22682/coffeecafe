from django.shortcuts import render
from coffeeapp.models import coffee_details,chai_details
from django.core.paginator import Paginator
from coffeeapp.forms import coffeeform
from django.db.models import Q

# Create your views here.
def hello(request):
    # k="i am creating coffee returant website"
    fm=coffee_details.objects.all()
    # # for i in fm:
    # #     print(i)
    # if request.method=="POST":
    #     value=request.POST['search']
    #     print(50*'#')
    #     print("search data:",value)
    # else:
    #     return 'no data comes to backend'
    return render(request,'html/base.html',{'fm':fm})

def coffeeList(request):
    fm=coffee_details.objects.all().order_by('id')
    paginator=Paginator(fm,8)
    page_number=request.GET.get('pg')
    fm=paginator.get_page(page_number)
    return render(request,'html/coffee.html',{'fm':fm})

def orderDetails(request,id=0):
    fm=coffee_details.objects.get(id=id)
    # print(fm)
    form = coffeeform(instance=fm)
    return render(request,'html/orderpage.html',{'form':form})
 
def search_coffee_item(request):
    if request.method == 'POST':
        query = request.POST.get('q')   # 👈 YOU MISSED THIS
        print("query:",query)
        results = coffee_details.objects.filter(
            Q(coffee_name__icontains=query) |
            Q(coffee_description__icontains=query)
        )
    else:
        results = coffee_details.objects.all()
        
    return render(request, 'html/search_item.html', {'results': results})