import bisect

class SnapshotArray:
    
    # naive하게 풀면 풀리는 문제인데, 공간 효율성 limit 때문에 다른 방법 찾아야 했음..
    # 변경된 인자들만 저장하면 되겠다! 까지는 생각해서 풀었는데,
    # 만약 변경 시점에 snap이 없었을 때 그냥 for문 돌려서 했더니 time out 에러 남..
    # bisect 라이브러리 사용해서 binary search를 하면 풀림...ㅎ
    
    array_history = []
    snap_id = 0

    def __init__(self, length: int):
        self.array_history = [[[0,0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.array_history[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        snap_idx = bisect.bisect_right(self.array_history[index], [snap_id, 10 ** 9+1])
        return self.array_history[index][snap_idx-1][1]
        

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)