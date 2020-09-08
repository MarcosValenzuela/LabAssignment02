import math
"""
 get inputgirt 
 devide sheets by 5
round up
print output
"""
sheets = 16

def calculate(sheets):
    answer = sheets/5
    print('-------------------------')
    print('Sheets:', sheets)
    print('The answer is: ',answer)
    stamps = math.ceil(answer)
    print ('Rounded:',stamps,'!')
    print('-------------------------')
    return stamps
output = calculate(16)

print("the return statement is: ", output)