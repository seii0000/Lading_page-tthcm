import networkx as nx
import matplotlib.pyplot as plt

# Tạo một đối tượng đồ thị
G = nx.DiGraph()

# Thêm các nút và cạnh cho AND-OR graph
G.add_node("OR Node")
G.add_node("AND Node 1")
G.add_node("AND Node 2")
G.add_node("OR Node 3")
G.add_node("AND Node 4")

G.add_edge("OR Node", "AND Node 1")
G.add_edge("OR Node", "AND Node 2")
G.add_edge("AND Node 1", "OR Node 3")
G.add_edge("AND Node 2", "OR Node 3")
G.add_edge("OR Node 3", "AND Node 4")

# Vẽ đồ thị
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=5000, node_color="lightblue", font_size=10, font_color="black", font_weight="bold")

plt.title("AND-OR Graph")
plt.show()
