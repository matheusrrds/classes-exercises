# MATHEUS RAMOS RODRIGUES DE SOUZA

filename = input()
attempt = 0
suspects = 0

with open(filename, 'r') as file :
    for line in file :
        attempt += 1
        line = line.strip()
        user, password = line.split(':')

        if 'admin' in user.lower() or len(password) < 6 :
            suspects += 1
            print(f"ALERTA: Tentativa suspeita detectada para usuário '{user}'.")
    
    print(f'Total de tentativas: {attempt} | Suspeitas: {suspects}.')
        
