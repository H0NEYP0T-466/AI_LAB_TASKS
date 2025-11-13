import heapq 

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 1, 'E': 5},
    'C': {'E': 2},
    'D': {'F': 4},
    'E': {'F': 1},
    'F': {}
}

def uniform_cost_search(graph, start, goal):
   
    queue = [(0, [start])]
    visited = set()

    while queue:
        cost, path = heapq.heappop(queue)
        node = path[-1]

        
        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)

            for neighbor, edge_cost in graph[node].items():
                new_cost = cost + edge_cost
                new_path = path + [neighbor]
                heapq.heappush(queue, (new_cost, new_path))

    return None, float('inf')



start_node = 'A'
goal_node = 'F'
path, total_cost = uniform_cost_search(graph, start_node, goal_node)

print("Path found by UCS:", path)
print("Total cost:", total_cost)