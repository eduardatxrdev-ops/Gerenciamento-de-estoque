# ================================
# SISTEMA DE RECURSOS HUMANOS
# ================================

def cadastrar_funcionarios():
    funcionarios = []

    print("\n=== CADASTRO DE FUNCIONÁRIOS ===")

    for i in range(5):
        print(f"\nFuncionário {i + 1}")
        funcionario = {
            "nome": input("Nome: "),
            "cpf": input("CPF: "),
            "rg": input("RG: "),
            "endereco": input("Endereço: "),
            "telefone": input("Telefone: "),
            "filhos": int(input("Quantidade de filhos: ")),
            "cargo": input("Cargo (operacional / gerente / diretor): ").lower(),
            "valor_hora": float(input("Valor da hora trabalhada: R$ ")),
            "horas_trabalhadas": float(input("Horas trabalhadas no mês: "))
        }

        funcionarios.append(funcionario)

    return funcionarios


def calcular_salario_bruto(funcionario):
    salario = funcionario["horas_trabalhadas"] * funcionario["valor_hora"]

    if funcionario["cargo"] not in ["gerente", "diretor"]:
        if funcionario["horas_trabalhadas"] > 160:
            extras = funcionario["horas_trabalhadas"] - 160
            salario += extras * funcionario["valor_hora"] * 0.5

    return salario


def calcular_irpf(salario_bruto):
    if salario_bruto <= 2259.20:
        return 0
    elif salario_bruto <= 2826.65:
        return salario_bruto * 0.075
    elif salario_bruto <= 3751.05:
        return salario_bruto * 0.15
    elif salario_bruto <= 4664.68:
        return salario_bruto * 0.225
    else:
        return salario_bruto * 0.275


def calcular_salario_liquido(salario_bruto, ir):
    return salario_bruto - ir


def gerar_relatorio(funcionarios):
    print("\n=== RELATÓRIO FINAL ===\n")

    funcionarios_ordenados = sorted(funcionarios, key=lambda x: x["nome"])

    for f in funcionarios_ordenados:
        salario_bruto = calcular_salario_bruto(f)
        ir = calcular_irpf(salario_bruto)
        salario_liquido = calcular_salario_liquido(salario_bruto, ir)

        paga_ir = "SIM" if ir > 0 else "NÃO"

        print(f"Nome: {f['nome']}")
        print(f"Salário Bruto: R$ {salario_bruto:.2f}")
        print(f"Salário Líquido: R$ {salario_liquido:.2f}")
        print(f"Paga IR: {paga_ir}")
        print("-" * 30)


def main():
    funcionarios = cadastrar_funcionarios()
    gerar_relatorio(funcionarios)


main()
