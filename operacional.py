#CARLOS DOS SANTOS BATISTA - 2025

def cadastro_semanal():
    semana = []
    turnos = ["manhã", "tarde", "noite"]

    print("\n\033[4m \033[36m \033[1m CADASTRO DE PRODUÇÃO(7 DIAS)   \033[0m")

    for dia in range(1, 8):
        print(f"\n\033[4m \033[35m \033[1m Dia {dia}: \033[0m")
        producao = {}
        for turno in turnos:
            producao[turno] = int(input(f"\033[35m PRODUÇÃO NO TURNO {turno}: \033[0m"))
        semana.append(producao)

    return semana


def resultado(semana):
    total_semanal = 0
    soma_turnos = {"manhã": 0, "tarde": 0, "noite": 0}

    for dia in semana:
        for turno in soma_turnos:
            soma_turnos[turno] += dia[turno]
            total_semanal += dia[turno]

    media_diaria = total_semanal / 7
    media_por_turno = {t: soma_turnos[t] / 7 for t in soma_turnos}

    return total_semanal, media_diaria, media_por_turno


def simular_mensal_anual(total_semanal):
    mensal = total_semanal * 4  
    anual = total_semanal * 52  
    return mensal, anual


def calcular_ideal():
    capacidade_base = 500          
    capacidade_total = capacidade_base * 1.5  

    ideal_mensal = capacidade_total
    ideal_anual = ideal_mensal * 12
    ideal_semanal = ideal_mensal / 4

    return ideal_semanal, ideal_mensal, ideal_anual


def gerar_relatorio(semana, totais, simulacao, ideal):
    total_sem, media_dia, media_turno = totais
    mensal, anual = simulacao
    ideal_sem, ideal_mes, ideal_ano = ideal

    print("\n\033[4m \033[36m \033[1m   RELATÓRIO  \033[0m")

    print("\033[35m PRODUÇÃO SEMANAL:\033[0m")
    for i, dia in enumerate(semana, start=1):
        print(f"\033[36mDia \033[33m{i}\033[36m: {dia}\033[0m")

    print("\n\033[35m Totais e médias reais:\033[0m")
    print(f"\033[36mTotal semanal:\033[33m{total_sem}\033[0m")
    print(f"\033[36mMédia por dia: \033[33m{media_dia:.2f}\033[0m")
    print("\033[35m Média por turno:\033[0m")
    for t, m in media_turno.items():
        print(f"\033[36m{t}: \033[33m{m:.2f}\033[0m")
    print("\n\033[35m Simulação baseada na semana:\033[0m")
    print(f"\033[36mProdução mensal estimada: \033[33m{mensal}\033[0m")
    print(f"\033[36mProdução anual estimada : \033[33m{anual}\033[0m")

    print("\n\033[35m Produção ideal (100% da capacidade com 3 turnos):\033[0m")
    print(f"\033[36mIdeal semanal: \033[33m{ideal_sem:.2f}\033[0m")
    print(f"\033[36mIdeal mensal : \033[33m{ideal_mes:.2f}\033[0m")
    print(f"\033[36mIdeal anual  : \033[33m{ideal_ano:.2f}\033[0m")

    print("\n\033[35m Comparação real x ideal:\033[0m")
    print(f"\033[36mSemanal: \033[33m{total_sem - ideal_sem:.2f}\033[0m")
    print(f"\033[36mMensal : \033[33m{mensal - ideal_mes:.2f}\033[0m")
    print(f"\033[36mAnual  : \033[33m{anual - ideal_ano:.2f}\033[0m")

    print("\n\033[4m \n")
