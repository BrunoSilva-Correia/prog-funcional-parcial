# Conceitos de Programação Funcional Implementados

## 1. Funções de Alta Ordem

**Onde**: Função `process_tasks` em `src/core/tasks.py`  
**Como**: Recebe uma função como parâmetro e aplica a todas as tarefas

## 2. Closures

**Onde**: Função `create_task_completer` em `src/core/tasks.py`  
**Como**: Retorna uma função que mantém acesso ao escopo da função externa

## 3. Funções Lambda

**Onde**: Variável `format_task` em `src/core/tasks.py`  
**Como**: Função anônima para formatação de strings

## 4. List Comprehensions

**Onde**: Função `filter_tasks` em `src/core/tasks.py`  
**Como**: Filtra listas de forma declarativa

## 5. Imutabilidade

**Como**: Todas as funções retornam novas estruturas em vez de modificar as existentes
