'''Conversion of infix to poostfix'''
'''defining precedence of operators in dictionary'''
def I2P(exp):
    prece = {}
    prece['*'] = 3
    prece['/'] = 3
    prece['+'] = 2
    prece['-'] = 2
    prece['('] = 1
    prece[')'] = 1
    res = ''
    '''stack'''
    op_stack = []

    
    for token in exp:
        if token in 'ABCDEFGHIJKLNMOPQRSTUVWXYZ':
            res = res + token
        elif token in '+*/(' and len(op_stack) == 0:
            op_stack.append(token)
        elif prece[token] > prece[op_stack[0]]:
            op_stack.append(token)
        
        elif prece[token] <= prece[op_stack[0]] and token not in '(':
            temp = op_stack.pop()
            if temp in ' ()':
                continue
            res = res + temp
            while len(op_stack) !=0:
                temp1 = op_stack.pop()
                if temp1 in ' ()':
                    continue
                res = res + temp1

        
            op_stack.append(token)    
    while len(op_stack) != 0:
        temp3 = op_stack.pop()
        if temp3 not in '()':
            res = res + temp   
            
    return res
        

               
I2P('A+B+C+D')
