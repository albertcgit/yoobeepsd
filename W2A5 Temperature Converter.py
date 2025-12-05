class TempConverter:
    def __init__(self, user_input): #initialize and execute user_input
        try:

            if " " in user_input:
                raise ValueError #if there's whitespaces

            self.unit = user_input[0] #get 1st element from string

            if self.unit not in ['C', 'F']:
                raise ValueError #check element and throws error if failed

            self.value = float(user_input[1:]) #get 2nd element and onwards from string
            self.convert()  #proceed to convert if no error thrown

        except ValueError: #print if error thrown
            print("Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix.")

    def to_celsius(self):
        return (self.value - 32) * 5/9 #conversion

    def to_fahrenheit(self):
        return (self.value * 9/5) + 32 #conversion

    def convert(self):
        if self.unit == 'C': #execute conversion to Fahrenheit and print
            print(f"{self.unit}{int(self.value)} Celsius is converted to {self.to_fahrenheit():.2f} Fahrenheit")
        if self.unit == 'F': #execute conversion to Celsius and print
            print(f"{self.unit}{int(self.value)} Fahrenheit is converted to {self.to_celsius():.2f} Celsius")

if __name__ == "__main__":
    user_input = input("Enter temperature (i.e. C15 or F15): ") #ask user input
    object = TempConverter(user_input) #create object