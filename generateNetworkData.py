import random as rd


max_dist = 6
filepath = "sample_networkGraphData.csv"

max_nodes_per_node = 5


data = ""
count = 1
prev_nodes = [0]

# add nodes at each distance
for n in range(1, max_dist + 1):
    
    
    # for each existing node add 0 to 5 new nodes
    # store new nodes in list

    newNodes = [] 

    for node in prev_nodes:
        newNodeCount = rd.randint(1,max_nodes_per_node) if n == 1 else rd.randint(0,max_nodes_per_node)
        
        for _ in range(newNodeCount):
            line = f"Id_{count},Id_{rd.choice(prev_nodes)},{n},\n"
            data += line
            newNodes.append(count)
            count += 1

    prev_nodes = newNodes



with open(filepath, "w") as sampleData:
    sampleData.writelines("Id,Previous,Distance,\n")
    sampleData.writelines("Id_0,Id_0,0,\n")

    sampleData.writelines(data)
