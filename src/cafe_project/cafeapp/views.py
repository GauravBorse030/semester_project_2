from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import MenuItem, Order
from django.shortcuts import render



def home(request):
    return render(request, 'index.html')  

@csrf_exempt
def place_order(request):
    if request.method == "POST":
        data = json.loads(request.body)

        table_no = data.get("table")
        name = data.get("name")
        price = data.get("price")
        image_url = data.get("image_url")

        # Check if menu item already exists, otherwise create it
        item, created = MenuItem.objects.get_or_create(
            name=name,
            defaults={"price": price, "image_url": image_url}
        )

        # Create order
        Order.objects.create(table_no=table_no, item=item)

        return JsonResponse({"message": f"Order placed for {name} on Table {table_no}"})

    return JsonResponse({"error": "Invalid request"}, status=400)
