class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        rem=purchaseAmount%10
        if rem==0:
            return 100-purchaseAmount
        if rem<5:
            return 100-(purchaseAmount-rem)
        if rem>=5:
            return 100-(purchaseAmount+(10-rem))
       