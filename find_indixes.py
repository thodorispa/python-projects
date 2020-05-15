def index_all(target_list,indice):
    index_list = list()
    for i in target_list:
        if indice == i:
            index_list.append(target_list.index(i))
    return index_list

disco = [2,2,1,56,6,1,22,4,[1,2]]
print(index_all(disco, 1))
        