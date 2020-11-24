#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution():
    """
    Class Solution is to convert
    Roman numbers to Arabic
    """

    # Dict of corresponding Roman to Numbers
    rule = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    # Each element is less because first we just add a first element
    # and then convert a pair of literals if right literal is
    # more than left
    rule_div = {
        ('I', 'V'): 3,
        ('I', 'X'): 8,
        ('X', 'L'): 30,
        ('X', 'C'): 80,
        ('C', 'D'): 300,
        ('C', 'M'): 800,
    }


    def romanToInt(self, s: str) -> int:
        """
        This function converts a Roman number to Arabic one
        :param s:   input string of Roman number
        :return:    result an Arabic number
        """

        roman_number = s.upper()
        if roman_number:
            # Check if Roman numbers count less then 15
            if len(roman_number) > 15:
                return 'Incorrect input number'

            result_number = 0
            prev_literal = None
            for literal in roman_number:
                # Check if prev_literal less than literal
                if prev_literal and self.rule[prev_literal] < self.rule[literal]:
                    # Add a corresponding number for prev_literal and literal
                    result_number += self.rule_div[(prev_literal, literal)]
                else:
                    # Just add a corresponding number for literal
                    result_number += self.rule[literal]
                prev_literal = literal

            return result_number

        return 'Incorrect input number'


    def test_romanToInt(self):
        '''
        Test function to check romanToInt() function
        '''
        assert self.romanToInt('III') == 3
        assert self.romanToInt('IV') == 4
        assert self.romanToInt('IX') == 9
        assert self.romanToInt('LVIII') == 58
        assert self.romanToInt('MCMXCIV') == 1994

        assert self.romanToInt('I') == 1
        assert self.romanToInt('II') == 2
        assert self.romanToInt('III') == 3
        assert self.romanToInt('IV') == 4
        assert self.romanToInt('V') == 5
        assert self.romanToInt('VI') == 6
        assert self.romanToInt('VII') == 7
        assert self.romanToInt('VIII') == 8
        assert self.romanToInt('IX') == 9
        assert self.romanToInt('X') == 10
        assert self.romanToInt('XXXI') == 31
        assert self.romanToInt('XLVI') == 46
        assert self.romanToInt('XCIX') == 99
        assert self.romanToInt('DLXXXIII') == 583
        assert self.romanToInt('DCCCLXXXVIII') == 888
        assert self.romanToInt('MDCLXVIII') == 1668
        assert self.romanToInt('MCMLXXXIX') == 1989
        assert self.romanToInt('MMX') == 2010
        assert self.romanToInt('MMXII') == 2012
        assert self.romanToInt('MMMCMXCIX') == 3999

        print('All tests Passed!')


if __name__ == '__main__':
    # Create an instance of Solution() class
    solution = Solution()
    # Test function
    solution.test_romanToInt()
    # Ask user for Arabic number for input
    s = input('Input: ')
    while s != 'q':
        # Convert Roman number to Arabic
        result = solution.romanToInt(s)
        print(f'Output: {result}')
        s = input('Input: ')
