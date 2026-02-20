import json
import os

ARQUIVO = "usuario.json"

def carregar_usuario():
    if not os.path.exists(ARQUIVO):
        return []
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return[]
    
def salvar_usuario(lista):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)

def validar_email(email, lista_existente):
    if "@" not in email or "." not in email:
        return False, "E-mail inválido"
    
    for user in lista_existente:
        if user["email"] == email:
            return False, "E-mail já cadastrado!"
        
    return True, ""

def buscar_usuario_por_email(email):
    usuario = carregar_usuario()
    for user in usuario:
        if user["email"].lower() == email.lower():
            return user
    return None