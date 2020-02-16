from django.shortcuts import render, get_object_or_404
from app4.models import Pizza

def home(request):
    pizzas = Pizza.objects.all()
    return render(request, 'indextemplates.html', {'pizzas': pizzas})

def pizza_detail(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)
    return render(request, 'pizza_detail.html', {'pizza': pizza})
