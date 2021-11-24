# Алгоритм Дейкстры для нахождения кратчайшего пути
# Надо добраться из пункта A в пункт I
# Пусть граф выглядит так
''' 
              
    C -4- D -----12----- G 
   /       \            / \ 
  3         4          2   8
 /           \        /     \ 
A -----8----- B -27- F --5-- I
 \             \      \     / 
  \            13     10   3
   \             \      \ / 
    ----4-------- E -26- H

-> -> -> -> -> -> -> -> -> -> ->                           
'''
# Кратчайший путь A-C-D-G-I (27)

# Создание графа
graph = {}
graph['A'] = {'C': 3, 'B': 8, 'E': 4}
graph['B'] = {'F': 27, 'E': 13}
graph['C'] = {'D': 4}
graph['D'] = {'B': 4, 'G': 12}
graph['E'] = {'H': 26}
graph['F'] = {'G': 2, 'I': 5, 'H': 10}
graph['G'] = {'I': 8}
graph['H'] = {'I': 3}
graph['I'] = {}

def lowest_cost_way(graph: dict, point_start, point_finish):
    # Создание таблицы стоимостей
    costs = {key: value for key, value in graph[point_start].items()}
    infinity = float('inf')
    for key in graph.keys():
        if key not in costs.keys() and key != point_start:
            costs[key] = infinity

    # Создание таблицы родителей
    parents = {key: point_start for key in graph[point_start].keys()}
    parents[point_finish] = None

    # Хранение посещённых мест    
    processed = [] 

    while True:
        # Нахождение соседа с минимальной стоимостью
        node = None
        lowest_cost = infinity
        for curr_node in costs:
            cost = costs[curr_node]
            if cost < lowest_cost and curr_node not in processed:
                lowest_cost = cost
                node = curr_node
        if node is None:
            break
        cost = costs[node]
        neighbors = graph[node]
        for key, value in neighbors.items():
            new_cost = cost + value
            if costs[key] > new_cost:
                costs[key] = new_cost
                parents[key] = node
        processed.append(node)

    if parents[point_finish] is None:
        print('Not available')
        return None

    way, way_cost = point_finish, costs[point_finish]
    while True:
        way += parents[point_finish]
        point_finish = parents[point_finish]
        if point_finish == point_start:
            break

    return way[::-1], way_cost    
        


print( lowest_cost_way(graph, 'A', 'I') )
# Output: ('ACDGI', 27)