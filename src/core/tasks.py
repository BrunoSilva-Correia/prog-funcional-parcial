from typing import Callable

from .models import Task, TaskList


# Função de alta ordem - Recebe uma função como parâmetro
def process_tasks(tasks: TaskList, processing_func: Callable[[Task], Task]) -> TaskList:
    """Aplica uma função de processamento a todas as tarefas."""
    return list(map(processing_func, tasks))


# Closure - Função que retorna outra função com acesso a variáveis do escopo externo
def create_task_completer():
    """Factory para criar funções que completam tarefas."""
    completed_ids = set()

    def complete_task(task: Task, task_id: int) -> Task:
        if task["id"] == task_id:
            completed_ids.add(task_id)
            return {**task, "completed": True}
        return task

    return complete_task


def add_task(task_list: TaskList, description: str) -> TaskList:
    """Adiciona uma nova tarefa à lista."""
    new_id = max(task["id"] for task in task_list) + 1 if task_list else 1
    new_task: Task = {"id": new_id, "description": description, "completed": False}
    return [*task_list, new_task]


def delete_task(task_list: TaskList, task_id: int) -> TaskList:
    """Remove uma tarefa da lista."""
    return [task for task in task_list if task["id"] != task_id]


def update_task_description(
    task_list: TaskList, task_id: int, new_description: str
) -> TaskList:
    """Atualiza a descrição de uma tarefa."""
    return process_tasks(
        task_list,
        lambda task: (
            {**task, "description": new_description} if task["id"] == task_id else task
        ),
    )


# List comprehension - Para filtrar tarefas
def filter_tasks(task_list: TaskList, completed: bool = None) -> TaskList:
    """Filtra tarefas por status."""
    if completed is None:
        return task_list
    return [task for task in task_list if task["completed"] == completed]


def task_statistics(task_list: TaskList) -> dict:
    """Calcula estatísticas das tarefas."""
    total = len(task_list)
    completed = sum(1 for task in task_list if task["completed"])
    return {
        "total_tasks": total,
        "completed_tasks": completed,
        "pending_tasks": total - completed,
        "completion_percentage": (completed / total * 100) if total > 0 else 0,
    }


def complete_task(task_list, task_id):
    """Marca uma tarefa como concluída."""
    completer = create_task_completer()
    return process_tasks(task_list, lambda task: completer(task, task_id))


# Função lambda - Função anônima para formatar saída
format_task = (
    lambda task: f"{task['id']}. [{'X' if task['completed'] else ' '}] {task['description']}"
)
