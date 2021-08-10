import creational.builder.builder as bu
import creational.builder.computer as comp


class Director:

    def __init__(self, builder: bu.CompBuilder):
        self.builder = builder

    def setBuilder(self, builder):
        self.builder = builder

    def buildComputer(self) -> comp.Computer:
        self.builder.createComputer()
        self.builder.buildMonitor()
        self.builder.buildProcessor()
        self.builder.buildRam()
        return self.builder.getComputer()


if __name__ == "__main__":
    obj = bu.WeakCompBuilder()
    director = Director(obj)
    print(director.buildComputer())
    director.setBuilder(bu.StrongCompBuilder())
    print(director.buildComputer())