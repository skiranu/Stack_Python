'''decimal to binary(2)/octal(8)/Hex(16) conversion using stack'''
num = 25
stack=[]
base = int(input('enter the base of conversion: '))
'''function for conversion'''
def DtoB(num,base):
    s=''
    hex = {
        10:'A',
        11:'B',
        12:'C',
        13:'D',
        14:'E',
        15:'F'
    }
    while num>0:
        stack.append(num%base)
        num = num//base
    while len(stack)!=0:
        temp =  stack.pop()
        if temp >9:
            temp = hex[temp]
        s  = s + str(temp)
    return s
DtoB(num,base)        
