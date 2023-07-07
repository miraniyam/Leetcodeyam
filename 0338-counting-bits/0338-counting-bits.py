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