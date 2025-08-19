#initiate a class
class employee:
    #special function/ magin method / dunder method - constructor
    def __init__(self):
        print("Started executing data/attributes")
        self.id= 451
        self.salary = 50000
        self.designation = "SDE"
        print("attributes/data have been initiated")

    def travel(self, destination):
        print("The travel method was called manually")
        print(f"Employee is now travelling to {destination}")    

#creating an Object(instance) of the class
sam = employee()

#printing attribute
#print(sam.id)

#calling a method
sam.travel("Bangalore")




