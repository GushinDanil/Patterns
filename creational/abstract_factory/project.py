import creational.abstract_factory.factories as f


def client(team_factory):
    dev = team_factory().getDev()
    tester = team_factory().getTester()
    pm = team_factory().getPM()

    print(tester.testCode())
    print(pm.manageProject())
    print(dev.writeCode())


client(f.WebProgTeam)
print('-'*50)
client(f.BankingTeam)
