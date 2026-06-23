# Atributos: id_robo (string), modelo (string), 
# minerio_coletado (float) e capacidade_maxima (float).

class Robominerador :

    def __init__(self, id_robot, model, mine_collected, max_capacity) :

        self.id = id_robot
        self.model = model
        self.mncollected = mine_collected
        self.max = max_capacity
        self.efficiency = self.mncollected / self.max

    def __str__(self) :

        return f'{self.model} (ID: {self.id}) - Progresso: {(self.mncollected / self.max):.1f} kg'
    
    def __add__(self, another) :

        return self.mncollected + another.mncollected
    
    def __gt__(self, another) :

        return self.efficiency > another.efficiency 
    

filename = input()

robo1 = input()
robo2 = input()

valid_robots = {}

try :
    with open(filename) as file :

        for line in file :

            line = line.strip()
            
            if not line :
                continue

            idr, model, mncollected, maxcap = line.split(',')

            model = model.strip()
            mncollected = mncollected.strip()
            maxcap = maxcap.strip()

            if not idr.isalnum() or not model.isalnum() :

                print(f'Erro: Dados inválidos para o robô {idr}.')
                continue

            try :
                mncollected = float(mncollected)
                maxcap = float(maxcap)

                if maxcap < mncollected :
                    
                    print(f'Erro: Dados inválidos para o robô {idr}.')
                    continue

                if maxcap < 0 or mncollected < 0 :

                    print(f'Erro: Dados inválidos para o robô {idr}.')
                    continue

            except ValueError :
                print(f'Erro: Dados inválidos para o robô {idr}.')
                continue
            
            valid_robots[idr] = Robominerador(idr, model, mncollected, maxcap)

            print(valid_robots[idr])

except FileNotFoundError :

    print(f"Erro: Arquivo '{filename}' não encontrado.")
    exit()

if robo1 in valid_robots and robo2 in valid_robots :

    print(f'Soma do minério coletado ({valid_robots[robo1].id} + {valid_robots[robo2].id}): {valid_robots[robo1] + valid_robots[robo2]} kg')

else :

    print('Um ou ambos os robos não foram encontrados.')
