# MATHEUS RAMOS RODRIGUES DE SOUZA

class Megazord :
    def __init__(self, nome, coord_x, coord_y, bateria) :
        
        self.nome = nome

        self.coord_x = coord_x
        self.coord_y = coord_y

        if bateria > 100 :
            self.bateria = 100
        else :
            self.bateria = bateria

        print(f'Megazord formado: [{self.nome}] Pos: ({self.coord_x:.1f}, {self.coord_y:.1f}) | Bateria: {self.bateria:.0f}%')
    
    def movermz(self, dx, dy) :

        try :


            if self.exists is None:
                print(f'Robô {self.nome} não pôde ser movido: Robô não encontrado!')
                return

            if self.bateria >= (abs(dx) + abs(dy)) : 

                distance = ( (self.coord_x - dx)**2 + (self.coord_y - dy)**2 ) ** 0.5

                self.coord_x += dx
                self.coord_y += dy

                self.bateria -= distance

                print(f'Robô movido: [{self.nome}] Pos: ({self.coord_x}, {self.coord_y}) | Bateria: {self.bateria:.0f}%')
            
            else :
                raise(Exception)

        except Exception: 
            print(f'Robô {self.nome} não pôde ser movido: Bateria insuficiente!')
        
        except ValueError:
            print(f'Robô {self.nome} não pôde ser movido: Robô não encontrado!')

class Robo :
    def __init__(self, nome, coord_x, coord_y, bateria=100.0) :
        
        self.nome = nome
        self.exists = True

        self.coord_x = coord_x
        self.coord_y = coord_y

        self.bateria = bateria

        print(f'Robô em operação: [{self.nome}] Pos: ({self.coord_x:.1f}, {self.coord_y:.1f}) | Bateria: {self.bateria:.0f}%')

    def __str__(self) :

        return f'[{self.nome}] Pos: ({self.coord_x:.1f}, {self.coord_y:.1f}) | Bateria: {self.bateria:.0f}%'

    def __add__(self, other) :

        newrobot = Megazord(self.nome + '-' + other.nome, (self.coord_x + other.coord_x)/2, (self.coord_y + other.coord_y)/2, self.bateria + other.bateria)

        self.exists = None
        other.exists = None

        megazords[self.nome + '-' + other.nome] = newrobot

        return newrobot

    
    def mover(self, dx, dy) :

        try :

            if self.exists is None:
                print(f'Robô {self.nome} não pôde ser movido: Robô não encontrado!')
                return

            if self.bateria >= (abs(dx) + abs(dy)) : 

                distance = ((self.coord_x - dx)**2 + (self.coord_y - dy)**2) ** 0.5
                self.coord_x += dx
                self.coord_y += dy


                self.bateria -= distance

                print(f'Robô movido: [{self.nome}] Pos: ({self.coord_x}, {self.coord_y}) | Bateria: {self.bateria:.0f}%')
            
            else :
                raise(Exception)

        except Exception: 
            print(f'Robô {self.nome} não pôde ser movido: Bateria insuficiente!')
        
        except ValueError:
            print(f'Robô {self.nome} não pôde ser movido: Robô não encontrado!')
        

n, m = map(int, input().split())

robots = {}
megazords = {}

for _ in range(n) :
    name, x, y = input().split(',')
    x = float(x)
    y = float(y)
    
    robots[name] = Robo(name, x, y)

for _ in range(m) :

    sequence = input().split()

    action = sequence[0]
    identifiers = sequence[1].split(',')

    if action == 'MZ' :

        robotnamea, robotnameb = identifiers        
        string = robotnamea + '-' + robotnameb

        robots[robotnamea] + robots[robotnameb]

    
    elif action == 'MV' :

        robotname, distx, disty = identifiers
        distx = float(distx)
        disty = float(disty)

        if robotname in megazords :
            print(megazords[robotname])
            megazords[robotname].movermz(distx, disty)
        else :
            robots[robotname].mover(distx, disty)

            
    
# era pra mover deu bateria insuficiente
