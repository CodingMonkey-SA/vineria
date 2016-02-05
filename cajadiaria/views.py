from django.shortcuts import render
from cajadiaria.models import CajaDiaria
from products.models import Venta, VentaProducto
from django.db.models import Q
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import Http404
import json
from django.db.models import Sum

def abrircaja(request):
	caja = CajaDiaria()
	valorinicial = request.GET['saldo']
	caja.saldoinicial = valorinicial
	caja.usuario = request.user
	caja.save()
	return render(request, 'products/home.html', {})

def cerrarcaja(request):
	id_caja =  CajaDiaria.objects.filter(~Q(saldoinicial = 0), saldofinal=0).values('id')
	caja = CajaDiaria.objects.get(id=id_caja[0].get('id'))
	id_venta = Venta.objects.filter(fecha__gte=caja.fecha)
	sum = 0
	for venta in id_venta:
		sum+= venta.total
	print caja.saldoinicial
	caja.saldofinal = sum
	print caja.saldofinal
	caja.save()
	balance = {'balance':(float(caja.saldofinal) + float(caja.saldoinicial))}
	return HttpResponse(json.dumps(balance), content_type='application/json')

def cajaabierta(request):
	caja =  CajaDiaria.objects.filter(~Q(saldoinicial = 0), saldofinal=0).values('id')
	if caja.count()>0:
		return HttpResponse({},'')
	else:
		raise Http404("")
