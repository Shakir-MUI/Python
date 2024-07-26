class Storage:
    def __init__(self):
        self.data = 0.0
        self.help_text = """
Data :   0.0
>>>>: + 10
Data :   10.0
>>>>: * 100
Data :   1000.0
>>>>: / 10
Data :   100.0
>>>>: % 9
Data :   1.0
>>>>: - 1
Data :   0.0
>>>>: + 1
Data :   1.0
>>>>: + 2
Data :   3.0
>>>>: ** 3
Data :   27.0
>>>>: // 3
Data :   9.0
>>>>: / 2
Data :   4.5
>>>>: exit 0
        """

class Calculator(Storage):
    def add(self,a,b):
        self.data = a + b

    def subtract(self,a,b):
        self.data = a - b

    def multiply(self,a,b):
        self.data = a * b

    def divide(self,a,b):
        if b != 0:
            self.data = a / b
        else:
            raise ZeroDivisionError("Cannot divide by zero")

    def floor_divide(self,a,b):
        if b != 0:
            self.data = a // b
        else:
            raise ZeroDivisionError("Cannot floor divide by zero")

    def power(self,a,b):
        self.data = a ** b

    def modulus(self,a,b):
        if b != 0:
            self.data = a % b
        else:
            raise ZeroDivisionError("Cannot perform modulus operation with zero")

    def validate(self,query):
        self.valid = False
        self.q = query.split()
        if len(self.q) == 2:
            self.op, self.number = self.q[0], self.q[1]
            if self.op in "+-**/*//%":
                try:
                    self.number = float(self.number)
                    self.valid = True
                except TypeError as e:
                    print("Wrong number type",e)
                except Exception as e:
                    print("invalid",e)
            elif self.op == "exit":
                print("Good-bye")
                quit()
            elif self.op == "help":
                print(self.help_text)
            else:
                print("Wrong opeartory type",self.op)
        else:
            self.number = 0
            self.op = ""
            print("Wrong number of arguments")

        return [self.valid,self.op,self.number]

    def __str__(self):
        return f'Data : \t {self.data}'


obj = Calculator()
print(obj)
print("Enter an expression:")
while True:
    query = input(">>>>\t ")
    valid, op, number = obj.validate(query)
    if valid:
        if op == '+':
            obj.add(obj.data, number)
        elif op == '-':
            obj.subtract(obj.data, number)
        elif op == '*':
            obj.multiply(obj.data, number)
        elif op == '/':
            obj.divide(obj.data, number)
        elif op == '//':
            obj.floor_divide(obj.data, number)
        elif op == '**':
            obj.power(obj.data, number)
        elif op == '%':
            obj.modulus(obj.data, number)
        else:
            print("Invalid operator")
    else:
        print("Invalid expression")
    
    print(obj)