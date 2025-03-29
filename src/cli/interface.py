
from typing import Callable, Optional

from ..core.models import TaskList


def get_user_input(
    prompt: str,
    validation_func: Callable[[str], bool] = lambda x: True,
    error_msg: str = "Entrada inválida",
) -> Optional[str]:
    """Obtém entrada do usuário com validação."""
    while True:
        try:
            user_input = input(prompt)
            if validation_func(user_input):
                return user_input
            print(error_msg)
        except (EOFError, KeyboardInterrupt):
            print("\nOperação cancelada.")
            return None
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return None


def display_tasks(task_list: TaskList) -> None:
    """Exibe a lista de tarefas formatada."""
    if not task_list:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\nLISTA DE TAREFAS:")
    for task in task_list:
        print(
            f"{task['id']}. [{'X' if task['completed'] else ' '}] {task['description']}"
        )


def display_stats(stats: dict) -> None:
    """Exibe estatísticas das tarefas."""
    print("\nESTATÍSTICAS:")
    print(f"Total de tarefas: {stats['total_tasks']}")
    print(f"Concluídas: {stats['completed_tasks']}")
    print(f"Pendentes: {stats['pending_tasks']}")
    print(f"Percentual concluído: {stats['completion_percentage']:.1f}%")

