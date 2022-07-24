import networkx as nx
import numpy as np

# ランダムにグラフを生成する
airport_code = ["HND", "NRT", "CTS", "ITM", "KIX", "FUK", "OKA"]

travelers = [
    [0, 0, 420059, 310884, 64422, 473142, 336687], 
    [0, 0, 114039, 1116, 62662, 113658, 63456], 
    [420059, 114039, 0, 66113, 85515, 42474, 9115], 
    [310884, 1116, 66113, 0, 0, 44969, 71348], 
    [64422, 62662, 85515, 0, 0, 31471, 74875], 
    [473142, 113658, 42474, 44969, 31471, 0, 122941], 
    [336687, 63456, 9115, 71348, 74875, 122941, 0]
]

G = nx.DiGraph()
G.add_nodes_from(airport_code)
for O in range(len(travelers)):
    for D in range(len(travelers[O])):
        if travelers[O][D] != 0:
            G.add_edge(airport_code[O], airport_code[D], weight=travelers[O][D])


print(nx.pagerank(G))