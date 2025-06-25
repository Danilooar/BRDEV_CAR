from django.views.generic import ListView, CreateView, DetailView, UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Car, Brand
from .forms import CarModelForm
from django.db.models import Q



@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView): # type: ignore
    model = Car 
    template_name = 'car_delete.html'
    success_url = reverse_lazy('car_views')
    
@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    success_url = reverse_lazy('car_views')

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})

class CarsView(ListView):
    model = Car
    template_name = "cars.html"
    context_object_name = "carros"
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")
        marca_id = self.request.GET.get("marca")
        preco = self.request.GET.get("preco")

        if query:
            queryset = queryset.filter(modelo__icontains=query)

        if marca_id:
            queryset = queryset.filter(marca_id=marca_id)

        if preco:
            if preco == "50000":
                queryset = queryset.filter(preco__lte=50000)
            elif preco == "100000":
                queryset = queryset.filter(Q(preco__gt=50000) & Q(preco__lte=100000))
            elif preco == "150000":
                queryset = queryset.filter(Q(preco__gt=100000) & Q(preco__lte=150000))
            elif preco == "150001":
                queryset = queryset.filter(preco__gt=150000)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["marcas"] = Brand.objects.all()
        return context



@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
        model = Car
        form_class = CarModelForm
        template_name = 'newcar.html'
        success_url =  reverse_lazy('car_views')




class CarDetailView(DetailView):
    model = Car
    template_name = "car_detail.html"
    context_object_name = "carro"


