class DoisMetodos():

    def __init__(self):
        self.palavra1 = ""
    def get_string(self):
        self.palavra1 = input("Digite alguma palavra: ")
    def print_string(self):
        print(self.palavra1.upper())

palavra1 = DoisMetodos()
palavra1.get_string()
palavra1.print_string()        