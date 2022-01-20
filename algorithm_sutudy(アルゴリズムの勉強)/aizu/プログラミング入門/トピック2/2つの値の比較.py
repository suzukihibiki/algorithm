
















def comparison(a_,b_):
    if a_ < b_:
        return str("a_ < b_")
    if a_ > b_:
        return str("a_ > b_")
    if a_ == b_:
        return str("a_ == b_")
    
a,b = str(input()).split()
a = int(a)
b = int(b)
ancer = comparison(
    a_=a,
    b_=b
)