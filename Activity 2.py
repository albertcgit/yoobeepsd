hoursWorked = float(input("Enter hours worked: ")) #user input to hoursWorked variable
hourlyRate = float(input("Enter hourly pay rate: ")) #user input to hourlyRate variable
grossPay = hoursWorked * hourlyRate

print(f"Gross pay for {hoursWorked} hours at ${hourlyRate}/hour is: ${grossPay:.2f}") #print gross pay

tax = 0 #initialize variable

if(grossPay>=0) and (grossPay<=15600):
    tax = 0.105
elif(grossPay>=15601) and (grossPay<=53500):
    tax = 0.175
elif(grossPay>=53501) and (grossPay<=78100):
    tax = 0.3
elif(grossPay>=78101) and (grossPay<=180000):
    tax = 0.33
elif(grossPay>=180001):
    tax = 0.39
else:
    print('Invalid input')

netPay = grossPay - tax #calculate net pay

print(f"Net pay for {hoursWorked} hours at ${hourlyRate}/hour is: ${netPay:.2f}") #print net pay
