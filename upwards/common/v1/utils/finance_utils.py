import math
from math_utils import positive_ceil, ceil


def get_tenure(principal, emi, interest_rate):
    numerator = math.log((emi * 1.0) / (emi - principal * interest_rate))
    denominator = math.log(1.0 + interest_rate)
    return ceil(numerator / denominator)


def get_emi(principal, tenure, interest_rate):
    numerator = principal * 1.0 * interest_rate
    denominator = (1.0 - (1 + interest_rate)**(-1 * tenure))
    return positive_ceil((numerator / denominator), 0)
