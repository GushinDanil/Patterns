class Computer:

    def __init__(self, ram='4', processor='Intel i5', monitor='700/1200', mice='Razer', camera='logitech'):
        self.ram = ram
        self.processor = processor
        self.monitor = monitor
        self.mice = mice
        self.camera = camera

    def __str__(self):
        return 'Ram: {0},Monitor: {1},Processor: {2},Mice: {3},Camera: {4}'.format(self.ram,
                                                             self.monitor, self.processor, self.mice,self.camera)

    def setRam(self, ram):
        self.ram = ram

    def setProcessor(self, processor):
        self.processor = processor

    def setMonitor(self, monitor):
        self.monitor = monitor
