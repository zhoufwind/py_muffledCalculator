class MuffledCalculator:
    _muffled = False
    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self._muffled:
                print 'Division by zero is illegal'
            else:
                raise

calculator = MuffledCalculator()
print calculator.calc('10/2')

#print calculator.calc('10/0')

calculator._muffled = True
print calculator.calc('10/0')