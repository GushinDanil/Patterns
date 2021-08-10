from abc import ABC, abstractmethod


class Developer(ABC):
    @abstractmethod
    def writeCode(self):
        pass


class JavaDev(Developer):
    def writeCode(self):
        return 'System.out.println(\'Java language\');'


class PhpDev(Developer):
    def writeCode(self):
        return 'std::cout<<\'Cpp language\';'

