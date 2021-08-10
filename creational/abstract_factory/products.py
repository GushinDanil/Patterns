from abc import ABC, abstractmethod


class Developer(ABC):
    @abstractmethod
    def writeCode(self):
        pass


class JavaDev(Developer):
    def writeCode(self):
        return 'Java developer write code ...'


class PhpDev(Developer):
    def writeCode(self):
        return 'Cpp developer write code ...'


class PM(ABC):
    @abstractmethod
    def manageProject(self):
        pass


class BankPG(PM):
    def manageProject(self):
        return 'Bank PM manages project ...'


class WebPM(PM):
    def manageProject(self):
        return 'Web PM manages project ...'


class Tester(ABC):
    @abstractmethod
    def testCode(self):
        pass


class TechnicalTester(Tester):
    def testCode(self):
        return 'Technical tester test code ...'


class AnalyticalTester(Tester):
    def testCode(self):
        return 'Analytical tester test code ...'
