class MathService(object):

    @staticmethod
    def calculate_difference(n: int) -> int:
        square_sum: int = int((n * (n + 1) * (2 * n + 1)) / 6)
        sum_square: int = int((n * (n + 1)) / 2) ** 2

        return sum_square - square_sum
