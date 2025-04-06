# 🤖 AutoTaskBot

Projeto - RPA (Robotic Process Automation) com Python

## 📌 Descrição

Este projeto simula um assistente virtual automatizado utilizando Python. Ele é capaz de ler tarefas de um arquivo CSV, interpretar o tipo de ação e executá-la automaticamente, simulando as ações de um usuário no computador (como clicar em ícones, digitar, pressionar teclas, e esperar).

Foi desenvolvido para a disciplina de AP1 da Faculdade Impacta, com foco na aplicação prática de automação de processos.

---

## ⚙️ Tecnologias Utilizadas

- Python 3.13.2
- [pandas](https://pypi.org/project/pandas/)
- [openpyxl](https://pypi.org/project/openpyxl/)
- [pyautogui](https://pypi.org/project/pyautogui/)
- json
- csv

---

## 🚀 Funcionalidades

- 📄 Leitura de tarefas a partir de um arquivo CSV
- 🖱️ Automação de cliques e digitação
- ⌨️ Pressionar teclas e atalhos
- ⏱️ Aguardar intervalos de tempo
- 📌 Captura e reutilização de posições na tela
- 🧾 Geração de relatório de execução em Excel

---

## ▶️ Como Executar

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/AutoTaskBot.git
cd projeto-automacao
```

2. **Crie um ambiente virtual (opcional mas recomendado):**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
3. **Instale as dependências:**
```bash
pip install pandas openpyxl pyautogui
```

4. **Prepare seu arquivo de tarefas**
 
5. **Execute o arquivo assistente_virtual:**
```bash
python assistente_virtual.py:
```

--- 

## 📄 Licença

Este projeto está licenciado sob os termos da [Licença MIT](LICENSE).
