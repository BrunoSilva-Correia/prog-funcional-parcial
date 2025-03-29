### **Utilização de Chatbot**

- Criação do README
- Inserção das DocStrings, para facilitar a leitura do código.
- Foi utilizado o DeepSeek para montagem da matriz de requisitos funcionais e não funcionais, onde o output foram as tabelas de requisitos (./funcional.md e ./non-functional.md).
- Utilizado para ajuda da melhor estruturação de pastas para o projeto, onde o output foi:

```
│
├── src/
│   ├── _init_.py
│   ├── core/
│   │   ├── _init_.py
│   │   ├── tasks.py
│   │   └── models.py
│   │
│   └── cli/
│       ├── _init_.py
│       ├── interface.py
│       └── menu.py
│
├── tests/
│   ├── _init_.py
│   ├── unit/
│   │   ├── _init_.py
│   │   ├── test_core.py
│   │   └── test_cli.py
│
├── docs/
│   ├── requirements/
│   │   ├── functional.md
│   │   └── non-functional.md
│   │
│   ├── design/
│   │   └── functional.md
│
├── .gitignore
├── README.md
```
