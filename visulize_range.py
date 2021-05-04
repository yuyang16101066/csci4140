def testYearMonth(string):
    import re
    '''write your code here'''
    
    pattern = "^(\d{1,4})\.(\d{1,2})$"
    m = re.search(pattern, string)
    year = int(m.groups()[0])
    month = int(m.groups()[1])
    if m:
        if 1 <= year <= 3000 and 1 <= month <= 12:
            print("Valid pair")
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                print("The year is a leap year")
            else:
                print("The year is not a leap year")
        else:
            print("Invalid pair")
    else:
        print("Invalid pair")

string = "2020.05"
testYearMonth(string)
