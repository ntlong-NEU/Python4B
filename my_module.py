print('the module is imported')

data = 'đây là dữ liệu test'

def even(n:int)->bool:
    return n%2==0

def is_prime(n:int)->bool:
    if n<=1:
        return False
    else:
        for d in range(2,int(n**0.5)+1):
            if n%d==0:
                return False
        return True