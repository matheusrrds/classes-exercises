# MATHEUS RAMOS RODRIGUES DE SOUZA

def processar_transacoes(nome_arquivo) :
    total = 0

    try :
        with open(nome_arquivo, 'r') as fileinput :
            
            for line in fileinput :
                line = line.strip()

                idprod, value = line.split(',')
                try :
                    value = float(value)
                    total += value
                except ValueError :
                    print('Aviso: Linha ignorada devido a dados corrompidos.')

    except FileNotFoundError :
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
    
    else :

        with open('resultado_final.txt', 'w') as fileout :
            fileout.write(f'Total arrecadado: R$ {total:.2f}')

processar_transacoes('vendas.txt')