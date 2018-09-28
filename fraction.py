import unittest

class Fraction:
    ''' A fraction class that will help us define simple fractions.
        The class will operate operations like add, subtract, multiply and divide.
        It will also test 2 fractions for equality.
    '''
    def __init__(self, num, denom):
        ''' Constructor to define a fraction '''

        # assign -ve to numerator only if either num or denom is -ve
        # ^ is the XOR operator
        self.numerator = (abs(num) * -1) if (num < 0) ^ (denom < 0) else abs(num)
        if denom != 0:
            self.denominator = abs(denom)
        else:
            raise ValueError('\nDenominator cannot be 0!')

    def __add__(self, fraction):
        ''' returns a new instance of class Fraction with the sum of self and other where other is another Fraction '''
        common_denom = self.denominator * fraction.denominator
        common_num = (self.numerator * fraction.denominator) + (fraction.numerator * self.denominator)

        return Fraction(common_num, common_denom)

    def __sub__(self, fraction):
        '''  returns a new instance of class Fraction with the difference of self and other where other is another Fraction '''
        common_denom = self.denominator * fraction.denominator
        common_num = (self.numerator * fraction.denominator) - (fraction.numerator * self.denominator)

        return Fraction(common_num, common_denom)

    def __mul__(self, fraction):
        '''  returns a new instance of class Fraction with the product of self and other where other is another Fraction '''
        common_num = self.numerator * fraction.numerator
        common_denom = self.denominator * fraction.denominator

        return Fraction(common_num, common_denom)

    def __truediv__(self, fraction):
        '''  returns a new instance of class Fraction with the quotient of self and other where other is another Fraction '''
        common_num = self.numerator * fraction.denominator
        common_denom = self.denominator * fraction.numerator

        return Fraction(common_num, common_denom)

    def __eq__(self, fraction):
        ''' Tests if this instance of the fraction is equal to the one passed as argument.
                Returns True if equal, otherwise, False '''
        return (self.numerator * fraction.denominator == self.denominator * fraction.numerator)

    def __ne__(self, fraction):
        ''' Returns True if this instance of the fraction is not equal to the one passed as argument.
            Returns False otherwise. '''
        return not self.__eq__(fraction)

    def __lt__(self, fraction):
        ''' Returns True if this instance of the fraction is less than the one passed as argument.
            Returns False otherwise. '''
        return (self.numerator * fraction.denominator < self.denominator * fraction.numerator)

    def __le__(self, fraction):
        ''' Returns True if this instance of the fraction is less than or equal to the one passed as argument.
            Returns False otherwise. '''
        return (self.numerator * fraction.denominator <= self.denominator * fraction.numerator)

    def __gt__(self, fraction):
        ''' Returns True if this instance of the fraction is greater than the one passed as argument.
            Returns False otherwise. '''
        return not self.__le__(fraction)

    def __ge__(self, fraction):
        ''' Returns True if this instance of the fraction is greater than or equal to the one passed as argument.
            Returns False otherwise. '''
        return not self.__lt__(fraction)

    def __str__(self):
        ''' Returns a string representation of the fraction '''
        return '0' if self.numerator == 0 else '{}/{}'.format(self.numerator, self.denominator)

    #  TODO: Refactor this to use range which will shorten it
    def simplify(self):
        ''' simplify the fraction into it's smallest possible representation '''
        minimum = min(abs(self.numerator), abs(self.denominator))
        gcf = None

        while minimum >=2:
            if self.numerator % minimum == 0 and self.denominator % minimum == 0:
                gcf = minimum
                break
            else:
                minimum -= 1

        if gcf is not None:
            simplifiedNumerator = int(self.numerator / gcf)
            simplifiedDenominator = int(self.denominator / gcf)
            return Fraction(simplifiedNumerator, simplifiedDenominator)
        else:
            return Fraction(self.numerator, self.denominator)

