
class Cat:
    def say(self):
        print("I am a cat")

class Dog:
    def say(self):
        print("I am a dog")

class Duck:
    def say(self):
        print("I am a duck")

animals = [Cat(), Dog(), Duck()]
for animal in animals:
    animal.say()


a = ["harry", "hermione", "ron"]
name_tuple = {"zhangsan", "lisi"}
a.extend(name_tuple)
print(a)                    # ['harry', 'hermione', 'ron', 'lisi', 'zhangsan']


class Company:
    def __init__(self, employee_list) -> None:
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]
    
company = Company(['tom', 'bob', 'jack'])
a.extend(company)
print(a)                    # ['harry', 'hermione', 'ron', 'lisi', 'zhangsan', 'tom', 'bob', 'jack']


