import networkx as nx
import os
import glob
import matplotlib.pyplot as plt

plt.rcParams.update({
"text.usetex": True,
"font.family": "serif",
"font.sans-serif": ["Palatino"]})

SUPPORTED_EXTENSIONS = [".peaf", ".eaf"]

def get_file_name(path):
	base = os.path.basename(path)
	base = base.replace(".","_")
	return f"./output/{base}.pdf"

def get_extension(path):
	return os.path.splitext(path)[-1]


def plot(path, show=True, save=False):
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)

	ext = get_extension(path)
	if ext not in SUPPORTED_EXTENSIONS:
		print(f"Unknown file extension format: {ext}")
		return

	peaf = ext == ".peaf"

	print(path)
	G = nx.read_edgelist(path, create_using=nx.DiGraph, data=True)

	print(G)


	pos=nx.circular_layout(G)

	if peaf:
		labels = nx.get_edge_attributes(G,'weight')
		nx.draw_networkx_edge_labels(G,pos, edge_labels=labels)

	colors = nx.get_edge_attributes(G,'color').values()

	nx.draw(G, pos, with_labels=True, edge_color=colors, node_color='whitesmoke')

	if len(ax.collections) > 0:
		ax.collections[0].set_edgecolor("#000000")
		ax.collections[0].set_linewidth(0.5)

	if save:
		plt.savefig(get_file_name(path))

	if show:
		plt.show()

	plt.close(fig)

for path in os.listdir("./input/"):
	plot("./input/" + path, show=False, save=True)

