from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404,redirect
from .models import Car,Brand
from cars.forms import CarForm



def new_car_view(request):
  if request.method == "POST":
    new_car_form = CarForm(request.POST, request.FILES) 
    if new_car_form.is_valid():
      new_car_form.save()
      return redirect('car_list')
   
  else:
    new_car_form = CarForm()
    return render(request, "new_car.html", {"new_car_form": new_car_form})
    
    
def car_detail(request, id):
    carro = get_object_or_404(Car, id=id)
    return render(request, 'car_detail.html', {'carro': carro})

def car_views(request):
    query = request.GET.get("q")
    marca_id = request.GET.get("marca")
    preco = request.GET.get("preco")

    carros = Car.objects.all()

    if query:
        carros = carros.filter(modelo__icontains=query)

    if marca_id:
        carros = carros.filter(marca_id=marca_id)

    if preco:
        if preco == "50000":
            carros = carros.filter(preco__lte=50000)
        elif preco == "100000":
            carros = carros.filter(preco__gt=50000, preco__lte=100000)
        elif preco == "150000":
            carros = carros.filter(preco__gt=100000, preco__lte=150000)
        elif preco == "150001":
            carros = carros.filter(preco__gt=150000)

    paginator = Paginator(carros, 6)  # 6 carros por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "carros": page_obj,
        "marcas": Brand.objects.all()
    }

    return render(request, "cars.html", context)
