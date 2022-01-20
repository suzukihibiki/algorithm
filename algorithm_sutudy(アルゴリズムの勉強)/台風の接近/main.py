




import numpy as np


def contrast(values_,limit_) -> bool:
    for value in values_:
        if value >= limit_:
            return False
        
    return True


value_list = "3 50\n40 40 40\n40 40 40\n40 40 40"




value_list = str(value_list).split("\n")


n, m = (value_list[0]).split()
n = int(n)
m = int(m)
load_list = value_list[1:]

# [
#     '1 3 43 234 324', 
#     '24 342342 42342 34 24234'
# ]


int_values = []
add_value = int_values.append
for i in load_list:
    _list = []
    _add_list=_list.append    
    i = i.split()
    for ii in i:
        _add_list(int(ii))
    add_value(_list)
# hack :

loads = np.array(int_values).T.tolist()
# [[100, 24], [300, 342342], [430, 42342], [234, 34], [324, 24234]]

ancers = []
add_ancers = ancers.append
for _id, i in enumerate(loads):
    _ancer = contrast(
        values_=i,
        limit_=m
    )
    if _ancer == True:
        add_ancers(_id+1)


if len(ancers) == 0:
    print("wait")
else:
    print(ancers)