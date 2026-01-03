from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Lista_compras

# Create your views here.
def lista_compras(request, lista_id=0):
    lista = get_object_or_404(Lista_compras, id=lista_id) #lista recebe os objetos diretos da lista_compras pelo seu id, se nao encontrar ele exibe uma pagina de erro 404 automaticamente.
    itens = lista.itens.all().order_by('-criado_em') #itens recebe uma todos os itens da lista por ordem de cricação.

    #Se o usuario enviou um formulario do tipo POST.
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip() #pega o valor digitado no formulario(pagina html) pelo usuario.
        if nome: #Se foi colocado algum nome no formulario, ele será craido e depois a pagina sera redirecionada para lista.
            Item.objects.create(nome=nome, lista_id=lista_id)
            return redirect('lista_compras', lista_id=lista_id)
    
    return render(request, 'compras/lista.html', {'itens': itens, 'lista': lista}) 


#funçao para deletar uma lista criada.
def deletar_lista(request, lista_id):
    lista = get_object_or_404(Lista_compras, id=lista_id) #lista recebe a lista pelo id.
    lista.delete() #lista acessa o banco de dados para deletar usando o id que foi salvo em lista.
    return redirect('home')

"""def listas(request): #função para retornar todas as listas.
    listas = Lista_compras.objects.all().order_by('-criado_em') #listas vai receber de Listas_compras importadas do models, todos os objetos por ordem de criação('-criada_em')
    return render(request, 'compras/lista.html', {'listas': listas}) #retornando o caminho de onde esntão todas as listas."""

#funcao para criar uma nova lista.
def nova_lista(request):
    if request.method == 'POST': #se a requisição tiver o metodo post ele vai receber o nome informado no formulario.
        nome = request.POST.get('nome', '').strip()
        if nome: #Se tiver algum nome no formulario ele vai acionar o listas_compras do model e criar um nome para a lista.
            Lista_compras.objects.create(nome=nome)
            return redirect('home')
        
    return render(request, 'compras/nova_lista.html')

def home(request):
    listas = Lista_compras.objects.all()
    return render(request, 'compras/home.html', {'listas':listas})




# Recebe da requiseção o item/id escolhido e acessa o medel fazendo a exclusão do item.
def deletar_item(request, lista_id, item_id):
    item = get_object_or_404(Item, id=item_id, lista_id=lista_id)
    item.delete()
    return redirect('lista_compras', lista_id=lista_id)

def marcar_comprado(request, lista_id, item_id):
    item = get_object_or_404(Item, id=item_id, lista_id=lista_id)
    item.comprado = not item.comprado #muda a situação do item.comprado, se for False muda para True.
    item.save() #salva a alteração feita no banco de dados.
    return redirect('lista_compras', lista_id=lista_id) #apos salvar ele redireciona para a pagina lista(que a pagina inicial)

