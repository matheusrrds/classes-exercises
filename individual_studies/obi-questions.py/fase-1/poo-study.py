class Ponto2D :

    def __init__(self, x=0, y=0) :

        self.x = x
        self.y = y
    
    def quadrante(self) :

        if self.x > 0 :

            if self.y > 0 :

                return 1
            
            if self.y < 0 :

                return 4
        
        if self.x < 0 :

            if self.y > 0 :

                return 2
            
            if self.y < 0 :

                return 3

    def translacao(self, dh=0, dv=0) :

        self.x += dh
        self.y += dv

    def manhattan_distance(self, x, y) :

        return abs(self.x - x) + abs(self.y - y)

    def distancia(self, point, dist_type='euclidean') :

        dist_type = dist_type.lower()

        if dist_type == 'euclidean' :

            return ((self.x - point.x)**2 + (self.y - point.y)**2) ** 0.5
        
        elif dist_type == 'manhattan' :

            return abs(self.x - point.x) + abs(self.y - point.y)
        
        return 0


p = Ponto2D(-1,4)
q = Ponto2D(12,63)

print(f"{p.distancia(q, 'euclidean'):.2f}")
