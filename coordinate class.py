class Point:    
    def __init__(self,x,y):
        self.x_cod=x
        self.y_cod=y
        
    def __str__(self):
        return '<{},{}>'.format(self.x_cod,self.y_cod)
        
p1=Point(0,0)
p2=Point(-2,-1)
print(p1)
print(p2)
