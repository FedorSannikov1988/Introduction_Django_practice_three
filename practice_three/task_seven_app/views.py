from django.shortcuts import render
from task_seven_app.models import Client, Order


def get_all_customer_orders_and_list_products(request, name_client: str):

    client = \
        Client.objects.filter(name=name_client).first()

    orders = \
        Order.objects.filter(client=client).all()

    context = {
        "title": f"Все заказы {name_client}",
        "name_client": name_client,
        "orders": orders
    }

    return render(request, "get_all_customer_orders_and_list_products.html", context)
