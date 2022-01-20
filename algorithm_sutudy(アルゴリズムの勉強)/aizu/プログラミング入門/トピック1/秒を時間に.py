




s = int(input())
def make_time(s_):
    h = int(s_/3600)
    m = int((s_%3600)/60)
    s = int((s_%3600)%60)
    return str(f"{h}:{m}:{s}")

time_str = make_time(s_=s)
print(time_str)

