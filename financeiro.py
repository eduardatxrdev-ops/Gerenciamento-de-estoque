#Robert Cefas Bispo Miranda
import os
import json   
os.system("cls")


class Despesas:
    def __init__(self, descricao, categoria, valor):
        self.descricao = descricao
        self.categoria = categoria
        self.valor = valor
        
        if categoria == "Salário":
            self.imposto = valor * 0.08
        else:
            self.imposto = valor * 0.15


class Veiculo:
    def __init__(self, modelo, ano, custo_fabricacao):
        self.modelo = modelo
        self.ano = ano
        self.custo_fabricacao = custo_fabricacao


class ControleEmpresa:
    def __init__(self):
        self.despesas = []
        self.veiculos = []
        self.vendas = []
        self.despesas_fixas = 0
        self.total_produzido = 0

    def salvar_dados(self):
        dados = {
            "despesas": [
                {"descricao": d.descricao, "categoria": d.categoria, "valor": d.valor}
                for d in self.despesas
            ],
            "veiculos": [
                {"modelo": v.modelo, "ano": v.ano, "custo_fabricacao": v.custo_fabricacao}
                for v in self.veiculos
            ],
            "despesas_fixas": self.despesas_fixas,
            "total_produzido": self.total_produzido
        }

        with open("dados_empresa.json", "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def carregar_dados(self):
        try:
            with open("dados_empresa.json", "r", encoding="utf-8") as f:
                dados = json.load(f)

            for d in dados["despesas"]:
                self.adicionar_despesa(Despesas(d["descricao"], d["categoria"], d["valor"]))

            for v in dados["veiculos"]:
                self.adicionar_veiculo(Veiculo(v["modelo"], v["ano"], v["custo_fabricacao"]))

            self.despesas_fixas = dados["despesas_fixas"]
            self.total_produzido = dados["total_produzido"]

        except FileNotFoundError:
            pass

    def adicionar_despesa(self, despesa):
        self.despesas.append(despesa)

    def listar_despesas(self):
        if self.despesas:
            print("\n--- Lista de Despesas ---")
            for index, despesa in enumerate(self.despesas, start=1):
                print(f"{index}. {despesa.descricao} - {despesa.categoria} - R${despesa.valor:.2f} (Imposto: R${despesa.imposto:.2f})")
        else:
            print("Nenhuma despesa registrada.")

    def listar_funcionarios(self):
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

    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)
        self.total_produzido += 1

    def listar_veiculos(self):
        if not self.veiculos:
            print("Nenhum veículo cadastrado.")
        else:
            print("\n--- Veículos Produzidos ---")
            total_veiculos = len(self.veiculos)
            despesa_fixa_por_carro = self.despesas_fixas / total_veiculos if total_veiculos > 0 else 0

            for i, v in enumerate(self.veiculos, start=1):
                custo_total_carro = v.custo_fabricacao + despesa_fixa_por_carro
                preco_venda_carro = custo_total_carro * 1.5
                print(f"{i}. {v.modelo} ({v.ano})")
                print(f"   Custo Fabricação: R${v.custo_fabricacao:.2f}")
                print(f"   Custo Total por Carro: R${custo_total_carro:.2f}")
                print(f"   Preço de Venda: R${preco_venda_carro:.2f}")

    
    def excluir_veiculo(self, index):                        # excluir veículo
        if 0 <= index < len(self.veiculos):
            veiculo = self.veiculos.pop(index)
            self.total_produzido -= 1
            print(f"Veículo {veiculo.modelo} ({veiculo.ano}) removido com sucesso!")
        else:
            print("Índice inválido.")

    def calcular_custo_total_producao(self):
        custo_fabr = sum(v.custo_fabricacao for v in self.veiculos)
        custo_total = custo_fabr + self.despesas_fixas
        return custo_total

    def calcular_custo_por_carro(self):
        if self.total_produzido == 0:
            return 0
        return self.calcular_custo_total_producao() / self.total_produzido

    def calcular_preco_venda(self):
        custo_unitario = self.calcular_custo_por_carro()
        return custo_unitario * 1.5


if __name__ == "__main__":
    controle = ControleEmpresa()
    controle.carregar_dados()   

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

        if escolha == '1':
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
                            idx = int(input("Número do funcionário a excluir: ")) - 1
                            controle.excluir_funcionario(idx)
                        except ValueError:
                            print("Digite apenas números válidos.")

                elif opc == '3':
                    controle.listar_funcionarios()

                elif opc == '4':
                    break

                else:
                    print("Opção inválida.")

        elif escolha == '3':
            while True:
                print("\n--- Menu Produção de Veículos ---")
                print("1. Adicionar Veículo")
                print("2. Listar Veículos")
                print("3. Excluir Veículo")  
                print("4. Voltar")
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
                    controle.listar_veiculos()
                    if controle.veiculos:
                        try:
                            idx = int(input("Número do veículo a excluir: ")) - 1
                            controle.excluir_veiculo(idx)
                        except ValueError:
                            print("Digite apenas números válidos.")

                elif opc == '4':
                    break

                else:
                    print("Opção inválida.")

        elif escolha == '4':
            custo_total = controle.calcular_custo_total_producao()
            custo_por_carro = controle.calcular_custo_por_carro()
            preco_venda = controle.calcular_preco_venda()

            print("\n--- Custos e Preço de Venda ---")
            print(f"Despesas Fixas: R${controle.despesas_fixas:.2f}")
            print(f"Total Produzido: {controle.total_produzido}")
            print(f"Custo Total de Produção: R${custo_total:.2f}")
            print(f"Custo por Carro: R${custo_por_carro:.2f}")
            print(f"Preço de Venda Sugerido (+50% lucro): R${preco_venda:.2f}")

        elif escolha == '5':
            controle.listar_despesas()

        elif escolha == '6':
            controle.listar_veiculos()

        elif escolha == '7':
            print("Salvando dados...")
            controle.salvar_dados()
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida.")
