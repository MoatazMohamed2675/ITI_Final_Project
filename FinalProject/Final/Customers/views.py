from django.shortcuts import redirect, render
from .models import Customer
# Create your views here.

def customers_list(request):
    customers = Customer.objects.all()
    return render(request, "Customers/customers_list.html", {"customers": customers})

def add_customer(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        Customer.objects.create(name=name, email=email, phone=phone)
        return redirect("customers_list")
    return render(request, "Customers/add_customer.html")

def update_customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    if request.method == "POST":
        customer.name = request.POST.get("name")
        customer.email = request.POST.get("email")
        customer.phone = request.POST.get("phone")
        customer.save()
        return redirect("customers_list")
    return render(request, "Customers/update_customer.html", {"customer": customer})

def delete_customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    customer.delete()
    return redirect("customers_list")