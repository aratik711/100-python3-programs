"""

Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

output
[1, 2, 3, 4, 5, 6, 7, 8, 9]

"""

flat_list = []

def get_flat_list(l):
        if isinstance(l, list):
            for element in l:
                get_flat_list(element)
        else:
            flat_list.append(l)

list_of_lists =[[[1, 2, 3]],[[4, 5, 6]],[[7, 8, 9]]]
get_flat_list(list_of_lists)
print (flat_list)
