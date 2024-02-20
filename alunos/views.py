from django.shortcuts import render, redirect
from .forms import AlunoForm
from .models import Aluno

def adicionar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alunos')
    else:
        form = AlunoForm()
    return render(request, 'adicionar_aluno.html', {'form': form})

def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'lista_alunos.html', {'alunos': alunos})