

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp


class ValidationAndPloting:
    def __init__(self, equation, domain, excepted_Points):
        self.stack = []
        self.opening_symbols = {'(': ')', '[': ']', '{': '}'}
        self.valid_operators = {'+', '-', '*', '/', '^'}
        self.valid_chars = set('0123456789x')
        self.equation = equation
        self.domain = domain
        self.excepted_Points = excepted_Points

    def is_equation_valid(self, equation):
        equation = self._remove_whitespace(equation)

        if not equation or not self._is_valid_chars(equation) or not self._is_valid_start_end(equation):
            return False

        for i in range(len(equation) - 1):
            current_char = equation[i]
            next_char = equation[i + 1]

            if current_char in self.opening_symbols.keys():
                self.stack.append(current_char)
                if next_char not in self.valid_chars:
                    return False
            elif current_char in self.opening_symbols.values():
                if len(self.stack) == 0 or current_char != self.opening_symbols[self.stack[-1]]:
                    return False
                self.stack.pop()
                if next_char in self.valid_operators:
                    continue
            elif current_char in self.valid_chars and next_char in self.valid_chars:
                if next_char != 'x':
                    continue
                return False  # Two consecutive valid characters (e.g., "x2")
            elif current_char in self.valid_chars and next_char in self.valid_operators:
                continue  # Valid character followed by a valid operator
            elif current_char in self.valid_operators and next_char in self.valid_chars:
                continue  # Valid operator followed by a valid character
            elif current_char in self.valid_operators and next_char in self.opening_symbols.keys():
                continue
            elif current_char in self.valid_chars and next_char in self.opening_symbols.values():
                continue
            else:
                return False  # Invalid operator placement or consecutive operators

        return len(self.stack) == 0

    def _remove_whitespace(self, equation):
        return equation.replace(" ", "")

    def _is_valid_chars(self, equation):
        return set(equation).issubset(self.valid_chars.union(self.valid_operators, self.opening_symbols.keys(), self.opening_symbols.values()))

    def _is_valid_start_end(self, equation):
        return (equation[0] in self.valid_chars or equation[0] in self.opening_symbols.keys()) and (equation[-1] in self.valid_chars or equation[-1] in self.opening_symbols.values())

    def check_domanin_excepted_validation(self, domain, state = None):

        for item in range(len(domain)):
            try:
                domain[item] = float(domain[item])
            except ValueError:
                return False
        if domain and state == "domain":
            if domain[0] > domain[1]:
                return False
        return domain

    def check_excepted_Points(self, excepted_Points):
        if excepted_Points:
            excepted_Points = [item for item in excepted_Points.split(',')]
            return self.check_domanin_excepted_validation(excepted_Points, "excepted")
    
    def Get_Result(self):
            return self.is_equation_valid(self.equation), self.check_domanin_excepted_validation(self.domain, "domain"),self.check_excepted_Points(self.excepted_Points )
    



