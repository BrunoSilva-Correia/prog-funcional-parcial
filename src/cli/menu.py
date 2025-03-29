from typing import NoReturn

from ..core.models import TaskList
from ..core.tasks import (
    add_task,
    complete_task,
    delete_task,
    filter_tasks,
    task_statistics,
    update_task_description,
)
from .interface import display_stats, display_tasks, get_user_input


def show_menu() -> None:
    """Exibe o menu de opções."""
    menu_items = [
        "1. Adicionar nova tarefa",
        "2. Listar todas as tarefas",
        "3. Marcar tarefa como concluída",
        "4. Deletar tarefa",
        "5. Atualizar descrição da tarefa",
        "6. Filtrar tarefas (pendentes/concluídas)",
        "7. Mostrar estatísticas",
        "8. Sair",
    ]

    print("\n" + "=" * 50)
    print("MENU DE GERENCIAMENTO DE TAREFAS")
    print("=" * 50)
    print("\n".join(menu_items))
    print("=" * 50)


def handle_menu_choice(choice: str, tasks: TaskList) -> TaskList:
    """Processa a escolha do menu e retorna a lista atualizada."""
    if choice == "1":
        description = get_user_input(
            "Digite a descrição da nova tarefa: ", lambda x: len(x.strip()) > 0
        )
        return add_task(tasks, description) if description else tasks

    elif choice == "2":
        display_tasks(tasks)
        return tasks

    elif choice == "3":
        display_tasks(tasks)
        task_id = get_user_input(
            "Digite o ID da tarefa a marcar como concluída: ",
            lambda x: x.isdigit() and any(task["id"] == int(x) for task in tasks),
        )
        return complete_task(tasks, int(task_id)) if task_id else tasks

    elif choice == "4":
        display_tasks(tasks)
        task_id = get_user_input(
            "Digite o ID da tarefa a ser deletada: ",
            lambda x: x.isdigit() and any(task["id"] == int(x) for task in tasks),
        )
        return delete_task(tasks, int(task_id)) if task_id else tasks

    elif choice == "5":
        display_tasks(tasks)
        task_id = get_user_input(
            "Digite o ID da tarefa a atualizar: ",
            lambda x: x.isdigit() and any(task["id"] == int(x) for task in tasks),
        )
        if task_id:
            new_desc = get_user_input(
                "Digite a nova descrição: ", lambda x: len(x.strip()) > 0
            )
            return (
                update_task_description(tasks, int(task_id), new_desc)
                if new_desc
                else tasks
            )
        return tasks

    elif choice == "6":
        filter_choice = get_user_input(
            "Filtrar por: (1) Pendentes (2) Concluídas (3) Todas: ",
            lambda x: x in ["1", "2", "3"],
        )
        if filter_choice:
            status_filter = None if filter_choice == "3" else (filter_choice == "2")
            filtered = filter_tasks(tasks, status_filter)
            display_tasks(filtered)
        return tasks

    elif choice == "7":
        stats = task_statistics(tasks)
        display_stats(stats)
        return tasks

    return tasks


def main_loop() -> NoReturn:
    """Loop principal da aplicação."""
    tasks: TaskList = []

    while True:
        show_menu()
        choice = get_user_input(
            "Escolha uma opção (1-8): ", lambda x: x.isdigit() and 1 <= int(x) <= 8
        )

        if not choice:
            continue

        if choice == "8":
            print("Saindo do sistema...")
            break

        tasks = handle_menu_choice(choice, tasks)


if __name__ == "__main__":
    print("Sistema de Gerenciamento de Tarefas")
    main_loop()
