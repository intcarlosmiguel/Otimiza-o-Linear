import networkx as nx
import matplotlib.pyplot as plt
def create_graph():
    G = nx.DiGraph()
    G.add_edge('Unidade 1','Incinerador 1',weight = 30)
    G.add_edge('Unidade 1','Incinerador 2',weight = 36)
    G.add_edge('Unidade 2','Incinerador 1',weight = 35)
    G.add_edge('Unidade 2','Incinerador 2',weight = 42)

    G.add_edge('Incinerador 1','Aterro 1',weight = 5)
    G.add_edge('Incinerador 1','Aterro 2',weight = 8)
    G.add_edge('Incinerador 2','Aterro 1',weight = 9)
    G.add_edge('Incinerador 2','Aterro 2',weight = 6)

    cores = []
    for i in G.nodes:
        if('Aterro' in i):
            cores.append('mediumseagreen')
        elif('Unidade' in i):
            cores.append('teal')
        else:
            cores.append('indianred')
        
    peso = [G.get_edge_data(i[0],i[1])['weight']/10 for i in G.edges]
    pos = {
        'Unidade 1': [0,3],
        'Unidade 2': [0,1],
        'Incinerador 1': [1,5],
        'Incinerador 2': [1,-1],
        'Aterro 1': [2,7],
        'Aterro 2': [2,-3],
        }
    plt.figure(figsize=(12,12),dpi = 300)
    nx.draw(
        G,
        with_labels = True,
        pos = pos,
        node_size=9000,
        node_color = cores,
        width = peso,
        
    )
    nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels={edge:G.get_edge_data(edge[0],edge[1])['weight'] for edge in G.edges}
    )
    plt.savefig("grafo.png")