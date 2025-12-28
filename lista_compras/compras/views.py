from django.shortcuts import render, redirect
from .models import Item

# Create your views here.
def lista_compras(request):
    itens = Item.objects.all()

    #Se o usuario enviou um formulario do tipo POST.
    if request.method == 'POST':
        nome = request.POST.get('nome') #pega o valor digitado no formulario(pagina html) pelo usuario.
        if nome: #Se foi colocado algum nome no formulario, ele será craido e depois a pagina sera redirecionada para lista.
            Item.objects.create(nome=nome)
            return redirect('lista')
    
    return render(request, 'compras/lista.html', {'itens': itens}) 

def marcar_comprado(request, item_id):
    item = Item.objects.get(id=item_id) #item recebe o valor do id passado na pagina html atraves do get.
    item.comprado = not item.comprado #muda a situação do item.comprado, se for False muda para True.
    item.save() #salva a alteração feita no banco de dados.
    return redirect('lista') #apos salvar ele redireciona para a pagina lista(que a pagina inicial)

#Recebe da requiseção o item/id escolhido e acessa o medel fazendo a exclusão do item.
def deletar_item(request, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()
    return redirect('lista')