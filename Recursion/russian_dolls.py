def count_dolls_normal_way(doll):
    count = 0
    while doll != []:
        count += 1
        doll = doll[1]
    return count

def count_dolls_recursively(doll):
    if doll == []:
        return 0
    else:
        increase = count_dolls_recursively(doll[1])
        return 1 + increase

russian_dolls = ["doll1", ["doll2", ["doll3", ["doll4", []]]]]

print("Normal way: ", count_dolls_normal_way(russian_dolls))
print("Recursively: ", count_dolls_recursively(russian_dolls))