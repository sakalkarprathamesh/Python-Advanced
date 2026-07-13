class number2words:
    number = ['zero','one','two','three','four','five','six','seven','eight','nine']
    ls = []
    def input_number(self):
        self.ls=input("Enter Number between 0 to 10: ")

    def convert_to_words(self):
        self.input_number()
        for x in self.ls:
            print(self.number[int(x)], end=" ")
    
if __name__ == "__main__":
        obj = number2words()
        obj.convert_to_words()


