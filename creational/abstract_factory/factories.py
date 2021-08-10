from abc import ABC, abstractmethod
import creational.abstract_factory.products as prod


class TeamFactory(ABC):
    @abstractmethod
    def getDev(self):
        pass

    @abstractmethod
    def getTester(self):
        pass

    @abstractmethod
    def getPM(self):
        pass


class BankingTeam(TeamFactory):

    def getDev(self):
        return prod.PhpDev()

    def getTester(self):
        return prod.AnalyticalTester()

    def getPM(self):
        return prod.BankPG()


class WebProgTeam(TeamFactory):

    def getDev(self):
        return prod.JavaDev()

    def getTester(self):
        return prod.TechnicalTester()

    def getPM(self):
        return prod.WebPM()
