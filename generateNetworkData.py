import random as rd


max_dist = 5
filepath = "sample_networkGraphData.csv"



data = ""
count = 1
prev_nodes = [0]

# add nodes at each distance
for n in range(1, max_dist + 1):
    
    
    # for each existing node add 0 to 5 new nodes
    # store new nodes in list
    
    newNodes = [] 

    for node in prev_nodes:
        
        for _ in range(rd.randint(0,5)):
            line = f"Id_{count}, Id_{rd.choice(prev_nodes)}, {n},"
            data += line + "\n"
            newNodes.append(count)
            count += 1

    prev_nodes = newNodes



with open(filepath, "w") as sampleData:
    sampleData.writelines("Id, previous, distance,\n")
    sampleData.writelines("id_0, , 0,\n")

    sampleData.writelines(data)
