from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Producto, Embarque
from .forms import ProductoForm, EmbarqueForm

# Vistas de Productos
def lista_productos(request):
    productos = Producto.objects.all().prefetch_related('embarques')
    context = {'productos': productos}
    return render(request, 'productos/lista.html', context)

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'productos/producto_detalle.html'

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('productos:lista_productos')

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('productos:lista_productos')

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'productos/producto_confirm_delete.html'
    success_url = reverse_lazy('productos:lista_productos')

# Vistas de Embarques
class EmbarqueListView(ListView):
    model = Embarque
    template_name = 'productos/embarque_lista.html'
    context_object_name = 'embarques'
    queryset = Embarque.objects.all().prefetch_related('productos')

class EmbarqueDetailView(DetailView):
    model = Embarque
    template_name = 'productos/embarque_detalle.html'

class EmbarqueCreateView(CreateView):
    model = Embarque
    form_class = EmbarqueForm
    template_name = 'productos/embarque_form.html'
    success_url = reverse_lazy('productos:embarque_lista')

class EmbarqueUpdateView(UpdateView):
    model = Embarque
    form_class = EmbarqueForm
    template_name = 'productos/embarque_form.html'
    success_url = reverse_lazy('productos:embarque_lista')

class EmbarqueDeleteView(DeleteView):
    model = Embarque
    template_name = 'productos/embarque_confirm_delete.html'
    success_url = reverse_lazy('productos:embarque_lista')