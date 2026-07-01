def consolidar_leituras(*files) :

    for file in files :
        num = 0
        linenum = 0
        counter = 0
        try :
            with open(file, 'r') as fileinput :

                for line in fileinput :
                    linenum += 1

                    try :
                        num += float(line.strip())
                        counter += 1
                    except ValueError :
                        print(f'linha {linenum} do arquivo {file} não possui número')
                
            if counter != 0 :
                average = num / counter
            else :
                average = 0

            with open('relatorio_final.txt', 'a') as fileout :

                fileout.write(f'Arquivo: {file} | Média: {average:.2f} \n')
        
        except FileNotFoundError :
            print(f'Arquivo {file} não encontrado.')

consolidar_leituras('teste1.txt', 'teste2.txt')