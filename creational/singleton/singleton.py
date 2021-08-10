class Singleton:
    instance = None

    def __init__(self):
        if Singleton.instance is None:
            Singleton.instance = self
        else:
            raise Exception('This class is a singleton')

    @staticmethod
    def getInstance():
        if Singleton.instance is None:
            Singleton()
        return Singleton.instance


print(id(Singleton()))
print(id(Singleton.getInstance()))

