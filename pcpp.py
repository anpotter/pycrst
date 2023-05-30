# Pretty crummy pretty print
# print either the rp or the logical function

##def negation(u):
##    return('negation('+str(u)+')')
##
##def conjunction(n1,n2):
##    return('conjunction('+str(n1) + ', '+ str(n2) + ')')
##
##def condition(s,n):
##    return('implication(' + str(s) + ', ' + str(n) + ')')
##
##def modusponens(s,n):
##    return("modusponens(" + str(s) + ", " + str(n) + ")")
##
##elaboration = preparation = solutionhood = background = motivation = enablement = circumstance = evidence = modusponens
##
##def evaluation(s,n):
##    return("modusponens(" + str(n) + ", " + str(s) + ")")
##
##def antithesis(s,n):
##    return("disjunctiveSyllogism(" + str(s) + "," + str(n) +")")
##
##def concession(s,n):
##    return(modusponens(negation(condition(s, negation(n))),n))


"Not lazy"
#exp ='background(volitional-result(1,circumstance(3,2)),evidence(concession(5,antithesis(7,6)),4))'
#exp = 'background(volitional-result(1,circumstance(3,2)),evidence(concession(5,antithesis(7,6)),4))'

#CC Letter
#exp = 'motivation(conjunction(evidence(justify(10,concession(11,antithesis(12,13))),1),evidence(antithesis(evidence(contrast(5,6),concession(2,3)),elaboration(9,condition(8,7))),1)),14)'
exp = 'motivation(conjunction(evidence(justify(10,concession(11,antithesis(12,13))),1),evidence(antithesis(evidence(contrast(5,6),concession(2,3)),elaboration(9,condition(8,7))),1)),14)'


#exp = 'motivation(conjunction(evidence(justify(10,concession(11,antithesis(12,13))),1),evidence(antithesis(evidence(condition(4,contrast(5,6)),concession(2,3)),elaboration(9,condition(8,7))),1)),14)'

# GUM Worship
#exp = 'preparation(attribution(1,2),circumstance(3,background(16,background(concession(attribution(10,11),9),background(background(8,result(7,6)),attribution(4,5))))))'
#exp = 'preparation(attribution(1,2),circumstance(3,background(16,background(concession(attribution(10,11),9),background(background(8,result(7,6)),attribution(4,5))))))'
#exp = 'preparation(attribution(1,2),circumstance(3,background(contrast(12,concession(14,13)),background(concession(attribution(10,11),9),background(background(8,result(7,6)),attribution(4,5))))))'


# syncom
#exp = 'solutionhood(1,conjunction(motivation(elaboration(10,circumstance(3,purpose(5,4))),2),enablement(purpose(13,enablement(16,15)),2)))'
#exp = 'solutionhood(1,conjunction(motivation(conjunction(elaboration(10,18),circumstance(3,purpose(5,4)),elaboration(circumstance(7,6),18),elaboration(antithesis(8,9),18),elaboration(antithesis(11,12),18)),2),enablement(purpose(13,enablement(16,15)),2)))'



# misc
exp = 'conjunction(condition(circumstance(background(antithesis(1,2),3),4),5),elaboration(antithesis(means(7,evidence(9,8)),6),5))'
exp ="background(volitional-result(1, circumstance(3,2)), evidence(concession(5, antithesis(7,6)),4))"

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

