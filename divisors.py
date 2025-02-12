def divisors(n):
    """
    Returns a list6 of divisors of n
    :param n: The number we get as input
    :return: A list of integers
    """
    divisors=[1, n]# start with an empty list
    for i in range(2,n//2+1):
        if n%i==0:
            divisors.append(i)
    return divisors

print(divisors(100))