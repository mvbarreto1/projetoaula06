def adicionar_tarefa(tarefas, nome, descricao, prioridade, categoria):
    id_tarefa = len(tarefas) + 1
    tarefa = {
        "id": id_tarefa,
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "concluida": False
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{nome}' adicionada com sucesso!")


def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    for tarefa in tarefas:
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"[{tarefa['id']}] {tarefa['nome']} - Prioridade: {tarefa['prioridade']} - {status}")


def marcar_concluida(tarefas, id_tarefa):
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefa["concluida"] = True
            print(f"Tarefa '{tarefa['nome']}' marcada como concluída!")
            return
    print("Tarefa não encontrada!")


def exibir_por_prioridade(tarefas, prioridade):
    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa["prioridade"] == prioridade]
    if not tarefas_filtradas:
        print(f"Nenhuma tarefa encontrada com a prioridade {prioridade}.")
        return
    for tarefa in tarefas_filtradas:
        print(f"[{tarefa['id']}] {tarefa['nome']} - {tarefa['descricao']} - Status: {'Concluída' if tarefa['concluida'] else 'Pendente'}")


def exibir_por_categoria(tarefas, categoria):
    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa["categoria"].lower() == categoria.lower()]
    if not tarefas_filtradas:
        print(f"Nenhuma tarefa encontrada na categoria '{categoria}'.")
        return
    for tarefa in tarefas_filtradas:
        print(f"[{tarefa['id']}] {tarefa['nome']} - {tarefa['descricao']} - Status: {'Concluída' if tarefa['concluida'] else 'Pendente'}")


def exibir_menu():
    print("\nMenu de Tarefas:")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Exibir tarefas por prioridade")
    print("5. Exibir tarefas por categoria")
    print("6. Sair")


def main():
    tarefas = [
        {"id": 1, "nome": "Lavar a louça", "descricao": "Lavar e secar a louça de ontem", "prioridade": 2, "categoria": "Domestica", "concluida": False},
        {"id": 2, "nome": "Ir para academia", "descricao": "Malhar peito e triceps", "prioridade": 1, "categoria": "Saúde", "concluida": False},
        {"id": 3, "nome": "Estudar py", "descricao": "Revisar funções e dicionários", "prioridade": 3, "categoria": "Educação", "concluida": False},
        {"id": 4, "nome": "Caminhar", "descricao": "Ir até a esquina e voltar", "prioridade": 1, "categoria": "Saúde", "concluida": False}
    ]

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome da tarefa: ")
            descricao = input("Descrição da tarefa: ")
            prioridade = int(input("Prioridade (1, 2, 3): "))
            categoria = input("Categoria: ")
            adicionar_tarefa(tarefas, nome, descricao, prioridade, categoria)

        elif escolha == "2":
            listar_tarefas(tarefas)

        elif escolha == "3":
            id_tarefa = int(input("Digite o ID da tarefa a ser marcada como concluída: "))
            marcar_concluida(tarefas, id_tarefa)

        elif escolha == "4":
            prioridade = int(input("Digite a prioridade para filtrar (1, 2, 3): "))
            exibir_por_prioridade(tarefas, prioridade)

        elif escolha == "5":
            categoria = input("Digite a categoria para filtrar: ")
            exibir_por_categoria(tarefas, categoria)

        elif escolha == "6":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()