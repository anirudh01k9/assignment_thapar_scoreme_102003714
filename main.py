def longest_path(graph: list) -> int:
    def topological_sort(graph):
        in_degree = [0] * len(graph)
        for node in graph:
            for neighbor, weight in node:
                in_degree[neighbor] += 1
        
        stack = [i for i in range(len(graph)) if in_degree[i] == 0]
        topo_order = []

        while stack:
            node = stack.pop()
            topo_order.append(node)
            for neighbor, weight in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    stack.append(neighbor)

        return topo_order

    def calculate_longest_path(graph, topo_order):
        dist = [-float('inf')] * len(graph)
        
        for node in topo_order:
            if dist[node] == -float('inf'):
                dist[node] = 0

        for node in topo_order:
            for neighbor, weight in graph[node]:
                if dist[neighbor] < dist[node] + weight:
                    dist[neighbor] = dist[node] + weight

        return max(dist)
    
    topo_order = topological_sort(graph)
    return calculate_longest_path(graph, topo_order)

if __name__ == "__main__":
    graph = [
        [(1, 3), (2, 2)],
        [(3, 4)],
        [(3, 1)],
        []
    ]
    print("Longest Path Length:", longest_path(graph))
