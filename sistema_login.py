# Definindo as credenciais corretas
USUARIO_CORRETO = "admin"
SENHA_CORRETA = "123456"

# Numero maximo de tentativas
MAX_TENTATIVAS = 3

# Inicializando o contador de tentativas
tentativas = 0

# Loop principal
while tentativas < MAX_TENTATIVAS:
    # Solicitando as credenciais ao usuário
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    # Verificando as credenciais
    if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
        print("Bem-vindo ao sistema!")
        break  # Sai do loop se as credenciais estiverem corretas
    else:
        tentativas += 1
        tentativas_restantes = MAX_TENTATIVAS - tentativas
        if tentativas_restantes > 0:
            print(f"Credenciais incorretas. Você tem mais {tentativas_restantes} tentativa(s).")
        else:
            print("Todas as tentativas foram esgotadas.")

# Verificando se todas as tentativas foram esgotadas
if tentativas == MAX_TENTATIVAS:
    print("Acesso bloqueado!")
    for _ in range(3):
        print("Acesso bloqueado!")
