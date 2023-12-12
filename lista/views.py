from django.shortcuts import render, redirect
from .models import Item

def home(request):
    itens = Item.objects.all()
    return render(request, "index.html", {"itens": itens})

def salvar(request):
    vnome = request.POST.get("nome")
    vvalor = request.POST.get("valor")
    Item.objects.create(nome=vnome, valor=vvalor)
    itens = Item.objects.all()
    return render(request, "index.html", {"itens": itens})



def editar(request, id):
    item = Item.objects.get(id=id)
    return render(request, "uptade.html", {"item": item})

def uptade(request, id):
    vnome = request.POST.get("nome")
    item = Item.objects.get(id=id)
    item.nome = vnome
    item.save()
    return redirect(home)

def delete(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return redirect(home)