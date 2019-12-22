import sympy as sym
from sympy.printing.ccode import C99CodePrinter
from sympy.printing.codeprinter import Assignment

sym.init_printing()

class CMatrixPrinter(C99CodePrinter):
    def _print_ImmutableDenseMatrix(self, expr):
        sub_exprs, simplified = sym.cse(expr)
        lines = []
        M = sym.MatrixSymbol('M', simplified[0].shape[0], simplified[0].shape[1])
        lines.append('num_rows = ' + str(simplified[0].shape[0]) + ';')
        lines.append('num_cols = ' + str(simplified[0].shape[1]) + ';')
        lines.append('size = ' + str(len(simplified[0])) + ';')
        for var, sub_expr in sub_exprs:
            lines.append('double ' + self._print(Assignment(var, sub_expr)))
        return '\n'.join(lines) + '\n' + self._print(Assignment(M, simplified[0]))
