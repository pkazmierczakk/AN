import math


class EPowerX:
    def __init__(self, x, diff=False, precision=10 ** -16):
        self.precision = precision
        self.x = x
        self.diff_from_buildin_func = diff
        self.def_partial_sums = [] # zapisane aby dwa razy nie liczyć tego samego
        self.rec_partial_sums = [] # zapisane aby dwa razy nie liczyć tego samego
        self.build_in_result = None # zapisane aby dwa razy nie liczyć tego samego

    def func(self, x, n):  # TODO replace build in functions
        return (x ** n) / (math.factorial(n))

    def _is_good_precision(self, elem, n):
        # To tylko na teraz jest tak zrobione bo wyniki są podobne jak przy ograniczeniu z góry
        return self.precision > elem

    def get_partial_sums_from_definition(self):
        if not self.def_partial_sums:
            elem = 1
            n = 0
            while not self._is_good_precision(elem, n):
                self.def_partial_sums.append(elem)
                n += 1
                elem = self.func(self.x, n)

        return self.def_partial_sums

    def get_partial_from_recursion(self):
        if len(self.rec_partial_sums) <= 1:
            elem = 1
            n = 0
            while not self._is_good_precision(elem, n):
                self.rec_partial_sums.append(elem)
                n += 1
                elem *= self.x / (n + 1)

        return self.rec_partial_sums

    def compute_exp(self, method="def", reverse=False):
        if method == "def":
            series = self.get_partial_sums_from_definition()
        else:
            series = self.get_partial_from_recursion()

        if reverse:
            series.reverse()

        result = 0

        for s in series:
            result += s

        if self.diff_from_buildin_func:
            return abs(result - self.compute_from_build_in_func())

        return result

    def compute_from_build_in_func(self):
        if self.diff_from_buildin_func:
            self.build_in_result = math.exp(self.x)
        return self.build_in_result