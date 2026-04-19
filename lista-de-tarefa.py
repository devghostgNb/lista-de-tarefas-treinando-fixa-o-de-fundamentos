import json

lista = []

def salvar_contato():
    with open('tarefas.json', 'w', encoding= 'utf-8') as arquivo:
        json.dump(lista, arquivo, indent= 4)

def carregar_contato():
    global lista

    try:
        with open('tarefas.json', 'r', encoding='utf-8') as arquivo:
            lista = json.load(arquivo)
    except FileNotFoundError:
        lista = []

def add_tarefa(tarefa):

    tarefa = tarefa.strip().lower()

    if not tarefa:
        print("Tarefa inválida")
        return

    for tarefas in lista:
        if tarefas['Tarefa'] == tarefa:
            print("Tarefa existente.")
            return


    tarefas = {'Tarefa': tarefa, 'Concluido': False}
    lista.append(tarefas)
    salvar_contato()
    print("Tarefa adicionada com sucesso")

def ver_lista(lista):
    if not lista:
        print("Lista vazia")
        return

    for t, tarefas in enumerate(lista, start=1):
        status = "★" if tarefas ['Concluido'] else ''
        print(f"{t}. {tarefas['Tarefa']} [{status}]")

def buscar_tarefa(tarefa):
    if not lista:
        print("Lista vazia.")
        return

    tarefa = tarefa.strip().lower()

    if not tarefa:
        print("Tarefa inválida.")
        return

    for item in lista:
        if tarefa in item['Tarefa']:
            status = "★" if item.get('Concluido', False) else ""
            print(f"Tarefa encontrada: {item['Tarefa']} [{status}]")
            return
    else:
        print("Tarefa não encontrada.")

def concluir_tarefa(lista, indice):
    indice = int(indice) - 1

    if indice < 0 or indice >= len(lista):
        print("Índice inválido.")
        return

    lista [indice] ['Concluido'] = True
    print(f"Tarefa {lista[indice]['Tarefa']} foi concluída.")
    salvar_contato()

def desmarcar_concluir(lista, indice):
    indice = int(indice) - 1

    if indice < 0 or indice >= len(lista):
        print("Índice inválido.")
        return

    lista [indice] ['Concluido'] = False
    print(f"Tarefa {lista[indice]['Tarefa']} não concluída.")
    salvar_contato()

def editar_tarefa(indice, novo_nome):
    if not lista:
        print("Lista vazia.")
        return

    novo_nome = novo_nome.strip().lower()

    indice -= 1

    if indice < 0 or indice >= len(lista):
        print("Tarefa não existe.")
        return

    for t, tarefas in enumerate(lista):
        if t != indice and tarefas['Tarefa'] == novo_nome:
            print("Nome existente.")
            return

    antiga = lista[indice]['Tarefa']
    lista[indice]['Tarefa'] = novo_nome
    salvar_contato()
    print(f"Tarefa {antiga} atualizada para: {novo_nome}")

def deletar_tarefa(indice):
    if not lista:
        print("Lista vazia.")
        return

    indice -= 1

    if indice < 0 or indice >= len(lista):
        print("Tarefa não existe.")
        return

    removido = lista[indice]
    confirmar = input(f"Tem certeza que deseja deletar a tarefa {removido['Tarefa']}? (s/n)").lower().strip()

    if confirmar not in ('s', 'n'):
        print("Opção inválida.")
        return

    if confirmar == 's':
        removido = lista.pop(indice)
        print(f"Tarefa '{removido['Tarefa']}' deletada com sucesso.")

    else:
        print("Exclusão cancelada.")

    salvar_contato()

carregar_contato()

while True:
    print("\n1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Buscar tarefas")
    print("4. Marcar conclusão")
    print("5. Desmarcar conclusão")
    print("6. Editar tarefa")
    print("7. Deletar tarefa")
    print("8. Sair")

    try:
        escolha = int(input("Digite o número que deseja acessar:"))

        if escolha == 1:
            tarefa = input("Digite o nome da tarefa que deseja adicionar:")
            add_tarefa(tarefa)

        elif escolha == 2:
            ver_lista(lista)

        elif escolha == 3:
            buscar = input("Digite a tarefa que deseja encontrar:")
            buscar_tarefa(buscar)

        elif escolha == 4:
            indice = int(input("Digite o indice do contato que deseja favoritar:"))
            concluir_tarefa(lista, indice)

        elif escolha == 5:
            indice = int(input("Digite o indice do contato que deseja desfavoritar:"))
            desmarcar_concluir(lista, indice)

        elif escolha == 6:
            indice = int(input("Digite o indice da tarefa que deseja editar:"))
            novo_nome = input("Digite o novo nome da tarefa:")
            editar_tarefa(indice, novo_nome)

        elif escolha == 7:
            indice = int(input("Digite o indice da tarefa que deseja deletar:"))
            deletar_tarefa(indice)

        elif escolha == 8:
            print("Programa finalizado.")
            break

        else:
            print("Escolha inválida.")

    except ValueError:
        print("Digite uma escolha válida de 1 a 8.")
