#Dev - MARIA EDUARDA PEDREIRA SOUZA TEIXEIRA

import os
import json
from typing import List, Dict, Any

FILE_NAME = "insumos.json"
FILE_PATH = os.path.join(os.path.dirname(__file__), FILE_NAME)

# Lista de dicionários para armazenar produtos
estoque: List[Dict[str, Any]] = []


def carregar_insumos() -> None:
    """Carrega produtos do arquivo JSON para a lista estoque."""
    global estoque
    if not os.path.exists(FILE_PATH):
        estoque = []
        return
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                estoque = data
            else:
                estoque = []
    except Exception as e:
        print(f"Erro ao carregar insumos: {e}")
        estoque = []


def salvar_insumos() -> None:
    """Salva a lista de produtos no arquivo JSON."""
    try:
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(estoque, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Erro ao salvar insumos: {e}")


def _buscar_produto(codigo: str) -> int:
    """Retorna o índice do produto ou -1 se não encontrado."""
    for i, produto in enumerate(estoque):
        if produto["codigo"] == codigo:
            return i
    return -1


def cadastrar_insumo() -> None:
    """Cadastra um novo insumo na lista."""
    print("\n--- Cadastrar Insumo ---")
    
    codigo = input("Código do insumo: ").strip()
    
    if _buscar_produto(codigo) != -1:
        print("Código já cadastrado. Tente novamente.")
        return
    
    nome = input("Nome do insumo: ").strip()
    quantidade = int(input("Quantidade em estoque: "))
    preco = float(input("Preço por unidade: "))
    fabricacao = input("Data de fabricação (DD/MM/AAAA): ").strip()
    validade = input("Data de validade (DD/MM/AAAA): ").strip()
    fornecedor = input("Nome do fornecedor: ").strip()
    
    novo_produto = {
        "codigo": codigo,
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco,
        "fabricacao": fabricacao,
        "validade": validade,
        "fornecedor": fornecedor
    }
    
    estoque.append(novo_produto)
    salvar_insumos()
    print("Insumo cadastrado com sucesso!")


def registrar_entrada() -> None:
    """Aumenta a quantidade de um insumo existente."""
    print("\n--- Registrar Entrada de Insumo ---")
    
    codigo = input("Código do insumo: ").strip()
    indice = _buscar_produto(codigo)
    
    if indice == -1:
        print("Código não encontrado. Tente novamente.")
        return
    
    quantidade = int(input("Quantidade a adicionar: "))
    estoque[indice]["quantidade"] += quantidade
    salvar_insumos()
    print("Entrada registrada com sucesso!")


def registrar_saida() -> None:
    """Diminui a quantidade de um insumo existente."""
    print("\n--- Registrar Saída de Insumo ---")
    
    codigo = input("Código do insumo: ").strip()
    indice = _buscar_produto(codigo)
    
    if indice == -1:
        print("Código não encontrado. Tente novamente.")
        return
    
    quantidade = int(input("Quantidade a remover: "))
    if estoque[indice]["quantidade"] < quantidade:
        print("Quantidade insuficiente em estoque.")
        return
    
    estoque[indice]["quantidade"] -= quantidade
    salvar_insumos()
    print("Saída registrada com sucesso!")


def listar_insumos() -> None:
    """Lista todos os insumos cadastrados."""
    if not estoque:
        print("\nNenhum insumo cadastrado.")
        return
    
    print("\n--- Lista de Insumos ---")
    for i, produto in enumerate(estoque, 1):
        print(f"\n{i}. {produto['nome']} (Código: {produto['codigo']})")
        print(f"   Quantidade: {produto['quantidade']} unidades")
        print(f"   Preço unitário: R$ {produto['preco']:.2f}")
        print(f"   Fabricação: {produto['fabricacao']}")
        print(f"   Validade: {produto['validade']}")
        print(f"   Fornecedor: {produto['fornecedor']}")


def deletar_insumo() -> None:
    """Remove um insumo do estoque."""
    print("\n--- Deletar Insumo ---")
    
    codigo = input("Código do insumo a deletar: ").strip()
    indice = _buscar_produto(codigo)
    
    if indice == -1:
        print("Código não encontrado.")
        return
    
    confirmacao = input(f"Tem certeza que deseja deletar '{estoque[indice]['nome']}'? (s/n): ").lower()
    if confirmacao == 's':
        estoque.pop(indice)
        salvar_insumos()
        print("Insumo deletado com sucesso!")
    else:
        print("Operação cancelada.")


def custo_mensal() -> None:
    """Calcula o custo total mensal dos insumos em estoque."""
    if not estoque:
        print("\nNenhum insumo em estoque.")
        return
    
    total_custo = sum(p["quantidade"] * p["preco"] for p in estoque)
    print(f"\nCusto total mensal dos insumos em estoque: R$ {total_custo:.2f}")


def custo_semanal() -> None:
    """Calcula o custo total semanal dos insumos em estoque."""
    if not estoque:
        print("\nNenhum insumo em estoque.")
        return
    
    total_custo = sum((p["quantidade"] * p["preco"]) / 4 for p in estoque)
    print(f"\nCusto total semanal dos insumos em estoque: R$ {total_custo:.2f}")


def custo_anual() -> None:
    """Calcula o custo total anual dos insumos em estoque."""
    if not estoque:
        print("\nNenhum insumo em estoque.")
        return
    
    total_custo = sum(p["quantidade"] * p["preco"] * 12 for p in estoque)
    print(f"\nCusto total anual dos insumos em estoque: R$ {total_custo:.2f}")  