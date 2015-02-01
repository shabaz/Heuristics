from DistanceMap import DistanceMap
distanceMap = DistanceMap()

import pygraphviz as pgv

number_of_cities = 4

G=pgv.AGraph(strict=True,directed=True, ranksep='1.0')
G.add_node('Amsterdam_root', label='Amsterdam', fontsize="25.0")
for i in xrange(number_of_cities):
    if i == 0:
        continue
    name = distanceMap.getCities()[i].getName()
    G.add_node(name+"_level_1", label=name, fontsize="25.0")
    G.add_edge('Amsterdam_root', name+"_level_1")
    G.add_edge(name+"_level_1", "Amsterdam_root", splines="curved", style="dashed", color='grey')
    for j in xrange(number_of_cities):
        if j == i:
            continue
        second_name = distanceMap.getCities()[j].getName()
        G.add_node(second_name+"_level_2"+name, label=second_name)
        G.add_edge(name+"_level_1", second_name+"_level_2"+name)
        if j != 0:
            G.add_edge(second_name+"_level_2"+name, "Amsterdam_root", splines="curved", style="dashed", color='grey')
        G.add_node(second_name+"_level_2"+name+"invis", label=second_name, style="invisible")
        G.add_edge(second_name+"_level_2"+name, second_name+"_level_2"+name+"invis", style="dotted", arrowhead="none")
G.layout("dot")
G.draw("bruteforce_tree.png")
