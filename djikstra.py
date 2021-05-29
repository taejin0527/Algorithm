import sys

class Node:
    """노드 클래스"""
    def __init__(self, name):
        self.name = name
        self.distance = None
        self.predecessor = None
        self.complete = None
        self.neibor = {}

    def add_connection(self, node, weight):
        """간선형성"""
        self.neibor[node.name] = (node, weight)
        node.neibor[self.name] = (self, weight)

def pick_min_node(graph) -> Node:
    """그래프에서 디스턴스가 가장 작은 노드를 찾는 메서드"""
    temp = None
    for node in graph.values():
        if temp is None and node.complete is False:
            temp = node
            continue
        if node.complete is False and temp.distance > node.distance:
            temp = node
    return temp

def Dijkstra(graph: dict, start_node: Node):
    """최단경로 메서드"""
    for node in graph.values():
        node.distance = sys.maxsize
        node.predecessor = None
        node.complete = False
    
    comp_cnt = 0
    start_node.distance = 0
    temp = start_node

    while comp_cnt < len(graph):
        for node, weight in temp.neibor.values():
            if node.distance > temp.distance + weight:
                node.distance = temp.distance + weight
                node.predecessor = temp

        temp.complete = True
        comp_cnt += 1
        temp = pick_min_node(graph)

def backtracking(node:Node):
    res_str = ''
    temp = node
    
    while temp:
        res_str = f'{temp.name} {res_str}' 
        temp = temp.predecessor
    
    return res_str + f'\n거리 : {node.distance}'