class SequenceGenerator:

    def no_generator(self, start= 34):
        for i in range(start, 1001):
            print(i, end=" ")

    def input_start(self):
        start_no= int(input('Enter Start No: '))
        self.no_generator(start=start_no)

if __name__ == "__main__":
    object = SequenceGenerator()
    object.input_start()