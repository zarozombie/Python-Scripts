class tester:

    def __init__(self, test):
        self.test = test

    def __repr__(self):
        return 'This is the repr of hello world'

    def __str__(self):
        return 'hello'

p = tester("test")
