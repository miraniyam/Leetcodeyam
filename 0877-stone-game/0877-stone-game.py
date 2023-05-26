class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alice = 0
        bob = 0
        
        turn = 0
        
        while(turn <= len(piles)):
            if turn == 0 or turn % 2 == 1:
                # alice's turn
                alice += max(piles)
            else:
                bob += max(piles)
            piles[piles.index(max(piles))] = -1
            turn += 1
        
        return True if alice > bob else False