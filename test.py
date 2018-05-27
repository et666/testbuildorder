import networkx as nx

def biggest_order_of_pred(preds, build_stage_new, list_of_components):
    help_list = []
    for pred_comp in preds:
        index = list_of_components.index(pred_comp)
        help_list.append(build_stage_new[index])
    return max(help_list)

def build_order(graph, starter_component):
    list_of_components = list(graph)

    build_stage_old = [-1] * len(list_of_components)
    build_stage_new = list(build_stage_old)
    build_stage_new[list_of_components.index(starter_component)] = 0

    while build_stage_old != build_stage_new:
        build_stage_old = list(build_stage_new)
        for comp in list_of_components:
            
            for testcomp in list_of_components:
                if testcomp is starter_component:
                    continue
                if comp is testcomp:
                    continue
                    
                iter = G.predecessors(testcomp)
                preds = list(iter)
                
                if comp in preds:
                    biggest_pred = biggest_order_of_pred(preds, build_stage_new, list_of_components)
                    if biggest_pred >= 0:
                        build_stage_new[list_of_components.index(testcomp)] = biggest_pred + 1
    
    for build_stage in range(0, max(build_stage_new)+1):
        print 'Build Stage:' + str(build_stage)
        indices = [i for i, x in enumerate(build_stage_new) if x == build_stage]
        for index in indices:
            print list_of_components[index]
          

if __name__=='__main__':
    G = nx.DiGraph()
    G.add_path(['A','B','C','D'])
    G.add_path(['A','C','D'])
    G.add_path(['A','E','D'])
    build_order(G, 'A')


