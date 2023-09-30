'''
Andrew Potter
Azar Score
Computing an RST Metric
Simple 'hello world' example of relational proposition as Python

Citation:
Potter, A. (Accepted). An algorithm for pythonizing rhetorical structures. In DiSLiDaS 2023. 

For more info:
Moshe Azar. 1999. Argumentative text as rhetorical structure:
An application of rhetorical structure theory.
Argumentation, 13(1), 97-114. 
'''

import sys
azar = 0
nonazar = 0

arg_rels = ['antithesis', 'concession','evidence',
            'motivation', 'justify']

def tally(argv):
    global azar
    global nonazar

    relname = sys._getframe(1).f_code.co_name
    if relname in arg_rels:
        azar += 1
    else:
        nonazar += 1
    return relname

def antithesis(*argv): return tally(argv), argv
def background(*argv): return tally(argv), argv
def circumstance(*argv): return tally(argv), argv
def concession(*argv): return tally(argv), argv
def condition(*argv): return tally(argv), argv
def conjunction(*argv): return tally(argv), argv
def contrast(*argv): return tally(argv), argv
def convergence(*argv): return tally(argv), argv
def disjunction(*argv): return tally(argv), argv
def elaboration(*argv): return tally(argv), argv
def enablement(*argv): return tally(argv), argv
def evaluation(*argv): return tally(argv), argv
def evidence(*argv): return tally(argv), argv
def interpretation(*argv): return tally(argv), argv
def joint(*argv): return tally(argv), argv
def justify(*argv): return tally(argv), argv
def list_(*argv): return tally(argv), argv
def means(*argv): return tally(argv), argv
def motivation(*argv): return tally(argv), argv
def nonvolitional_cause(*argv): return tally(argv), argv
def nonvolitional_result(*argv): return tally(argv), argv
def preparation(*argv): return tally(argv), argv
def otherwise(*argv): return tally(argv), argv
def purpose(*argv): return tally(argv), argv
def restatement(*argv): return tally(argv), argv
def restatement_mn(*argv): return tally(argv), argv
def same_unit(*argv): return tally(argv), argv
def sequence(*argv): return tally(argv), argv
def solutionhood(*argv): return tally(argv), argv
def summary(*argv): return tally(argv), argv
def unless(*argv): return tally(argv), argv
def unconditional(*argv): return tally(argv), argv
def volitional_cause(*argv): return tally(argv), argv
def volitional_result(*argv): return tally(argv), argv

############################
# plugin the rp here:
# common cause analysis
motivation(evidence(evidence(justify(10,antithesis(
concession(11,12),13)),antithesis(evidence(condition(4,contrast(5,6)),
concession(2,3)),elaboration(9,condition(8,7)))),1),14)

##################################
print("Argumentative:", azar)
print("Nonargumentative:", nonazar)
print("Azar score:", round(azar / (azar + nonazar),2))
