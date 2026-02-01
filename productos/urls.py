from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    # URLs de Productos
    path('', views.lista_productos, name='lista_productos'),
    path('producto/nuevo/', views.ProductoCreateView.as_view(), name='producto_crear'),
    path('producto/<int:pk>/', views.ProductoDetailView.as_view(), name='producto_detalle'),
    path('producto/<int:pk>/editar/', views.ProductoUpdateView.as_view(), name='producto_editar'),
    path('producto/<int:pk>/eliminar/', views.ProductoDeleteView.as_view(), name='producto_eliminar'),

    # URLs de Embarques
    path('embarques/', views.EmbarqueListView.as_view(), name='embarque_lista'),
    path('embarques/nuevo/', views.EmbarqueCreateView.as_view(), name='embarque_crear'),
    path('embarques/<int:pk>/', views.EmbarqueDetailView.as_view(), name='embarque_detalle'),
    path('embarques/<int:pk>/editar/', views.EmbarqueUpdateView.as_view(), name='embarque_editar'),
    path('embarques/<int:pk>/eliminar/', views.EmbarqueDeleteView.as_view(), name='embarque_eliminar'),
]
