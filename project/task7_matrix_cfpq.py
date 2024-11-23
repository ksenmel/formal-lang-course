import networkx as nx
from pyformlang.cfg import CFG
from scipy.sparse import csr_matrix

from project.task6_cfpq import cfg_to_weak_normal_form


def matrix_based_cfpq(
    cfg: CFG,
    graph: nx.DiGraph,
    start_nodes: set[int] = None,
    final_nodes: set[int] = None,
) -> set[tuple[int, int]]:
    cfg = cfg_to_weak_normal_form(cfg)
    nullable = cfg.get_nullable_symbols()

    graph_nodes = graph.nodes
    node_to_idx_mapping = {node: i for i, node in enumerate(graph_nodes)}
    idx_to_node_mapping = {i: node for i, node in enumerate(graph_nodes)}

    decomposition = {}
    n = len(graph_nodes)
    for variable in cfg.variables:
        decomposition[variable] = csr_matrix((n, n), dtype=bool)

    for u, v, label in graph.edges.data("label"):
        for prod in cfg.productions:
            if len(prod.body) == 1 and (prod.body[0].value == label):
                decomposition[prod.head][node_to_idx_mapping[u], node_to_idx_mapping[v]] = True

    for var in nullable:
        decomposition[var].setdiag(True)

    added = True
    while added:
        added = False

        for prod in cfg.productions:
            if len(prod.body) == 2:
                head, A, B = prod.head, prod.body[0], prod.body[1]
                head_matrix = decomposition[head] + (decomposition[A] @ decomposition[B])
                if (decomposition[head] != head_matrix).nnz:
                    added = True
                    decomposition[head] = head_matrix

    result_pairs = set()
    rows, cols = decomposition[cfg.start_symbol].nonzero()
    for u, v in zip(rows, cols):
        if idx_to_node_mapping[u] in start_nodes:
            if idx_to_node_mapping[v] in final_nodes:
                result_pairs.add((idx_to_node_mapping[u], idx_to_node_mapping[v]))

    return result_pairs
