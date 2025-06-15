import re
from sqlalchemy.orm import Session
from model import (
    Produto, Marca, Nutriente, Ingrediente, Tag, Categoria,
    ProdutoMarca, ProdutoIngrediente, ProdutoNutriente,
    ProdutoTag, ProdutoCategoria
)

def SanitizeText(texto, maxLength=None, onlyAscii=False):
    if not isinstance(texto, str):
        texto = str(texto or "")
    texto = texto.strip()
    if onlyAscii:
        texto = re.sub(r'[^\x00-\x7F]+', '', texto)
    if maxLength:
        return texto[:maxLength]
    return texto

def Load(db: Session, data: dict):
    if db.query(Produto).filter_by(codigo=data["codigo"]).first():
        print(f"WARN: Produto {data['codigo']} já existe no banco. Pulando inserção.")
        return
    
    produto = Produto(
        codigo=data["codigo"],
        nome=SanitizeText(data["nome"], 100),
        nutriscore=data.get("nutriscore"),
        ecoscore=data.get("ecoscore"),
        novascore=data.get("novascore"),
    )
    db.add(produto)
    db.flush()

    # Marcas
    marcasInseridas = set()
    for marca_nome in data.get("marcas", []):
        nome = SanitizeText(marca_nome, 100)
        if not nome or nome in marcasInseridas:
            continue
        marcasInseridas.add(nome)

        marca = db.query(Marca).filter_by(nome=nome).first()
        if not marca:
            marca = Marca(nome=nome)
            db.add(marca)
            db.flush() 
        db.add(ProdutoMarca(produto_id=produto.codigo, marca_id=marca.id))

    # Categorias
    categoriasInseridas = set()
    for categoria_nome in data.get("categorias", []):
        nome = SanitizeText(categoria_nome, 100)
        if not nome or nome in categoriasInseridas:
            continue
        categoriasInseridas.add(nome)

        categoria = db.query(Categoria).filter_by(nome=nome).first()
        if not categoria:
            categoria = Categoria(nome=nome)
            db.add(categoria)
            db.flush()
        db.add(ProdutoCategoria(produto_id=produto.codigo, categoria_id=categoria.id))

    # Ingredientes
    ingredientesInseridos = set()
    for ing in data.get("ingredientes", []):
        nome = SanitizeText(ing.get("text"), 100)
        if not nome or nome in ingredientesInseridos:
            continue
        ingredientesInseridos.add(nome)

        ingrediente = db.query(Ingrediente).filter_by(nome=nome).first()
        if not ingrediente:
            ingrediente = Ingrediente(
                nome=nome,
                vegano=ing.get("vegan") == "yes",
                vegetariano=ing.get("vegetarian") == "yes"
            )
            db.add(ingrediente)
            db.flush()
        db.add(ProdutoIngrediente(produto_id=produto.codigo, ingrediente_id=ingrediente.id))

    # Nutrientes
    for nome, valor in data.get("nutrientes", {}).items():
        if not isinstance(valor, (int, float)):
            continue
        nome = SanitizeText(nome, 100)
        unidade = "g"
        nutriente = db.query(Nutriente).filter_by(nome=nome).first()
        if not nutriente:
            nutriente = Nutriente(nome=nome, unidade=unidade)
            db.add(nutriente)
            db.flush()
        db.add(ProdutoNutriente(produto_id=produto.codigo, nutriente_id=nutriente.id, quantidade_100g=valor))

    # Tags
    tagsInseridas = set()
    for tag_nome in data.get("tags", []):
        nome = SanitizeText(tag_nome, 100)
        if not nome or nome in tagsInseridas:
            continue
        tagsInseridas.add(nome)

        tipo = "additive" if "add" in nome else "allergen"

        tag = db.query(Tag).filter_by(nome=nome, tipo=tipo).first()
        if not tag:
            tag = Tag(nome=nome, tipo=tipo)
            db.add(tag)
            db.flush()
        db.add(ProdutoTag(produto_id=produto.codigo, tag_id=tag.id))

    db.flush()