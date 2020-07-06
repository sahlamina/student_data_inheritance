class Student_data:
    def __init__(self, name, stream):

        self.name = name
        self.stream = stream

    def study(self):
        print(self.name + " is studying")

    def online(self):
        print(self.name + " is online")



class Trainee(Student_data):
    pass


agbo = Trainee("Agbo", "DevOps")
print(agbo.name)
agbo.study()
print(agbo.study())
agbo.online()