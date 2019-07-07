def faculteit(n):
    if n == 1:
        return 1
    else:
        print('{} * facutleit({})'.format(n, n-1))
        res = faculteit(n - 1)
        print('{} * {} = {}'.format(n, res, n * res))
        return n * res

def isPalindroom(woord):

    if len(woord) == 1 or len(woord) == 0:
        return True
    else:
        print('{} == {} and isPalindroom({})'.format(woord[0], woord[-1], woord[1:-1]))
        res = isPalindroom(woord[1: -1])
        print('{} and {}'. format(woord[0] == woord[-1], res))
        return woord[0] == woord[-1] and res

print(isPalindroom('demooiezeemannamannameezeied'))

