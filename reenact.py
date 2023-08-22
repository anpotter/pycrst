## Reenacting Rhetorical Structures
## 8/2023, Andrew Potter
## Demonstrates bottom-up construction of coherence

import sys

def get_rel_name(argv):
    return sys._getframe(1).f_code.co_name

def replay(rp):
    if not isinstance(rp, tuple):
        return rp
    exp_list = []
    for arg in rp[1]:
        exp_list.append(replay(arg))
    exp = '{}({})'.format(rp[0],','.join(map(str,exp_list)))
    print(exp)
    return exp

def collect(relname, argv):
    rps=[]
    for arg in argv:
        rps.append(replay(arg))
    return rps

# M & T Relations
def antithesis(*argv): return get_rel_name(argv), argv
def background(*argv): return get_rel_name(argv), argv
def circumstance(*argv): return get_rel_name(argv), argv
def concession(*argv): return get_rel_name(argv), argv
def condition(*argv): return get_rel_name(argv), argv
def elaboration(*argv): return get_rel_name(argv), argv
def enablement(*argv): return get_rel_name(argv), argv
def evaluation(*argv): return get_rel_name(argv), argv
def evidence(*argv): return get_rel_name(argv), argv
def interpretation(*argv): return get_rel_name(argv), argv
def justify(*argv): return get_rel_name(argv), argv
def means(*argv): return get_rel_name(argv), argv
def motivation(*argv): return get_rel_name(argv), argv
def nonvolitional_cause(*argv): return get_rel_name(argv), argv
def nonvolitional_result(*argv): return get_rel_name(argv), argv
def otherwise(*argv): return get_rel_name(argv), argv
def preparation(*argv): return get_rel_name(argv), argv
def purpose(*argv): return get_rel_name(argv), argv
def restatement(*argv): return get_rel_name(argv), argv
def solutionhood(*argv): return get_rel_name(argv), argv
def summary(*argv): return get_rel_name(argv), argv
def unconditional(*argv): return get_rel_name(argv), argv
def unless(*argv): return get_rel_name(argv), argv
def unstated_relation(*argv): return get_rel_name(argv), argv
def volitional_cause(*argv): return get_rel_name(argv), argv
def volitional_result(*argv): return get_rel_name(argv), argv
def conjunction(*argv): return get_rel_name(argv), argv
def contrast(*argv): return get_rel_name(argv), argv
def disjunction(*argv): return get_rel_name(argv), argv
def joint(*argv): return get_rel_name(argv), argv
def list(*argv): return get_rel_name(argv), argv
def restatement_mn(*argv): return get_rel_name(argv), argv
def sequence(*argv): return get_rel_name(argv), argv
def convergence(*argv): return get_rel_name(argv), argv

# outermost function override
def preparation(*argv):
    relname = get_rel_name(argv)
    rps = collect(relname, argv)
    exp = "{}({},{})".format(relname, rps[0], rps[1])
    print(exp)
    return relname, argv

# leading indicators
preparation(1,interpretation(concession(5,6),elaboration(evidence(4,3),2)))





