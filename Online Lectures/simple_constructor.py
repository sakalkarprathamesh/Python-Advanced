class SimpleConstructor:

    def __init__(self, name): #constuctor 
        self.name= name

    def __init__(self): #constuctor -2
        pass

    def show_name(self):
        print('Name :', self.name)

    def __del__(self):
        print('I am deleting class') 

    def run(self):
        pass

if __name__ == "__main__": 
    object = SimpleConstructor()
    object.run