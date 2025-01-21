from pyformlang.cfg import CFG
from pyformlang.rsa import RecursiveAutomaton
from pyformlang.finite_automaton import NondeterministicFiniteAutomaton
from networkx import DiGraph
from typing import Set, Tuple
from scipy.sparse import csr_array

from project.task2_fa import graph_to_nfa
from project.task3 import AdjacencyMatrixFA, intersect_automata


def tensor_based_cfpq(
    rsm: RecursiveAutomaton,
    graph: DiGraph,
    start_nodes: Set[int] = None,
    final_nodes: Set[int] = None,
) -> Set[Tuple[int, int]]:
    rsm_nfa = rsm_to_nfa(rsm)
    graph_nfa = graph_to_nfa(graph, start_nodes, final_nodes)
    rsm_adj = AdjacencyMatrixFA(rsm_nfa)
    graph_adj = AdjacencyMatrixFA(graph_nfa)

    initialize_graph_adj(graph_adj, rsm, graph_adj.number_of_states)

    last_nnz, current_nnz = 0, None

    while current_nnz != last_nnz:
        intersection = intersect_automata(rsm_adj, graph_adj)
        transitive_closure = intersection.transitive_closure()

        update_adjacency_matrix(transitive_closure, intersection, rsm, graph_adj)

        last_nnz = current_nnz
        current_nnz = sum(
            graph_adj.adj_matrix[nonterminal].nnz
            for nonterminal in graph_adj.adj_matrix
        )

    return {
        (st, fn)
        for st in graph_nfa.start_states
        for fn in graph_nfa.final_states
        if graph_adj.adj_matrix[rsm.initial_label][
            graph_adj.state_index[st], graph_adj.state_index[fn]
        ]
    }


def initialize_graph_adj(graph_adj, rsm, num_states):
    for nonterminal in rsm.boxes:
        if nonterminal not in graph_adj.adj_matrix:
            graph_adj.adj_matrix[nonterminal] = csr_array(
                (num_states, num_states), dtype=bool
            )


def update_adjacency_matrix(transitive_closure, intersection, rsm, graph_adj):
    for row_id, col_id in zip(*transitive_closure.nonzero()):
        row_state = intersection.index_state[row_id]
        col_state = intersection.index_state[col_id]
        (row_symbol, row_rsm_state), row_graph_state = row_state
        (col_symbol, col_rsm_state), col_graph_state = col_state

        if is_valid_transition(
            rsm, row_symbol, col_symbol, row_rsm_state, col_rsm_state
        ):
            row_graph_id = graph_adj.state_index[row_graph_state]
            col_graph_id = graph_adj.state_index[col_graph_state]
            graph_adj.adj_matrix[row_symbol][row_graph_id, col_graph_id] = True


def is_valid_transition(rsm, row_symbol, col_symbol, row_rsm_state, col_rsm_state):
    if row_symbol != col_symbol:
        return False
    dfa = rsm.boxes[row_symbol].dfa
    return row_rsm_state in dfa.start_states and col_rsm_state in dfa.final_states


def cfg_to_rsm(cfg: CFG) -> RecursiveAutomaton:
    return ebnf_to_rsm(cfg.to_text())


def ebnf_to_rsm(ebnf: str) -> RecursiveAutomaton:
    return RecursiveAutomaton.from_text(ebnf)


def rsm_to_nfa(rsm: RecursiveAutomaton) -> AdjacencyMatrixFA:
    nfa = NondeterministicFiniteAutomaton()
    for nonterminal, box in rsm.boxes.items():
        dfa = box.dfa
        edges = dfa.to_networkx().edges(data="label")
        for u, v, label in edges:
            nfa.add_transition((nonterminal, u), label, (nonterminal, v))
    return nfa
