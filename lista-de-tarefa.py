import json

lista = []

def salvar_contato():
    with open('tarefas.json', 'w', encoding= 'utf-8') as arquivo:
        json.dump(lista, arquivo, indent= 4)

def carregar_contato():
    global lista

    try:
        with open('tarefas,json', 'r', encoding='utf-8') as arquivo:
            lista = json.load(arquivo)
    except FileNotFoundError:
        lista = []

def add_tarefa(tarefa):
    tarefa = tarefa.split().lower()

    if not tarefa:
        print("Tarefa inválida")
        return

    for tarefas in lista:
        if tarefas['Tarefa'] == tarefa:
            print("Tarefa existente.")
            return


    tarefas = {'Tarefa': tarefa, 'Concluído': False}
    lista.append(tarefas)
    salvar_contato()
    print("Tarefa adicionada com sucesso")

def ver_lista(lista):
    if not lista:
        print("Lista vazia")
        return

    for t, tarefas in enumerate(lista, start=1):
        status = "★" if tarefas ['Favorito'] else ''
        print(f"{t}. {tarefas['Tarefa']} [{status}]")

def buscar_contato():


