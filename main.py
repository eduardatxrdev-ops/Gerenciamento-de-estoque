import operacional as op
import estoque as es
import os

def menu_estoque():
    """Menu de gerenciamento de estoque."""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n=== Menu de Estoque ===")
        print("1 - Cadastrar insumo")
        print("2 - Listar insumos")
        print("3 - Registrar entrada")
        print("4 - Registrar saída")
        print("5 - Deletar insumo")
        print("6 - Custo mensal")
        print("7 - Custo semanal")
        print("8 - Custo anual")
        print("0 - Voltar ao menu principal")
        
        opc = input("\nEscolha uma opção: ").strip()
        
        if opc == "1":
            es.cadastrar_insumo()
        elif opc == "2":
            es.listar_insumos()
        elif opc == "3":
            es.registrar_entrada()
        elif opc == "4":
            es.registrar_saida()
        elif opc == "5":
            es.deletar_insumo()
        elif opc == "6":
            es.custo_mensal()
        elif opc == "7":
            es.custo_semanal()
        elif opc == "8":
            es.custo_anual()
        elif opc == "0":
            break
        else:
            print("Opção inválida.")
        
        input("\nPressione ENTER para continuar...")


def menu_operacional():
    """Menu de cadastro de produção (operacional)."""
    os.system('cls' if os.name == 'nt' else 'clear')
    semana = op.cadastro_semanal()
    totais = op.resultado(semana)
    simulacao = op.simular_mensal_anual(totais[0])
    ideal = op.calcular_ideal()
    op.gerar_relatorio(semana, totais, simulacao, ideal)


if __name__ == "__main__":
    main()
