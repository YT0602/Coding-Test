import heapq

N, K = map(int, input().split())
bag = []
gem = []
ans = 0

for _ in range(N):
    wei, price = map(int, input().split())
    heapq.heappush(gem, [wei, -price])

for _ in range(K):
    heapq.heappush(bag, int(input()))

# 보석후보
tmp_gem = []

for _ in range(K):
    bag_wei = heapq.heappop(bag)
    # 가방에 담을 수 있는 보석 후보 찾기
    while gem and gem[0][0] <= bag_wei:
        cur_wei, cur_pri = heapq.heappop(gem)
        heapq.heappush(tmp_gem, cur_pri)
    # 보석 후보가 있으면 가장 비싼 보석 선택하여 담기
    if tmp_gem:
        ans -= heapq.heappop(tmp_gem)
    elif not gem:
        break

print(ans)