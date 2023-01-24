import os


def calc(a, ch, b):
    if ch == '+':
        return a + b
    elif ch == '-':
        return a - b
    elif ch == '/':
        return a / b
    elif ch == '*':
        return a * b

def multi_division(m):
    i = 1
    j = len(m)-2
    while i <= j:
        if m[i] == '*' or m[i] == '/':
            result = calc(int(m.pop(i - 1)), m.pop(i - 1), int(m.pop(i-1)))
            m.insert(i-1, result)
            j -= 2
        else: i += 2
    return m    

def plus_mines(m):
    if len(m) == 1 : return m[0]
    else:
        result = int(m[0])
        for i in range(1, len(m) - 1, 2):
            result = calc(result, m[i], int(m[i + 1]))
        return result

def sol(m):
    r = plus_mines(multi_division(m))
    return r
    
def expression(line):
    m = line.split()
    def calculate (m):
        # print(m)
        if len(m) <= 3 : return sol(m)
        while '(' in m: 
            i = m.index('(')
            j = m.index(')')
            k = m[i:j].count('(')
            if m[i:j].count('(') > 1:
                while k > 1:
                    j = m.index(')', j+1, )
                    k -= 1
                x = calculate(m[i+1:j]) 
                for c in range(i,j+1):
                    m.pop(i)
                m.insert(i, x)
            else:
                x = sol(m[i+1:j])
                for c in range(i,j+1):
                    m.pop(i)
                m.insert(i, x)
        return sol(m)
    return calculate(m)
        
n = '( 10 - 5 ) * ( 2 + 3 ) - 1 + ( 4 * ( 20 - 20 / ( 5 - 1 ) ) )'

os.system('cls')

print('\n',n,'=',expression(n),'\n')