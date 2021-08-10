from abc import ABC, abstractmethod
import creational.factory_method.products as prod


class DevFactory(ABC):
    @abstractmethod
    def createDev(self):
        pass


class PhpDevFactory(DevFactory):
    def createDev(self):
        return prod.PhpDev()


class JavaDevFactory(DevFactory):
    def createDev(self):
        return prod.JavaDev()


