from typing import List, Optional, Union, Tuple


class MathService(object):

    @staticmethod
    def calculate_difference(n: int) -> int:
        square_sum: int = int((n * (n + 1) * (2 * n + 1)) / 6)
        sum_square: int = int((n * (n + 1)) / 2) ** 2

        return sum_square - square_sum

    @staticmethod
    def pythagorean_triplet(a: Union[int, str], b: Union[int, str], c: Union[int, str]) -> Tuple[int, bool]:
        numbers: List[int] = [a, b, c]
        sorted_numbers: List[int] = []
        for num in numbers:
            try:
                x: int = int(num)
                if x <= 0 or x > 1000 or int(x) != float(x):
                    raise Exception('Number %s is not a valid integer between 1 to 1000' % x)
                sorted_numbers.append(x)
            except Exception as e:
                raise Exception('Number %s does not seems to be a valid integer' % num)
        sorted_numbers.sort()

        if sorted_numbers[0]**2 + sorted_numbers[1]**2 == sorted_numbers[2]**2:
            return sorted_numbers[0] * sorted_numbers[1] * sorted_numbers[2], True
        else:
            return sorted_numbers[0] * sorted_numbers[1] * sorted_numbers[2], False

