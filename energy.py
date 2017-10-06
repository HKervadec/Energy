#!/usr/bin/env python3

import numpy as np
import scipy as sp
import scipy.sparse
import maxflow


class Energy(object):
    def __init__(self, nodes, connections):
        """
        nodes: expected number of nodes in the graph
        connections: expected number of edges in the graph
        """
        self._g = maxflow.Graph[float](nodes, connections)
        self._N = nodes
        self._g.add_nodes(self._N)

        self._was_minimized = False
        self._prev_u = np.zeros((self._N, 2))

    def set_neighbors(self, adj_matrix):
        """
        adj_matrix: (N, N) Adjacency matrix in a SciPy sparse format.
            Which one does not matter as it will be converted to coo format.
        """
        adj_m = sp.sparse.triu(adj_matrix.tocoo())

        for i, j, w in zip(adj_m.row, adj_m.col, adj_m.data):
            self._g.add_edge(i, j, w, w)

    def set_unary(self, unaries):
        """
        unaries: (N, 2) array containing the unary weights.
        """
        if not self._was_minimized:
            for i, u in enumerate(unaries):
                self._g.add_tedge(i, u[1], u[0])
        else:
            diff = unaries - self._prev_u
            for i, u in enumerate(diff):
                self._g.add_tedge(i, u[1], u[0])

        self._prev_u[:] = unaries

    def minimize(self):
        e = self._g.maxflow()
        self._was_minimized = True

        return e

    def get_labeling(self):
        labels = self._g.get_grid_segments(np.arange(self._N))

        return labels
