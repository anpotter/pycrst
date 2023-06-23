# Pretty crummy pretty print for relational propositions

def pcpp(exp):
    indent = 0;
    ppexp = ""
    comma = False
    
    for c in exp:

        if c == '(' :
     
            indent = indent + 1
            ppexp = ppexp + c + '\n' + ('   ' * indent)

        elif c == ' ':
            ppexp = ppexp + c + '\n' + ('   ' * indent)
        
        elif c == ')':
            indent = indent - 1
            ppexp = ppexp + c

        elif comma == True and c.isalpha():
            ppexp = ppexp + '\n' + ('   ' * indent) + c
            
        else:
            ppexp = ppexp + c
            
        comma = False        
        if c == ',':
            comma = True

    return(ppexp)

if __name__ == "__main__":
    "Not lazy"
    exp = 'background(volitional-result(1,circumstance(3,2)),evidence(concession(5,antithesis(7,6)),4))'
    print(pcpp(exp))

