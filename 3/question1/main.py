import profile
import timeit


def binomial_coefficient(n, k):
    # Calculate factorials
    if n==0:
        return 1
    elif k==0:
        return 1
    else:
        return binomial_coefficient(n-1,k-1)+binomial_coefficient(n-1,k)
    # numerator = 1
    # for i in range(k):
    #     numerator *= (n - i)
    # denominator = 1
    # for i in range(1, k + 1):
    #     denominator *= i
    # return numerator // denominator


def binomial_coefficient2(n, k):
    # Create table
    # Dynamic pro
    table = [[0] * (k + 1) for i in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                table[i][j] = 1
            else:
                table[i][j] = table[i - 1][j - 1] + table[i - 1][j]
    return table[n][k]


def print_number(num):
    num_str = '{:0.10f}'.format(num)
    print(num_str)


if __name__ == '__main__':
    print("The number of ways to solve the problem with input (10, 5) ->")
    print("division and solution time : ")
    div = timeit.timeit(stmt='binomial_coefficient(10, 5)', setup='from __main__ import binomial_coefficient',
                        number=5)
    print_number(div)
    print("dynamic time : ")
    div = timeit.timeit(stmt='binomial_coefficient2(10, 5)', setup='from __main__ import binomial_coefficient2',
                        number=5)
    print_number(div)

