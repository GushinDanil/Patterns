import creational.factory_method.factories as f


def client(dev_factory: f.DevFactory):
    dev = dev_factory().createDev()
    print(dev.writeCode())

client(f.JavaDevFactory)
client(f.PhpDevFactory)
