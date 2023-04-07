import math
def solution(n, stations, w):
    ans = 0
    no = []
    if stations[0]-w > 1:
        no.append(stations[0]-w-1)
    for i in range(1, len(stations)):
        no.append((stations[i]-w) - (stations[i-1]+w)-1)
    if stations[-1] + w < n:
        no.append(n - (stations[-1]+w))

    for i in no:
        ans += math.ceil(i/(w*2+1))
    return ans