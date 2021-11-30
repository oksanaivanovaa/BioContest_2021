

def find_closest_barier(x,list_of_bariers, delta): #This algorithm is for modification of middle barriers
    for b in list_of_bariers:
        if x<b:
            if x+delta>b:
                return b
            else:
                return None


def read_modification(read_list_of_bariers, list_of_bariers, delta):
    new_read_lob = []

    # First we modify middle barriers
    for i in range(1, len(read_list_of_bariers)-1):
        x = read_list_of_bariers[i]
        x_new = find_closest_barier(x, list_of_bariers, delta)
        if x_new == None:
            return None
        else:
            new_read_lob.append(x_new)

    &&&???????

    return(new_read_lob)
