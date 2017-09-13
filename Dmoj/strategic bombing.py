from copy import deepcopy
def find_path(graph, start_node, end_node, path=[]):
    path.append(start_node)
    if start_node == end_node:
        return path

    for n in graph[start_node]:
        if n not in path:
            e = find_path(graph, n, end_node, path)
            if e:
                return e
            if n in path:
                path.remove(n)
    if (start_node in path):
        path.remove(start_node)
    return None


def remove_edge(graph, start_node, end_node):
    try:
        graph[start_node].remove(end_node)
        graph[end_node].remove(start_node)
    except:
        print "unable to remove"

    return graph


def add_edge(graph, start_node, end_node):
    if start_node not in graph:
        graph[start_node] = []
    if end_node not in graph:
        graph[end_node] = []
    graph[start_node].append(end_node)
    graph[end_node].append(start_node)
    return graph




inp = ""
graph = {}
edges = []
d = []
while inp != "**":
    inp = raw_input()
    if inp != "**":
        graph = add_edge(graph, (inp[0]), (inp[1]))
        edges.append(inp)
edges = edges[::-1]

for e in edges:
    g2 = deepcopy(graph)
    g2 = remove_edge(g2, e[0], e[1])
    if not (find_path(g2, "A", "B", [])):
        d.append(e)
    g2 = add_edge(g2, e[0], e[1])
    g2 = deepcopy(graph)

for i in d:
    print i
print "There are "+str(len(d))+" disconnecting roads."
