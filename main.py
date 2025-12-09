import operacional as op
import os
os.system('cls' if os.name == 'nt' else 'clear')


def main():
    semana = op.cadastro_semanal()
    totais = op.resultado(semana)
    simulacao = op.simular_mensal_anual(totais[0])
    ideal = op.calcular_ideal()
    op.gerar_relatorio(semana, totais, simulacao, ideal)


if __name__ == "__main__":
    main()
