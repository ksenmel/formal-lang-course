from networkx import MultiDiGraph
from pyformlang.finite_automaton import Symbol
from typing import Iterable
from scipy.sparse import csr_matrix, kron, csgraph
import numpy as np

from project.task2_fa import (
    NondeterministicFiniteAutomaton,
    regex_to_dfa,
    graph_to_nfa
)


class AdjacencyMatrixFA:
    def __init__(self, fa: NondeterministicFiniteAutomaton):
        graph = fa.to_networkx()
        self.state_index = {state: idx for idx, state in enumerate(graph.nodes)}
        self.index_state = {idx: state for state, idx in self.state_index.items()}
        self.start_state_indices = set(self.state_index[st] for st in fa.start_states)
        self.final_state_indices = set(self.state_index[st] for st in fa.final_states)
        self.number_of_states = graph.number_of_nodes()

        self.adj_matrix = {}
        for sym in fa.symbols:
            self.adj_matrix[sym] = csr_matrix(
                (self.number_of_states, self.number_of_states), dtype=bool
            )

        for u, v, label in graph.edges(data="label"):
            if label:
                self.adj_matrix[label][self.state_index[u], self.state_index[v]] = True

    def accepts(self, word: Iterable[Symbol]) -> bool:
        symbols = list(word)
        configs = [(st, symbols) for st in self.start_state_indices]

        while len(configs) > 0:
            state, rest = configs.pop()
            if not rest:
                if state in self.final_state_indices:
                    return True
                continue

            for next_state in range(self.number_of_states):
                if self.adj_matrix[rest[0]][state, next_state]:
                    configs.append((next_state, rest[1:]))
        return False

    def transitive_closure(self):
        init_matrix = csr_matrix((self.number_of_states, self.number_of_states), dtype=bool)
        init_matrix.setdiag(True)

        if not self.adj_matrix:
            return init_matrix

        reach = csr_matrix(
            (self.number_of_states, self.number_of_states), dtype=bool
        )
        for matrix in self.adj_matrix.values():
            reach += matrix
        dist_matrix = csgraph.floyd_warshall(
            reach, directed=True, unweighted=True
        )
        reach_matrix = dist_matrix < np.inf

        return reach_matrix

    def is_empty(self) -> bool:
        tc = self.transitive_closure()
        for start in self.start_state_indices:
            for final in self.final_state_indices:
                if tc[start, final]:
                    return False

        return True


def intersect_automata(
    mfa1: AdjacencyMatrixFA, mfa2: AdjacencyMatrixFA
) -> AdjacencyMatrixFA:
    intersection = AdjacencyMatrixFA(NondeterministicFiniteAutomaton())

    intersection.number_of_states = mfa1.number_of_states * mfa2.number_of_states

    intersection.state_index = {}

    for st1 in mfa1.state_index:
        for st2 in mfa2.state_index:
            index = mfa1.state_index[st1] * mfa2.number_of_states + mfa2.state_index[st2]
            intersection.state_index[(st1, st2)] = index

    intersection.index_state = {idx: state for state, idx in intersection.state_index.items()}

    intersection.start_state_indices = set()

    for s1 in mfa1.start_state_indices:
        for s2 in mfa2.start_state_indices:
            index = s1 * mfa2.number_of_states + s2
            intersection.start_state_indices.add(index)

    intersection.final_state_indices = set()

    for f1 in mfa1.final_state_indices:
        for f2 in mfa2.final_state_indices:
            index = f1 * mfa2.number_of_states + f2
            intersection.final_state_indices.add(index)

    intersection.adj_matrix = {}

    for sym, adj1 in mfa1.adj_matrix.items():
        if sym not in mfa2.adj_matrix:
            continue

        adj2 = mfa2.adj_matrix[sym]
        intersection.adj_matrix[sym] = kron(adj1, adj2, format="csr")

    return intersection


def tensor_based_rpq(
    regex: str, graph: MultiDiGraph, start_nodes: set[int], final_nodes: set[int]
) -> set[tuple[int, int]]:
    all_nodes = {int(n) for n in graph.nodes}
    start_nodes = start_nodes or all_nodes
    final_nodes = final_nodes or all_nodes

    graph_mfa = AdjacencyMatrixFA(graph_to_nfa(graph, start_nodes, final_nodes))
    regex_dfa = regex_to_dfa(regex)
    regex_mfa = AdjacencyMatrixFA(regex_dfa)

    intersection_mfa = intersect_automata(graph_mfa, regex_mfa)
    tc = intersection_mfa.transitive_closure()

    result = set()
    for start in start_nodes:
        for final in final_nodes:
            for regex_start in regex_dfa.start_states:
                for regex_final in regex_dfa.final_states:
                    if tc[
                        intersection_mfa.state_index[(start, regex_start)],
                        intersection_mfa.state_index[(final, regex_final)],
                    ]:
                        result.add((start, final))

    return result
