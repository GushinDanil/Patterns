from abc import ABC, abstractmethod
import creational.builder.computer as comp


class CompBuilder(ABC):

    def createComputer(self):
        self.computer = comp.Computer()

    @abstractmethod
    def buildRam(self):
        pass

    @abstractmethod
    def buildProcessor(self):
        pass

    @abstractmethod
    def buildMonitor(self):
        pass

    def getComputer(self):
        return self.computer


class WeakCompBuilder(CompBuilder):

    def buildRam(self):
        self.computer.setRam(2)

    def buildProcessor(self):
        self.computer.setProcessor('Radeon 4.3')

    def buildMonitor(self):
        self.computer.setMonitor('500/1000')


class StrongCompBuilder(CompBuilder):

    def buildRam(self):
        self.computer.setRam(16)

    def buildProcessor(self):
        self.computer.setProcessor('Intel core i7 3.1')

    def buildMonitor(self):
        self.computer.setMonitor('1900/2500')
