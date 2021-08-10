import copy
from abc import ABC


class Cloneable(ABC):

    def clone(self):
        return copy.copy(self)

    def deep_clone(self):
        return copy.deepcopy(self)


class Project(Cloneable):
    def __init__(self, title: str, deadline: str, ):
        self.title = title
        self.deadline = deadline

    def __str__(self):
        return 'Project: title = {0},deadline = {1}, id_obj = {2}'.format(self.title, self.deadline, id(self))


obj1 = Project('CRM', '12.12.21')
obj1.l = [1, 2, [3]]
obj2 = obj1.deep_clone()
print(obj1)
print(obj2)
obj2.l.append(4)
print(obj1.l)
print(obj2.l)
