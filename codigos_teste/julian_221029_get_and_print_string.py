class maiusculo():
    def __init__(self):
        self.str1 = ""
    def get_String(self):
        self.str1 = input("digite uma palavra: ")
    def print_String(self):
        print(self.str1.upper())
str1 = maiusculo()
str1.get_String()
str1.print_String()