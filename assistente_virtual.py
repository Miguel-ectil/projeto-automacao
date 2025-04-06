# Projeto: Assistente Virtual Automatizado com Python
# Participantes:
# - Miguel Ectil (Desenvolvedor Principal)
# - RA : 2301985
# - Luiza Cristina Gonçalves Matias (Colaborador)
# - RA : 2400797

import pandas as pd
import pyautogui
import time
import json
from datetime import datetime
from openpyxl import Workbook

def carregar_posicoes():
    try:
        with open('posicoes.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def salvar_posicao(nome):
    global posicoes
    print(f"[INFO] Mova o mouse para a posição de '{nome}' em 5 segundos...")
    time.sleep(5)
    pos = pyautogui.position()
    posicoes[nome] = (pos.x, pos.y)
    with open('posicoes.json', 'w') as f:
        json.dump(posicoes, f)

def executar_tarefa(tarefa, tipo, dado):
    try:
        tipo = tipo.strip().lower()
        dado = str(dado).strip()

        if tipo == 'click':
            if dado not in posicoes:
                salvar_posicao(dado)
            x, y = posicoes[dado]
            pyautogui.click(x, y)
            time.sleep(1)

        elif tipo == 'texto':
            pyautogui.hotkey('alt', 'tab')
            time.sleep(1)
            pyautogui.write(dado, interval=0.1)

        elif tipo == 'tecla':
            if '+' in dado:
                teclas = [k.strip() for k in dado.split('+')]
                pyautogui.hotkey(*teclas)
            else:
                pyautogui.press(dado)

        elif tipo == 'espera':
            time.sleep(int(dado))

        else:
            return f"Tipo de tarefa desconhecido: {tipo}"

        return "Executada com sucesso"

    except Exception as e:
        return f"Erro: {str(e)}"

def gerar_relatorio(logs):
    wb = Workbook()
    ws = wb.active
    ws.append(['Tarefa', 'Tipo', 'Dado', 'Status', 'Horário'])

    for log in logs:
        ws.append(log)

    wb.save('relatorio.xlsx')
    print("📄 Relatório salvo como relatorio.xlsx")

def main():
    df = pd.read_csv("tarefas.csv")
    logs = []

    for _, linha in df.iterrows():
        tarefa = str(linha["Tarefa"]).strip()
        tipo = str(linha["Tipo"]).strip()
        dado = linha["Dado"]

        print(f"[EXECUTANDO] {tarefa} ({tipo}) -> {dado}")
        status = executar_tarefa(tarefa, tipo, dado)
        horario = datetime.now().strftime("%H:%M:%S")
        logs.append([tarefa, tipo, dado, status, horario])

    gerar_relatorio(logs)
    print("✅ Execução finalizada com sucesso.")

if __name__ == "__main__":
    posicoes = carregar_posicoes()
    main()
