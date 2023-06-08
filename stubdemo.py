# stubdemo
# simple how-to for generated stubs
# returns a nested tuple for the expression
# the relational proposition is from the
# Common Cause analysis

import sys

def get_rel_name(argv):
    return sys._getframe(1).f_code.co_name

def antithesis(*argv): return get_rel_name(argv), argv
def circumstance(*argv): return get_rel_name(argv), argv
def concession(*argv): return get_rel_name(argv), argv
def condition(*argv): return get_rel_name(argv), argv
def elaboration(*argv): return get_rel_name(argv), argv
def evidence(*argv): return get_rel_name(argv), argv
def justify(*argv): return get_rel_name(argv), argv
def motivation(*argv):
    exp =  get_rel_name(argv), argv
    print(exp)

motivation(
   evidence(
      evidence(
         justify(
            10,
            antithesis(
               concession(
                  11,12),13)),
         antithesis(
            evidence(
               condition(
                  4,
                  circumstance(
                     6,5)),
               concession(
                  2,3)),
            elaboration(
               9,
               condition(
                  8,7)))),1),14)
