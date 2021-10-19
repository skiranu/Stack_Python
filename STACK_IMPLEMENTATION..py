'''Balancing Parenthesis'''
def checkpara():
    '''Input string'''
    l = '{}({[(([{[]}({()()}{})[]]))]}[])'
    
    '''dictionary for K,V pairs'''
    check={
        '(':')',
        '[':']',
        '{':'}'
    }
    
    '''temp variables'''
    temp=[]
    index = 0
    balanced = True
    
    '''main logic'''
    while index < len(l) and balanced:
        if l[index] in '[{(':
            temp.append(l[index])
        elif len(temp) != 0:
            if check[temp.pop()] == l[index]:
                balanced = True
            else:
                balanced = False
        else:
            balanced =False
        index += 1
    if len(temp) == 0 and balanced:
        balanced = True
    else:
        balanced = False
    return balanced
'''function call'''
checkpara()
