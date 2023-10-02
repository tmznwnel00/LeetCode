class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice, bob = 0, 0
        temp = ''
        for color in colors:
            if temp == '':
                temp += color
            elif color == 'A':
                if temp[0] == 'A':
                    temp += 'A'
                else:
                    length = len(temp)
                    bob += max(length-2, 0)
                    temp = 'A'
            else:
                if temp[0] == 'B':
                    temp += 'B'
                else:
                    length = len(temp)
                    alice += max(length-2, 0)
                    temp = 'B'
        length = len(temp)
        if temp != '' and temp[0] == 'A':
            alice += max(length-2, 0)
        elif temp != '' and temp[0] == 'B':
            bob += max(length-2, 0)
        
        return True if alice > bob else False