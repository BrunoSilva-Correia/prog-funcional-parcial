### **Requisitos Não Funcionais**

| ID    | Descrição                                                                              | Implementação                                                |
| ----- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| RNF01 | Programação Funcional: Uso de paradigma funcional (imutabilidade, funções puras, etc.) | Implementado em todas as funções do `core/tasks.py`          |
| RNF02 | Desempenho: Operações devem ser O(n) no pior caso                                      | Uso de list comprehensions e funções otimizadas              |
| RNF03 | Usabilidade: Interface CLI intuitiva com tratamento de erros                           | Validações em `get_user_input()` e menus em `cli/menu.py`    |
| RNF04 | Manutenibilidade: Código modular e documentado                                         | Separação em `core/` e `cli/`, docstrings e tipagem estática |
| RNF05 | Testabilidade: Cobertura de testes > 90%                                               | Suíte de testes em `tests/unit/`                             |
| RNF06 | Extensibilidade: Facilidade para adicionar novas funcionalidades                       | Arquitetura em camadas e funções de alta ordem               |

---
