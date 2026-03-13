import json
import os

ARQUIVO = "usuarios.json"


def carregar_usuario():
    """Carrega a lista de usuários do arquivo JSON."""
    if not os.path.exists(ARQUIVO):
        return []

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def salvar_usuario(lista):
    """Salva a lista de usuários no arquivo JSON."""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)


def validar_email(email, lista_existente):
    """Valida formato básico do e-mail e verifica duplicidade."""
    email = email.strip()

    if not email:
        return False, "E-mail não pode ficar vazio."

    if "@" not in email or "." not in email:
        return False, "E-mail inválido."

    for user in lista_existente:
        email_existente = user.get("email", "").strip().lower()
        if email_existente == email.lower():
            return False, "E-mail já cadastrado!"

    return True, ""


def buscar_usuario_por_email(email):
    """Busca um usuário pelo e-mail."""
    usuarios = carregar_usuario()
    email = email.strip().lower()

    for user in usuarios:
        if user.get("email", "").strip().lower() == email:
            return user

    return None