class FractionTest(unittest.TestCase):
    ''' Test class to unit test the Fraction class implementation '''

    def test_init(self):
        ''' Test the __init__ '''
        fractionTest = Fraction(1, 2)
        self.assertEqual(fractionTest.numerator, 1)
        self.assertEqual(fractionTest.denominator, 2)

    def test_init_error(self):
        ''' Test __init__ when denominator is zero '''
        with self.assertRaises(ValueError):
            Fraction(9, 0)

    def test_str(self):
        ''' Test __str__ '''
        fraction = Fraction(5, 9)
        self.assertEqual(str(fraction), '5/9')

    def test_str_zero(self):
        ''' Test __str__ when numerator is 0 '''
        fraction = Fraction(0, 101)
        self.assertEqual(str(fraction), '0')

    def test_str_negative(self):
        ''' Test __str__ for either num or denom is -ve '''
        fraction = Fraction(-5, 8)
        self.assertEqual(str(fraction), '-5/8')

    def test_str_both_negative(self):
        ''' Test __str__ for both num and denom is -ve '''
        fraction = Fraction(-5, -8)
        self.assertEqual(str(fraction), '5/8')

    def test_equals(self):
        ''' Test the == operation '''
        f12 = Fraction(1,2)
        f34 = Fraction(3,4)
        f24 = Fraction(2,4)

        self.assertTrue(f12 == f12)
        self.assertTrue(f34 == f34)
        self.assertTrue(f24 == f12)
        self.assertFalse(f24 == f34)
        self.assertTrue(Fraction(-1,2) == Fraction(-2,4))

    def test_add(self):
        ''' test the + operation '''
        f12 = Fraction(1, 2)
        f44 = Fraction(4, 4)

        self.assertEqual(f12 + f12, f44)
        self.assertEqual(f12 + f44, Fraction(12,8))
        self.assertEqual(f12 + f12 +f12, Fraction(3, 2))

    def test_minus(self):
        ''' test the - operation '''
        f128 = Fraction(12, 8)
        f12 = Fraction(1, 2)

        self.assertEqual(f128 - f12, Fraction(16, 16))

    def test_times(self):
        ''' test the * operation '''
        f32 = Fraction(3, 2)
        f12 = Fraction(1, 2)

        self.assertEqual(f12 * f32, Fraction(3,4))

    def test_divide(self):
        ''' test the / operation '''
        f128 = Fraction(12, 8)
        f32 = Fraction(3, 2)

        self.assertEqual(f128 / f32, Fraction(24, 24))

    def test_ne(self):
        ''' test the != operation '''
        f12 = Fraction(1,2)
        f34 = Fraction(3,4)
        f24 = Fraction(2,4)

        self.assertTrue(f12 != f34)
        self.assertFalse(f12 != f24)

    def test_lt(self):
        ''' test the < opeeration '''
        f12 = Fraction(1,2)
        f34 = Fraction(3,4)

        self.assertTrue(f12 < f34)
        self.assertFalse(Fraction(5,2) < Fraction(2,5))
        self.assertTrue(Fraction(-1, 2) < Fraction(1, -3))

    def test_le(self):
        ''' test the <= operation '''
        f12 = Fraction(1,2)
        f34 = Fraction(3,4)

        self.assertTrue(f12 <= f12)
        self.assertTrue(f12 <= f34)
        self.assertTrue(Fraction(-1, 2) <= Fraction(1, -3))
        self.assertTrue(Fraction(-1, 2) <= Fraction(-1, 3))

    def test_gt(self):
        ''' test the > operation '''
        f12 = Fraction(1,2)
        f34 = Fraction(3,4)

        self.assertFalse(f12 > f12)
        self.assertTrue(f34 > f12)
        self.assertTrue(Fraction(1, -3) > Fraction(-1, 2))
        self.assertTrue(Fraction(-1, 3) > Fraction(-1, 2))
        self.assertFalse(Fraction(-1, -3) > Fraction(-1, -2))

    def test_ge(self):
        ''' test the >= operation '''
        f12 = Fraction(1,2)
        f34 = Fraction(3,4)

        self.assertTrue(f12 >= f12)
        self.assertTrue(f34 >= f12)
        self.assertTrue(Fraction(1, -3) >= Fraction(-1, 2))
        self.assertTrue(Fraction(-1, 3) >= Fraction(-1, 2))
        self.assertFalse(Fraction(-1, -3) >= Fraction(-1, -2))

    def test_simplify(self):
        ''' test the simplify method '''
        self.assertEqual(str(Fraction(4, 18).simplify()), str(Fraction(2, 9)))
        self.assertEqual(str(Fraction(-4, -18).simplify()), str(Fraction(2, 9)))
        self.assertEqual(str(Fraction(4, -18).simplify()), str(Fraction(-2, 9)))
        self.assertEqual(str(Fraction(9, 27).simplify()), str(Fraction(1, 3)))
        self.assertEqual(str(Fraction(4,2).simplify()), str(Fraction(2,1)))
        self.assertEqual(str(Fraction(63, -63).simplify()), str(Fraction(-1, 1)))
        self.assertEqual(str(Fraction(2,-1).simplify()), str(Fraction(-2, 1)))
        self.assertEqual(str(Fraction(-1,-1).simplify()), str(Fraction(1, 1)))
