from pydantic import BaseModel

class Schema(BaseModel):
    id_produto: int
    nome: str
    quantidade: int
    preco: float
    categoria: str

dicionario_produtos = {
    "id_produto": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "nome": ["Produto 1", "Produto 2", "Produto 3", "Produto 4", "Produto 5", "Produto 6", "Produto 7", "Produto 8", "Produto 9", "Produto 10"],
    "quantidade": [20, 15, 30, 25, 10, 18, 22, 12, 28, 35],
    "preco": [10.99, 15.50, 20.25, 8.75, 12.00, 18.99, 22.50, 11.25, 30.75, 14.99],
    "categoria": ["Categoria A", "Categoria B", "Categoria A", "Categoria C", "Categoria B", "Categoria C", "Categoria A", "Categoria B", "Categoria C", "Categoria A"]
}
