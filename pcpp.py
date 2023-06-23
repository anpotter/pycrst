# Pretty crummy pretty print for relational propositions

"Not lazy"
#exp ='background(volitional-result(1,circumstance(3,2)),evidence(concession(5,antithesis(7,6)),4))'
#exp = 'background(volitional-result(1,circumstance(3,2)),evidence(concession(5,antithesis(7,6)),4))'

#CC Letter
#exp = 'motivation(conjunction(evidence(justify(10,concession(11,antithesis(12,13))),1),evidence(antithesis(evidence(contrast(5,6),concession(2,3)),elaboration(9,condition(8,7))),1)),14)'




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

#print(pcpp(exp))

