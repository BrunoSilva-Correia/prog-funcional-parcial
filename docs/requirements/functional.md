### **Requisitos Funcionais**

| ID   | Descrição                                                      | Implementação                                                   |
| ---- | -------------------------------------------------------------- | --------------------------------------------------------------- |
| RF01 | Adicionar nova tarefa à lista                                  | `add_task()` em `core/tasks.py`                                 |
| RF02 | Listar todas as tarefas                                        | `display_tasks()` em `cli/interface.py`                         |
| RF03 | Marcar tarefa como concluída                                   | `complete_task()` e `toggle_task_status()` em `core/tasks.py`   |
| RF04 | Deletar tarefa                                                 | `delete_task()` em `core/tasks.py`                              |
| RF05 | Atualizar descrição da tarefa                                  | `update_task_description()` em `core/tasks.py`                  |
| RF06 | Filtrar tarefas por status (concluídas/pendentes)              | `filter_tasks()` e `group_tasks_by_status()` em `core/tasks.py` |
| RF07 | Buscar tarefas por termo na descrição                          | `search_tasks()` em `core/tasks.py`                             |
| RF08 | Exibir estatísticas (total, concluídas, pendentes, percentual) | `task_statistics()` em `core/tasks.py`                          |
| RF09 | Visualizar detalhes completos de uma tarefa                    | `display_task_details()` em `cli/interface.py`                  |
| RF10 | Alternar status de conclusão (marcar/desmarcar)                | `toggle_task_status()` em `core/tasks.py`                       |
| RF11 | Registrar histórico de modificações                            | `create_task_modifier()` (closure) em `core/tasks.py`           |
