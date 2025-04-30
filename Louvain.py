# #Louvain算法 
# import networkx as nx
# import community


# def louvain_algorithm_with_intermediate_results(G):
#     # 初始化划分
#     partition = {n: n for n in G.nodes()}
#     old_modularity = 0
#     iteration = 0

#     while True:
#         # 保存上一轮划分结果
#         prev_partition = partition.copy()

#         # 局部移动优化阶段
#         for node in G.nodes():
#             neighbors = list(G.neighbors(node))
#             best_gain = 0
#             best_community = partition[node]
#             for neighbor in neighbors:
#                 neighbor_community = partition[neighbor]
#                 if neighbor_community != partition[node]:
#                     # 临时将节点移动到邻居所在社区
#                     partition[node] = neighbor_community
#                     new_modularity = community.modularity(partition, G)
#                     gain = new_modularity - old_modularity
#                     if gain > best_gain:
#                         best_gain = gain
#                         best_community = neighbor_community
#                     # 恢复节点原来的社区
#                     partition[node] = prev_partition[node]
#             partition[node] = best_community

#         # 计算当前模块度
#         new_modularity = community.modularity(partition, G)
#         print(f"Iteration {iteration}: Modularity = {new_modularity}")

#         # 判断是否收敛
#         if new_modularity - old_modularity < 1e-9:
#             break

#         old_modularity = new_modularity
#         iteration += 1

#         # 合并阶段
#         new_G = nx.Graph()
#         community_to_nodes = {}
#         for node, com in partition.items():
#             if com not in community_to_nodes:
#                 community_to_nodes[com] = []
#             community_to_nodes[com].append(node)

#         for com, nodes in community_to_nodes.items():
#             new_G.add_node(com)
#             subgraph = G.subgraph(nodes)
#             total_weight = sum([d['weight'] for _, _, d in subgraph.edges(data=True)])
#             new_G.nodes[com]['weight'] = total_weight

#         for com1, nodes1 in community_to_nodes.items():
#             for com2, nodes2 in community_to_nodes.items():
#                 if com1 != com2:
#                     weight = sum([G[u][v]['weight'] for u in nodes1 for v in nodes2 if G.has_edge(u, v)])
#                     if weight > 0:
#                         new_G.add_edge(com1, com2, weight=weight)

#         # 更新图和划分
#         G = new_G
#         new_partition = {}
#         for node in G.nodes():
#             for com, nodes in community_to_nodes.items():
#                 if node in nodes:
#                     new_partition[node] = com
#                     break
#         partition = new_partition

#     return partition


# # 创建无向图
# G = nx.Graph()
# edges = [('B', 'A', 5), ('A', 'E', 2), ('B', 'C', 1), ('A', 'C', 3), ('C', 'D', 7), ('D', 'F', 3), ('E', 'F', 9)]
# G.add_weighted_edges_from(edges)

# # 运行Louvain算法并输出中间结果
# final_partition = louvain_algorithm_with_intermediate_results(G)
# print("Final Community Partition:", final_partition)


import matplotlib.pyplot as plt
import networkx as nx
from community import community_louvain #这个包不叫community，而是python-louvain
import pandas as pd

G = nx.Graph()
edges = [('B', 'A', 5), ('A', 'E', 2), ('B', 'C', 1), ('A', 'C', 3), ('C', 'D', 7), ('D', 'F', 3), ('E', 'F', 9)]
G.add_weighted_edges_from(edges)
print(G)

com = community_louvain.best_partition(G)

#节点大小设置，与度关联
node_size = [G.degree(i)**1*20 for i in G.nodes()]


#格式整理
df_com = pd.DataFrame({'Group_id':com.values(),
                       'object_id':com.keys()}
                    )
# 统计每个社群人数 并降序
df_com.groupby('Group_id').count().sort_values(by='object_id', ascending=False) 


# 颜色设置
colors = ['DeepPink','orange','DarkCyan','#A0CBE2','#3CB371','b','orange','y','c','#838B8B','purple','olive','#A0CBE2','#4EEE94']*500
colors = [colors[i] for i in com.values()]



#使用 kamada_kawai_layout spring_layout 布局
plt.figure(figsize=(4,3),dpi=500)
nx.draw_networkx(G,

                 pos = nx.spring_layout(G),
                 node_color = colors,
                 edge_color = '#2E8B57',
                 font_color = 'black',
                 node_size = node_size,
                 font_size = 5,
                 alpha = 0.9,
                 width = 0.1,
                 font_weight=0.9
                 )
plt.axis('off')  
plt.show()