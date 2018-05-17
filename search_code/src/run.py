# Search methods

import search


"""ab = search.GPSProblem('A', 'B', search.romania)


print "Busqueda en anchura --->", search.breadth_first_graph_search(ab).path()
print "Busqueda en profundidad --->", search.depth_first_graph_search(ab).path()
print "Ramificacion y acotacion --->", search.ramAndCot_first_graph_search(ab).path()
print "Ramificacion y acotacion con subestimacion --->", search.ramAndCotHeur_first_graph_search(ab).path()"""
#print search.iterative_deepening_search(ab).path()
#print search.depth_limited_search(ab).path()

#print search.astar_search(ab).path()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

"""th = search.GPSProblem('T', 'H', search.romania)
print "--------------------------------------------------------------------------------"

print "Busqueda en anchura --->", search.breadth_first_graph_search(th).path()
print "Busqueda en profundidad --->", search.depth_first_graph_search(th).path()
print "Ramificacion y acotacion --->", search.ramAndCot_first_graph_search(th).path()
print "Ramificacion y acotacion con subestimacion --->", search.ramAndCotHeur_first_graph_search(th).path()"""


og = search.GPSProblem('O', 'G', search.romania)
#print "--------------------------------------------------------------------------------"

print "Busqueda en anchura --->", search.breadth_first_graph_search(og).path()
print "Busqueda en profundidad --->", search.depth_first_graph_search(og).path()
print "Ramificacion y acotacion --->", search.ramAndCot_first_graph_search(og).path()
print "Ramificacion y acotacion con subestimacion --->", search.ramAndCotHeur_first_graph_search(og).path()


expandedNodes = search.getExpandedNodes(og)

print "\n", "El numero de nodos expandidos por ramificacion y acotacion es:", expandedNodes[0]
print "El numero de nodos expandidos por ramificacion y acotacion con subestimacion es:", expandedNodes[1]

