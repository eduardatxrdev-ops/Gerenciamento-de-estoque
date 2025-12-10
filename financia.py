import os
os.system("cls")


class Despesas:
    def __init__(self, descricao, categoria, valor):
        self.descricao = descricao
        self.categoria = categoria
        self.valor = valor
        
        if categoria == "Salário":                                   # Regra do imposto
            self.imposto = valor * 0.08                               # 8% apenas para salário
        else:
            self.imposto = valor * 0.15                               # 15% para o resto

class Veiculo:
    def __init__(self, modelo, ano, custo_fabricacao):
        self.modelo = modelo
        self.ano = ano
        self.custo_fabricacao = custo_fabricacao                     # custo direto de produção

class ControleEmpresa:
    def __init__(self):
        self.despesas = []                                           # lista de despesas e salários
        self.veiculos = []                                           # lista de veículos produzidos
        self.vendas = []                                             # lista de vendas
        self.despesas_fixas = 0                                      # despesas fixas adicionadas aqui
        self.total_produzido = 0                                     # total de carros produzidos
    
    def adicionar_despesa(self, despesa):                            # despesas gerais
        self.despesas.append(despesa)

    def listar_despesas(self):
        if self.despesas:
            print("\n--- Lista de Despesas ---")
            for index, despesa in enumerate(self.despesas, start=1):
                print(f"{index}. {despesa.descricao} - {despesa.categoria} - R${despesa.valor:.2f} (Imposto: R${despesa.imposto:.2f})")
        else:
            print("Nenhuma despesa registrada.")

    def listar_funcionarios(self):                                  # funcionários
        funcionarios = [d for d in self.despesas if d.categoria == "Salário"]
        if not funcionarios:
            print("Nenhum funcionário cadastrado.")
        else:
            for i, f in enumerate(funcionarios, start=1):
                print(f"{i}. {f.descricao} - R${f.valor:.2f}")
        return funcionarios

    def excluir_funcionario(self, index):
        funcionarios = [d for d in self.despesas if d.categoria == "Salário"]
        if 0 <= index < len(funcionarios):
            funcionario = funcionarios[index]
            self.despesas.remove(funcionario)
            print(f"Funcionário {funcionario.descricao} removido com sucesso!")
        else:
            print("Índice inválido.")

    def adicionar_veiculo(self, veiculo):                            # veículos
        self.veiculos.append(veiculo)
        self.total_produzido += 1                                     # Conta o total produzido

    def listar_veiculos(self):
        if not self.veiculos:
            print("Nenhum veículo cadastrado.")
        else:
            print("\n--- Veículos Produzidos ---")
            total_veiculos = len(self.veiculos)
            despesa_fixa_por_carro = self.despesas_fixas / total_veiculos if total_veiculos > 0 else 0

            for i, v in enumerate(self.veiculos, start=1):
                custo_total_carro = v.custo_fabricacao + despesa_fixa_por_carro
                preco_venda_carro = custo_total_carro * 1.5  # 50% de lucro
                print(f"{i}. {v.modelo} ({v.ano})")
                print(f"   Custo Fabricação: R${v.custo_fabricacao:.2f}")
                print(f"   Custo Total por Carro (incluindo despesas fixas): R${custo_total_carro:.2f}")
                print(f"   Preço Sugerido de Venda: R${preco_venda_carro:.2f}")

    def calcular_custo_total_producao(self):                         # custo de fabricação + despesas fixas
        custo_fabr = sum(v.custo_fabricacao for v in self.veiculos)
        custo_total = custo_fabr + self.despesas_fixas
        return custo_total

    def calcular_custo_por_carro(self):
        if self.total_produzido == 0:
            return 0
        return self.calcular_custo_total_producao() / self.total_produzido

    def calcular_preco_venda(self):                                   # Preço com 50% de lucro
        custo_unitario = self.calcular_custo_por_carro()
        return custo_unitario * 1.5

if __name__ == "__main__":                                           # programa principal
    controle = ControleEmpresa()

    while True:
        print("\n=== Menu da Empresa de ShockCar ===")
        print("1. Adicionar Despesa")
        print("2. Funcionários")
        print("3. Produção de Veículos")
        print("4. Consultar Custos e Preços")
        print("5. Listar Despesas")
        print("6. Listar Veículos")
        print("7. Sair")
        escolha = input("\nEscolha uma opção: ")

        if escolha == '1':                                          # despesa
            descricao = input("Descrição da Despesa: ")
            valor = float(input("Valor da Despesa: R$"))
            categoria = input("Categoria (Salário ou Despesa): ")
            despesa = Despesas(descricao, categoria, valor)
            controle.adicionar_despesa(despesa)
            if categoria != "Salário":
                controle.despesas_fixas += valor
            print("Despesa adicionada com sucesso!")

        elif escolha == '2':
            while True:
                print("\n--- Menu Funcionários ---")
                print("1. Adicionar Funcionário")
                print("2. Excluir Funcionário")
                print("3. Listar Funcionários")
                print("4. Voltar")
                opc = input("Escolha uma opção: ")

                if opc == '1':
                    descricao = input("Nome do Funcionário: ")
                    valor = float(input("Salário do Funcionário: R$"))
                    desp = Despesas(descricao, "Salário", valor)
                    controle.adicionar_despesa(desp)
                    print("Funcionário adicionado!")

                elif opc == '2':
                    funcionarios = controle.listar_funcionarios()
                    if funcionarios:
                        try:
                            idx = int(input("Digite o número do funcionário a excluir: ")) - 1
                            controle.excluir_funcionario(idx)
                        except ValueError:
                            print("Digite apenas números válidos.")

                elif opc == '3':
                    controle.listar_funcionarios()

                elif opc == '4':
                    break

                else:
                    print("Opção inválida.")

        elif escolha == '3':                                        # produção de veículos
            while True:
                print("\n--- Menu Produção de Veículos ---")
                print("1. Adicionar Veículo")
                print("2. Listar Veículos")
                print("3. Voltar")
                opc = input("Escolha uma opção: ")

                if opc == '1':
                    modelo = input("Modelo do Veículo: ")
                    ano = input("Ano do Veículo: ")
                    custo = float(input("Custo de Fabricação: R$"))
                    veic = Veiculo(modelo, ano, custo)
                    controle.adicionar_veiculo(veic)
                    print("Veículo adicionado com sucesso!")

                elif opc == '2':
                    controle.listar_veiculos()

                elif opc == '3':
                    break

                else:
                    print("Opção inválida.")

        elif escolha == '4':
            custo_total = controle.calcular_custo_total_producao()                      # cálculo custo total produção
            custo_por_carro = controle.calcular_custo_por_carro()                       # cálculo custo por carro
            preco_venda = controle.calcular_preco_venda()                               # preço com 50% de lucro

            print("\n--- Custos e Preço de Venda ---")
            print(f"Despesas Fixas: R${controle.despesas_fixas:.2f}")                   # despesas fixas
            print(f"Total Produzido: {controle.total_produzido}")
            print(f"Custo Total de Produção: R${custo_total:.2f}")                      # custo total produção
            print(f"Custo por Carro: R${custo_por_carro:.2f}")                          # custo por carro
            print(f"Preço de Venda Sugerido (+50% lucro): R${preco_venda:.2f}")         # preço de venda

        elif escolha == '5':
            controle.listar_despesas()

        elif escolha == '6':
            controle.listar_veiculos()

        elif escolha == '7':
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida.")
