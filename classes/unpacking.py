def consolidar_leituras(*files) :

    totalsum = 0
    counter = 0

    for arq in files :
        try :
            with open(arq) as file :
                for line in file: 
                    try :
                        num = float(line.strip())
                    except ValueError :
                        print(f'Valor não numérico.')
                    
                    else :
                        totalsum += num
                        counter += 1
        
        except FileNotFoundError :
            print(f'Arquivo {arq} não encontrado.')
    
    if counter != 0 :
        with open('relatorio_final.txt', 'w') as newfile :
            newfile.write(f'{totalsum/counter:.2f}')
    else :
        with open('relatorio_final.txt', 'w') as newfile :
            newfile.write(f'{0:.2f}')
