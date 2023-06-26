# relational proposition as code
import sys

def debug(*arg):
    frameinfo = currentframe()
    print(frameinfo.f_back.f_lineno,":",*arg)
    input()

def get_rel_name(argv):
    return sys._getframe(1).f_code.co_name

def antithesis(*argv): return get_rel_name(argv), argv
def background(*argv): return get_rel_name(argv), argv
def circumstance(*argv): return get_rel_name(argv), argv
def concession(*argv): return get_rel_name(argv), argv
def condition(*argv): return get_rel_name(argv), argv
def condition(*argv): return get_rel_name(argv), argv
def conjunction(*argv): return get_rel_name(argv), argv
def contrast(*argv): return get_rel_name(argv), argv
def convergence(*argv): return get_rel_name(argv), argv
def disjunction(*argv): return get_rel_name(argv), argv
def elaboration(*argv): return get_rel_name(argv), argv
def enablement(*argv): return get_rel_name(argv), argv
def evaluation(*argv): return get_rel_name(argv), argv
def evidence(*argv): return get_rel_name(argv), argv
def interpretation(*argv): return get_rel_name(argv), argv
def joint(*argv): return get_rel_name(argv), argv
def justify(*argv): return get_rel_name(argv), argv
def list(*argv): return get_rel_name(argv), argv
def means(*argv): return get_rel_name(argv), argv
def motivation(*argv): return get_rel_name(argv), argv
def nonvolitional_cause(*argv): return get_rel_name(argv), argv
def nonvolitional_result(*argv): return get_rel_name(argv), argv
def preparation(*argv): return get_rel_name(argv), argv
def otherwise(*argv): return get_rel_name(argv), argv
def purpose(*argv): return get_rel_name(argv), argv
def restatement(*argv): return get_rel_name(argv), argv
def restatement_mn(*argv): return get_rel_name(argv), argv
def same_unit(*argv): return get_rel_name(argv), argv
def sequence(*argv): return get_rel_name(argv), argv
def solutionhood(*argv): return get_rel_name(argv), argv
def summary(*argv): return get_rel_name(argv), argv
def unless(*argv): return get_rel_name(argv), argv
def unconditional(*argv): return get_rel_name(argv), argv
def volitional_cause(*argv): return get_rel_name(argv), argv
def volitional_result(*argv): return get_rel_name(argv), argv


# override default function

def motivation(*argv):
    name = get_rel_name(argv)
    print('\n(\'{}\', ({}))'.format(name, argv))
    return name, argv

print('common cause')
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
                  contrast(
                     5,6)),
               concession(
                  2,3)),
            elaboration(
               9,
               condition(
                  8,7)))),1),14)
