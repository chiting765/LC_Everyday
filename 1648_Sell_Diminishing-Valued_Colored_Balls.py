class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True)
        inventory.append(0) 
        i, gap, sold, amount = 0, 0, 0, 0
        while orders > 0:
            gap += 1
            sold = min(orders, gap * (inventory[i] - inventory[i+1]))
            whole, remainder = divmod(sold, gap)
            amount += gap * ((inventory[i] + inventory[i] - whole + 1) * whole // 2) + remainder * (inventory[i] - whole)
            orders -= sold
            i += 1
        return amount % (10 ** 9 + 7)
