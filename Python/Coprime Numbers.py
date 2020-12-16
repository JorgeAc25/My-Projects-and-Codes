'''
Sophia is playing a game on the computer. There are two random arrays A & B, each having the same number of elements.
The game begins with Sophia removing a pair (A , B ) from the array if they are not co-prime. She keeps a count on the
number of times this operation is done.
Sophia wants to find out the maximal number of times(S) she can do this on the arrays. Could you help Sophia find
the value?

Sample Input
4
2 5 6 7
4 9 10 12

Sample Output
3
'''

from math import gcd as bltin_gcd

n = int(input())
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))


def coprime(a, b):
    return bltin_gcd(a, b) == 1


def game(a, b):
    list_a = []
    list_b = []
    for i in b:
        if [x for x in a if not coprime(x, i)]:
            list_a.append(i)

    for i in a:
        if [x for x in b if not coprime(x, i)]:
            list_b.append(i)

    return min([len(list_b), len(list_a)])


print(game(a, b))
