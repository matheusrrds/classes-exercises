class Espaconave :

    def __init__(self, identificator, nome,combustivel) :

        self.nome = nome
        self.id = identificator

        try :
    
            self.combustivel = float(combustivel)
        
        except ValueError :
            
           pass

    def __str__(self) :

        try :
            return f'{self.id} - {self.nome} (Combustível: {self.combustivel:.1f} un)'
        
        except AttributeError :
            return f'Erro: Dados inválidos para a nave {self.id}.'
        
    def __add__(self, another) :

        return self.combustivel + another.combustivel

filename = input()
naveid1 = input()
naveid2 = input()

navedesc = {}
nonvalid = {}

try :
    with open(filename) as file :
        
        for line in file :
            line = line.strip()

            idn, nome, combustivel = line.split(',')

            try :
                float(combustivel)
            except ValueError :
                nonvalid[idn] = Espaconave(idn, nome, combustivel)
                continue

            if not idn.isalnum() or not nome.isalnum() :
                continue

            navedesc[idn] = Espaconave(idn, nome, combustivel)

except FileNotFoundError :
    print(f"Erro: Arquivo '{filename}' não encontrado.")
    exit()

for invalid in nonvalid.values() :
    print(invalid)

for nave in navedesc.values() :

    print(nave)

if naveid1 in navedesc and naveid2 in navedesc :
    print(f'Soma de combustível ({naveid1} + {naveid2}): {navedesc[naveid1] + navedesc[naveid2]}')
else :
    print(f'Erro: Uma ou ambas as naves não foram encontradas.')



