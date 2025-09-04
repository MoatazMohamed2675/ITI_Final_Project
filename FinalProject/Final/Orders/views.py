
from urllib import request
from django.shortcuts import get_object_or_404, redirect, render

from .models import *
from Menu.models import Menu

# Create your views here.

def order_list(request):
    orders_data = []

    for order in Order.get_orders():
        items = order.orderitem_set.all()
        orders_data.append({
            "id": order.id,   # ✅ add order id here
            "customer_name": order.customer_name,
            "phone": order.phone,
            "date": order.created_at,
            "items": items,
            "total_price": order.total_price,
        })
    context = {"orders": orders_data}
    return render(request, "Orders/order_list.html", context)

def add_order(request):
   
    if request.method == "POST":
        customer_name = request.POST.get("customer_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        order = Order.objects.create(customer_name=customer_name, phone=phone, email=email)
        menu_items = request.POST.getlist("menu_item[]")
        quantities = request.POST.getlist("quantity[]")
        for item_id, quantity in zip(menu_items, quantities):
            if quantity.strip() == "":  
                continue

            menu_item = Menu.objects.get(id=item_id)
            quantity = int(quantity)

            OrderItem.objects.create(
                order=order,
                menu_item=menu_item,
                quantity=quantity,
                total_price=menu_item.price * quantity,
            )
        return redirect("order_list")
    menu_items = Menu.objects.all()
    return render(request, "Orders/add_order.html", {"menu_items": menu_items})

def delete_order(request, order_id):
    order = Order.get_order_by_id(order_id)
    if order:
        order.delete()
    return redirect("order_list")

def update_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    menu_items = Menu.objects.all()

    # Attach quantity attribute to each menu_item for template use
    order_items_dict = {oi.menu_item.id: oi.quantity for oi in order.orderitem_set.all()}
    for item in menu_items:
        item.existing_qty = order_items_dict.get(item.id, 0)

    if request.method == "POST":
        order.customer_name = request.POST.get("customer_name")
        order.phone = request.POST.get("phone")
        order.save()

        for item in menu_items:
            qty = int(request.POST.get(f"quantity_{item.id}", 0))
            if qty > 0:
                OrderItem.objects.update_or_create(
                    order=order,
                    menu_item=item,
                    defaults={"quantity": qty, "total_price": qty * item.price}
                )
            else:
                OrderItem.objects.filter(order=order, menu_item=item).delete()

        return redirect("order_list")

    return render(request, "Orders/update_order.html", {
        "order": order,
        "menu_items": menu_items,
    })