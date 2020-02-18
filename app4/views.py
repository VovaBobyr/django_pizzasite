from django.shortcuts import render, get_object_or_404
from app4.models import Pizza
from app4.formy import OrderForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    pizzas = Pizza.objects.all()
    return render(request, 'indextemplates.html', {'pizzas': pizzas})

def pizza_detail(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)
    form = OrderForm(request.POST or None, initial={
        'pizza':pizza
    })

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('{}?sent=True'.format(reverse('pizza-detail', kwargs={'pizza_id':pizza.id})))

    return render(request, 'pizza_detail.html', {
        'pizza': pizza,
        'form': form,
        'sent': request.GET.get('sent', False)
    })
