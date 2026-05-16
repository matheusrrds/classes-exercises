users_a = input().split(',')
users_b = input().split(',')

server_a = set(users_a)
server_b = set(users_b)

both_servers = server_a.intersection(server_b)

only_a = server_a.difference(server_b)

unique_users = server_a.union(server_b)

print(f'Usuários em ambos os servidores: {len(both_servers)}')
print(f'Usuários apenas no Servidor A: {len(only_a)}')
print(f'Total de usuários únicos na auditoria: {len(unique_users)}')