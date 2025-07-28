class Car:
    def __init__(self,model,speed):
        self.model = model
        self.speed = speed

    def display (self):
        print(f"model:{self.model},speed:{self.speed}")


p1= Car("Tesla",30) 
p1.display()    
        
