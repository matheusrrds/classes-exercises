def replacefile(old, new, fileinput, fileoutput) :

    with open(fileinput, 'r') as filein :
        with open(fileoutput, 'w') as fileout :

            for line in filein :
                
                fileout.write(line.replace(old, new))
                
replacefile('peido', 'sou show', 'teste1.txt', 'GASESKKKK.txt')