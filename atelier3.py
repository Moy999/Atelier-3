class Vector2D:
    # constructeur
    def __init__(self, x=0 ,y=0):
        self.x = x
        self.y = y
    # show method
    def show(self):
        return "x= "+str(self.x)+" y="+str(self.y)
    # add operator
    def __add__(self , other):
        ax= self.x+other.x
        ay= self.y+other.y
        return Vector2D(ax , ay)
# créer des vectors
v1 = Vector2D()
v2 = Vector2D(5 , 9)
v3 = Vector2D(6 , 5)
# tester la méthode show()
print(v1.show())
print(v2.show())
# tester l'opération + avec 2 vectors
va = v2 + v3
print(va.show())
# //////////////
# classe Rectangle
class Rectangle:
    nom = "rectangle"
    # constructeur
    def __init__(self, lo=0 ,la=0):
        self.longueur = lo
        self.largeur = la
    def show(self):
    # méthode pour afficher les attributs de classe
        return "nom: "+self.nom +" longueur =" +str(self.longueur) + "largeur = "+str(self.largeur)
    # calculer le surface 
    def surface(self):
        return "surface : "+str(self.largeur * self.longueur)
# classe Carré
class Carré(Rectangle):
    nom= "carré"
    def __init__(self, lo=0):
        super().__init__(lo=lo, la=lo)

r1= Rectangle(5 , 6)
c1= Carré(8)
# tester avec le rectangle
print(r1.show())
print(r1.surface())
# tester avec le carré
print(c1.show())
print(c1.surface())
# ////////////
# classe Point
class Point:
    def __init__(self , x=0.0 , y=0.0):
        self.x = x
        self.y = y 
    def show(self):
        return "("+str(self.x)+" , "+str(self.y)+")"
# classe Segment
class Segment():
    # constructeur qui prend 2 objets Pount comme paramètres
    def __init__(self , x1=0.0 , y1=0.0, x2=0.0, y2=0.0):
        self.org = Point(x1, y1)
        self.ext = Point(x2 , y2)
    def show_seg(self):
        return "(org, ,ext) Segment = ["+self.org.show() + ", "+self.ext.show() + "]"
            
p1 = Point(1 , 2)
p2 = Point(3 , 4)
# tester le Point
print(p1.show())
# tester le Segment
s1= Segment(p1.x, p1.y , p2.x, p2.y)
print(s1.show_seg())                             