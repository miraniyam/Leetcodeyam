class Solution:
    def countBits(self, n: int) -> List[int]:
        
        tmp = [format(x, 'b') for x in range(0, n+1)]
        
        answer = []
        for i in tmp:
            cnt = 0
            for j in i:
                if j == '1':
                    cnt +=1
            answer.append(cnt)
        return answer

# def countBits(self, num: int) -> List[int]:
#     return [bin(i).count('1') for i in range(num+1)]

# def countBits(self, num: int) -> List[int]:
#     counter = [0]
#     for i in range(1, num+1):
#         counter.append(counter[i >> 1] + i % 2)
#     return counter
