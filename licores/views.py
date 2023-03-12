
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import  reverse_lazy
from django.shortcuts import  redirect, render
import json
from django.db import transaction
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView,UpdateView,DeleteView

from licores.services import get_licor
from licores.forms import VentasForm
from licores.models import *
# Create your views here.


class SaleCreateView(CreateView):
    model = Venta
    form_class = VentasForm
    template_name = 'index.html'
    success_url = reverse_lazy('venta_create')
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']

            if action == 'search_autocomplete':
                data = []
                
                products = get_licor(request.POST['term'])                
                
                for i in products:
                    item = i.toJSON()
                    item['text'] = i.strDrink
                    data.append(item)
            elif action == 'add':
                with transaction.atomic():
                    vents = json.loads(request.POST['vents'])
                    venta = Venta()
                    venta.subtotal = float(vents['subtotal'])
                    venta.descuento = float(vents['descuento'])
                    venta.total = float(vents['total'])
                    venta.save()

                    for i in vents['productos']:
                        detalle = DetVenta()
                        detalle.venta_id = venta.id
                        detalle.producto_id = i['id']
                        detalle.cant = int(i['cant'])
                        detalle.precio = float(i['precio_venta'])
                        detalle.subtotal = float(i['subtotal'])
                        detalle.save()
                        cantidad_ActualP = Cocteles.objects.filter(pk = i['id']).values_list('cantidad_total',flat=True)
                        cantidad_ActualP = int(cantidad_ActualP[0])
                        cantidad_ActualP = cantidad_ActualP - detalle.cant
                        Cocteles.objects.filter(id = i['id']).update(cantidad_total = cantidad_ActualP)
            
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de una Venta'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['detalle'] = []

        return context

