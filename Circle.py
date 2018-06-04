#!"C:\Phython\python.exe"
"""Circle.py, by yukthika,2017
This program is the first phython
"""               
    class Circle(object):
        
          def __init__(self):
                
                super(Circle, self).__init__()class Circle(object):
    
        self._radius = 0.0
        self._NoofCircleCreated++

    @property
    def radius(self):
        """I'm the Radius property.getter"""
        return self._radius


    @radius.setter
    def radius(self, value):
        """I'm the Radius property.setter"""
        
        self._radius = value

    @radius.deleter
    def radius(self):
         """I'm the Radius property deleter"""
        del self._radius
        
    @property
    def NoofCircleCreated(self):
        return self._NoofCircleCreated
     @property
    def Area():
        return math.pi * radius * radius
     @property
    def Perimeter():
        return math.pi * radius * 2
    
    # main function
    
    if __name__ == "__main__":
        
        """
        Main function
        """
        C1 =Circle()
        print(C1.self._radius )
        print(C!.self._NoofCircleCreated)
        
        C2 =Circle()
        print(C2.self._radius )
        print(C2.self._NoofCircleCreated)
        
         C3 =Circle()
        print(C3.self._radius )
        print(C3.self._NoofCircleCreated)
        
        
    
                    
                    
                
    