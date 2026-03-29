from functools import reduce
from itertools import product
from networkx import MultiDiGraph
from scipy.sparse import vstack
from typing import Type
import scipy.sparse as sp

from project.task2_fa import graph_to_nfa, regex_to_dfa
from project.task3 import AdjacencyMatrixFA


def ms_bfs_based_rpq(
    regex: str,
    graph: MultiDiGraph,
    start_nodes: set[int],
    final_nodes: set[int],
    sparse_format: Type[sp.spmatrix] = sp.lil_matrix,
) -> set[tuple[int, int]]:
    all_nodes = {int(n) for n in graph.nodes}
    start_nodes = start_nodes or all_nodes
    final_nodes = final_nodes or all_nodes

    dfa_adj_matrix = AdjacencyMatrixFA(regex_to_dfa(regex), sparse_format)
    nfa_adj_matrix = AdjacencyMatrixFA(
        graph_to_nfa(graph, start_nodes, final_nodes), sparse_format
    )

    nfa_st_ids = {i: state for i, state in enumerate(nfa_adj_matrix.state_index)}

    labels = dfa_adj_matrix.adj_matrix.keys() & nfa_adj_matrix.adj_matrix.keys()

    transposed = {label: dfa_adj_matrix.adj_matrix[label].T for label in labels}

    start_states = [
        (dfa_st, nfa_st)
        for dfa_st, nfa_st in product(
            dfa_adj_matrix.start_state_indices, nfa_adj_matrix.start_state_indices
        )
    ]

    k = len(dfa_adj_matrix.state_index.keys())
    m = len(nfa_adj_matrix.state_index.keys())

    def init_front():
        matrices = []
        for dfa_idx, nfa_idx in start_states:
            matrix = sparse_format((k, m), dtype=bool)
            matrix[dfa_idx, nfa_idx] = True
            matrices.append(matrix)
        return vstack(matrices, format=sparse_format([[]]).getformat(), dtype=bool)

    front = init_front()
    visited = front

    # checking nnz > 0 is more efficient for sparse matrices
    while front.nnz > 0:
        new_front = []

        for label in labels:
            sym_front = front @ nfa_adj_matrix.adj_matrix[label]

            new_front.append(
                vstack(
                    [
                        transposed[label] @ sym_front[k * i : k * (i + 1)]
                        for i in range(len(start_states))
                    ]
                )
            )

        front = reduce(lambda x, y: x + y, new_front, front) > visited
        visited += front

    res = set()

    for final_dfa in dfa_adj_matrix.final_state_indices:
        for i, start in enumerate(nfa_adj_matrix.start_state_indices):
            reached_states = visited[k * i : k * (i + 1)].getrow(final_dfa).indices

            for reached in reached_states:
                if reached in nfa_adj_matrix.final_state_indices:
                    res.add((nfa_st_ids[start], nfa_st_ids[reached]))

    return res
