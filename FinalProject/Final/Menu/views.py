from django.http import JsonResponse
from django.shortcuts import redirect, render

from Orders.models import Order
from .models import Menu
# Create your views here.

def menu_list(request):
    context = {}
    context['menu_items'] = Menu.objects.all()
    return render(request, "Menu/menu_list.html", context)

def add_item(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        Menu.objects.create(name=name, price=price, description=description)
        return redirect('menu_list')
    return render(request, "Menu/AddItem.html")

def delete_item(request, item_id):
    item = Menu.objects.get(id=item_id)
    item.delete()
    return redirect('menu_list')

def update_item(request, item_id):
    item = Menu.objects.get(id=item_id)
    if request.method == "POST":
        item.name = request.POST.get("name")
        item.price = request.POST.get("price")
        item.description = request.POST.get("description")
        item.save()
        return redirect('menu_list')
    return render(request, "Menu/UpdateItem.html", {"item": item})


def search_Menu(request):
    query = request.GET.get("q", "")
    if query:
        products = Menu.objects.filter(name__icontains=query)[:5]  # limit results
        data = list(products.values("id", "name", "price" ,"description"))
    else:
        data = []
    return JsonResponse({"results": data})