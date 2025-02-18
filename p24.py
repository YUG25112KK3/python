class Calculator:
    def addition(self,*args):
        return sum(args)

c=Calculator()
print(f'addition of 1 value:{c.addition(5)}')
print(f'addition of 2 value:{c.addition(5,10)}')
print(f'addition of 3 value:{c.addition(5,10,15)}')
print(f'addition of 4 value:{c.addition(5,10,15,20)}')
