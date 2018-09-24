def find_children(santas_list, children):
    santas_list.sort()
    children.sort()
    result=[]
    for child in children:
        if child in santas_list and child not in result:
            result.append(child)
    return result

print (find_children(["Jason", "Jackson", "Jordan", "Johnny"],["Jason", "Jordan", "Jennifer"]) )   
print(find_children(["Jason", "Jackson", "Johnson", "JJ"],["Jason", "James", "JJ"]))
print(find_children(["jASon", "JAsoN", "JaSON", "jasON"],["JasoN", "jASOn", "JAsoN", "jASon", "JASON"]))
