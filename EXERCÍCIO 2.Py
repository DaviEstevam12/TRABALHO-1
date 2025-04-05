def delta (a,b,c):
'''A) cálculo de discriminante '''

    return (b**2-4*a*c)

def duas_raizes (a,b,c):
    '''B) FUNÇÃO QUE RETOMA MINHAS RAÍZES'''
    
    return ((-b+(delta(a,b,c)**(1/2))))/2*a,((-b-(delta(a,b,c)**(1/2))))/2*a

def vertice (a,b,c):
'''calculo dos vértices da função'''
    return (-b/2*a), (-delta(a,b,c)/4*a)
