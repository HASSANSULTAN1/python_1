

def swap(lst):
    first      = lst[0]
    lst[0]     = lst[-1]
    lst[-1]    = first
    return lst


name_list = ['Hassan', 'Daniyal', 'Ibi','Ali']

print("SWAP FIRST AND LAST")



name = input("Enter a Name to insert: ")


name_list.append(name)

print("\nList before Swapping:")
print(name_list)



swapped_list = swap(name_list)

print("\nList after Swapping:")
print(swapped_list)
