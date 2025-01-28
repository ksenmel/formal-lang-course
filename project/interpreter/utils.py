from functools import reduce

from pyformlang.regular_expression import Regex
from pyformlang.finite_automaton import EpsilonNFA, Symbol
from typing import Optional
from pyformlang.rsa import RecursiveAutomaton, Box


def nfa_from_char(char: str) -> EpsilonNFA:
    return Regex(char).to_epsilon_nfa()


def nfa_from_var(var_name: str) -> EpsilonNFA:
    return Regex(var_name.upper()).to_epsilon_nfa()


def intersect(nfa1: EpsilonNFA, nfa2: EpsilonNFA) -> EpsilonNFA:
    intersected_nfa = nfa1.get_intersection(nfa2)
    return intersected_nfa.minimize()


def concatenate(nfa1: EpsilonNFA, nfa2: EpsilonNFA) -> EpsilonNFA:
    concatenated_nfa = nfa1.concatenate(nfa2)
    return concatenated_nfa.minimize()


def union(nfa1: EpsilonNFA, nfa2: EpsilonNFA) -> EpsilonNFA:
    union_nfa = nfa1.union(nfa2)
    return union_nfa.minimize()


def repeat(nfa: EpsilonNFA, times: int) -> EpsilonNFA:
    if times == 0:
        # creates empty nfa
        return Regex("$").to_epsilon_nfa()
    return reduce(concatenate, [nfa] * times).minimize()


def group(nfa: EpsilonNFA) -> EpsilonNFA:
    return Regex(f"({nfa.minimize().to_regex()})").to_epsilon_nfa()


def kleene(nfa: EpsilonNFA) -> EpsilonNFA:
    return nfa.kleene_star().minimize()


def repeat_range(
    nfa: EpsilonNFA, left_border: int, right_border: Optional[int]
) -> EpsilonNFA:
    if left_border == 0 and right_border is None:
        return kleene(nfa)

    if right_border is None:
        base = repeat(nfa, left_border)
        return concatenate(base, kleene(nfa))

    result_nfa = repeat(nfa, left_border)
    for i in range(left_border + 1, right_border + 1):
        result_nfa = union(result_nfa, repeat(nfa, i))
    return result_nfa.minimize()


def build_rsm(nfa: EpsilonNFA, subs_dict: dict[str, EpsilonNFA]) -> RecursiveAutomaton:
    boxes = [
        Box(var_nfa, Symbol(var_name.upper()))
        for var_name, var_nfa in subs_dict.items()
    ]
    boxes.append(Box(nfa, Symbol("START")))

    return RecursiveAutomaton(initial_label=Symbol("START"), boxes=boxes)