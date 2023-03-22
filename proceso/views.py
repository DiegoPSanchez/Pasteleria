from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Pedido
from .forms import nPedidoForm
from django.utils import timezone


# Create your views here.
def pedidos(request):
    fpedido = Pedido.objects.order_by('-fecha').first()
    pedidos = Pedido.objects.order_by('-fecha').all()
    return render(request, 'pedidos.html', {'pedidos':pedidos, 'fpedido':fpedido})

def pedido(request, id):
    pedido = Pedido.objects.get(id=id)
    return render(request, 'pedido.html', {'pedido':pedido})

def nuevoPedido(request):
    if request.method == 'GET':
        return render(request, 'nuevoPedido.html', {'form':nPedidoForm})
    else:
        form =  nPedidoForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')  
        else:
            form=nPedidoForm()
            return render(request, 'nuevoPedido.html', {'form':form})

def editPedido(request, id):
    if request.method == 'GET':
        pedido = Pedido.objects.get(id=id)
        form = nPedidoForm(instance=pedido)
        return render(request, 'editPedido.html', {'form':form})
    else:
        try:
            pedido = Pedido.objects.get(id=id)
            form =  nPedidoForm(request.POST, request.FILES, instance=pedido)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')  
            else:
                form=nPedidoForm()
                return render(request, 'editPedido.html', {'form':form})
        except ValueError:
            return render(request, 'editPedido.html', {'form':form, 'error':"Error actualizando registro"})

def pendientes(request):
    pedidos = Pedido.objects.filter(estado__isnull=True).order_by('-fecha')
    return render(request, 'pendientes.html', {'pedidos':pedidos})

def completado(request, id):
    pedido = Pedido.objects.get(id=id)
    pedido.estado = timezone.now()
    pedido.save()
    print(pedido.estado)
    return redirect('pendientes')

def finalizados(request):
    pedidos = Pedido.objects.filter(estado__isnull=False).order_by('-fecha')
    return render(request, 'finalizados.html', {'pedidos':pedidos})  
