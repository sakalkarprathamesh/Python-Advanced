class number2words:
    """
    Description: A class to convert numbers to their word representations.
    Input: Integer  Number between 0 to 10
    Output: Word representation of the number
    Author: Prathamesh Sakalkar
    Created On: 13/07/2026 12:02
    """

    number = ['zero','one','two','three','four','five','six','seven','eight','nine']
    ls = []


    def input_number(self):

        """
        Arguments: None
        Returns: List of digits in the input number
        """
        self.ls=input("Enter Number between 0 to 10: ")


    def convert_to_words(self):
        
        """
        Arguments: None
        Return: Word representation of the input number
        """

        self.input_number()
        for x in self.ls:
            print(self.number[int(x)], end=" ")

    
if __name__ == "__main__":
        obj = number2words()
        obj.convert_to_words()

