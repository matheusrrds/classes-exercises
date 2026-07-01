class Point2D :

    def __init__(self, x, y) :

        self.x = float(x)
        self.y = float(y)
        self.name = (x, y)
    
    def euclidian_dist(self, point) :

        distance = ((point.x - self.x)**2 + (point.y - self.y)**2) ** 0.5
        return distance
    
class Rectangle :
    
    def __init__(self, point, height, width) :

        self.height = height
        self.width = width

        if height <= 0 or width <= 0 :
            raise ValueError('Digite uma altura/largura válida.')
        
        self.topleft = point
        self.bottomleft = Point2D(point.x, point.y-height)

        self.topright = Point2D(point.x+width, point.y)
        self.bottomright = Point2D(point.x+width, point.y-height)

class Circle :

    def __init__(self, center, radius) :

        self.center = center
        self.radius = radius

        if radius <= 0 :
            raise ValueError('Informe um raio válido')

    def verify_point(self, point) :


        distance = self.center.euclidian_dist(point)


        if distance > self.radius :

            return f'O ponto {point.name} está fora do circulo'
        
        else :
            
            return f'O ponto {point.name} está no circulo'

    def verify_rectangle(self, rectangle) :
                
        vertices = [
            rectangle.topleft,
            rectangle.topright,
            rectangle.bottomleft,
            rectangle.bottomright
        ]

        for vertice in vertices :
            if vertice.euclidian_dist(self.center) > self.radius :
                return 'O retângulo não está dentro'
            
        return 'O retângulo está dentro do circulo'
       
center = Point2D(100, -75)
circle = Circle(center, 10)

a = Point2D(93, -68)
rectangle = Rectangle(a, 1, 1)

print(circle.verify_rectangle(rectangle))



