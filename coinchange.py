class Solution(object):
    numlist = []
    mem = {}
    numbofcoins = 0
    def isCoinChange(self,coins1,amount1,numb):
        #print(amount1)
        if self.numbofcoins != 0 and self.numbofcoins < numb:
            return False
        if amount1 == 0:
            if self.numbofcoins ==0 or self.numbofcoins > numb:
                self.numbofcoins = numb
            return True
        if len(coins1) ==0:
            return False
        if amount1 in self.mem:
            print ("hit")
            return False
        numofcoins = int(amount1/coins1[0])

        while numofcoins>=0:

            result = self.isCoinChange(coins1[1:],amount1-numofcoins*coins1[0],numofcoins+numb)
            numofcoins = numofcoins - 1

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        if amount == 0:
            return 0
        coins = sorted(coins,reverse = True)
        self.isCoinChange(coins,amount,0)

        if self.numbofcoins == 0:
            return -1
        return self.numbofcoins



if __name__ == "__main__":
    sl = Solution()
    print(sl.coinChange([3,7,405,436],8839))
