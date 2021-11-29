import math


def properFactors(n):
    """ Returns a list of the factors of n, not including n """
    factors = [1]
    for x in range(2, int(math.sqrt(n)) + 1):
        if n % x == 0:
            factors.append(x)
            if n // x != x:
                factors.append(n // x)
    return factors


def factors(n):
    """ Returns a list of the factors of n """
    factors = []
    for x in range(1, int(math.sqrt(n)) + 1):
        if n % x == 0:
            factors.append(x)
            if n // x != x:
                factors.append(n // x)
    return factors


def sigma(n):
    """ The divisor function """
    return sum(factors(n))


def aliquotSum(n):
    return sum(properFactors(n))


# Does some subset of arr sum to "sum"?
def doesSubsetSum(arr, sum):
    """ Returns true if some subset of arr sums to 'sum' """
    # Each index "i" of dyn represents whether a subset of arr can sum to i.
    dyn = [True] + [False] * (sum + 1)
    for x in arr:
        for y in range(sum, x - 1, -1):
            if dyn[y - x]:
                dyn[y] = True
    return dyn[sum]


def isPerfect(n):
    return aliquotSum(n) == n


def isSemiPerfect(n):
    return doesSubsetSum(properFactors(n), n)


def isAbundant(n):
    return aliquotSum(n) > n


if __name__ == "__main__":

    index = 1
    print("n\t:: sigma(n), (n*2.54)")
    for i in range(2, 1000000000):
        a = sigma(i)
        b = i * 2.54
        if a == round(b):
            print(str(i) + "\t:: " + str(a) + ", " + str(b))
