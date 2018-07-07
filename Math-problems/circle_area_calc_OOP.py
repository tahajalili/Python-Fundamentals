

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        pi = 3.14
        area_value = pi*(self.radius**2)
        print('Area of a circle with r='+str(self.radius),'is',area_value)
    
    def perimeter(self):
        pi = 3.14
        perimeter_value = pi*(self.radius*2)
        print('Perimeter of circle with r='+str(self.radius),'is',perimeter_value)
   
r = input('enter radius: ')


c1 = Circle(int(r))
results = 'Circle\'s info'
print('\n\n',results.center(45,'*'),'\n')
c1.area()
c1.perimeter()

