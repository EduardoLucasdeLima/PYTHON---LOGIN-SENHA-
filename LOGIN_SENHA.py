# Dicionário para armazenar os usuários e senhas
usuarios = {'usuario1': 'senha123', 'usuario2': 'senha456'}

def tela_login():
    print("=== TELA DE LOGIN ===")
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    return usuario, senha

def verificar_credenciais(usuario, senha):
    if usuario in usuarios and usuarios[usuario] == senha:
        return True
    else:
        return False

def main():
    tentativas = 3
    while tentativas > 0:
        usuario, senha = tela_login()
        if verificar_credenciais(usuario, senha):
            print("Login bem-sucedido! Bem-vindo,", usuario)
            break
        else:
            tentativas -= 1
            print("Credenciais inválidas. Tentativas restantes:", tentativas)
    else:
        print("Você excedeu o número máximo de tentativas.")

if __name__ == "__main__":
    main()
