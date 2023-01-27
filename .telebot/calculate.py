sign = '^*/+-'

def bracket_space(line):
    m = list(line)
    while ' ' in m:
        m.remove(' ')
    i = 0
    while i < len(m)-1 :
        if  (str(m[i]) + str(m[i+1]) ).isdigit() or (str(m[i]).isdigit() and str(m[i+1]).find('.') > -1)    or (str(m[i]).find('.') > -1 and str(m[i+1]).isdigit())     :
            new_i1 = m.pop(i) + m.pop(i)
            m.insert(i, new_i1)
            continue
        elif  (str(m[i]) in sign and str(m[i+1]) in sign) or  str(m[i]) == '(' and str(m[i+1]) == '-':
            new_i2 = m.pop(i+1) + m.pop(i+1)
            m.insert(i+1, new_i2)            
                    
        i += 1 
    else: return m

def calc(a, ch, b):
    if ch == '+':
        return a + b
    elif ch == '-':
        return a - b
    elif ch == '/':
        if b == 0 :
            print('\nДеление на 0. Проверьте выражение\n') 
            exit()
        return a / b
    elif ch == '*':
        return a * b
    elif ch == '^':
        return a ** b    

def raised_power(m):
    i = 1
    j = len(m)-2
    while i <= j:
        if m[i] == '^':
            result = calc(float(m.pop(i - 1)), m.pop(i - 1), float(m.pop(i-1)))
            m.insert(i-1, result)
            j -= 2
        else: i += 2
    return m   

def multi_division(m):
    i = 1
    j = len(m)-2
    while i <= j:
        if m[i] == '*' or m[i] == '/':
            result = calc(float(m.pop(i - 1)), m.pop(i - 1), float(m.pop(i-1)))
            m.insert(i-1, result)
            j -= 2
        else: i += 2
    return m    

def plus_mines(m):
    if len(m) == 1 : return m[0]
    else:
        result = float(m[0])
        for i in range(1, len(m) - 1, 2):
            result = calc(result, m[i], float(m[i + 1]))
        return result

def solution(m):
    if len(m) < 3 : return m[0]
    r = plus_mines(multi_division(raised_power(m)))
    return r
    
def expression(line):
    m = bracket_space(line)
    def calculate (m):
        if len(m) <= 3 : return solution(m)
        while '(' in m: 
            i = m.index('(')
            j = m.index(')')
            k = m[i:j].count('(')
            s = m[i:j+1].count(')')
            if k > s:
                while k > s:
                    j = m.index(')', j+1, )
                    k = m[i:j].count('(')
                    s = m[i:j+1].count(')')
                x = calculate(m[i+1:j]) 
                for c in range(i,j+1):
                    m.pop(i)
                m.insert(i, x)
            else:
                x = solution(m[i+1:j])
                for c in range(i,j+1):
                    m.pop(i)
                m.insert(i, x)
        return solution(m)
    return calculate(m)