class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        n = len(pizzas)
        pizzas.sort(reverse = True)
        days = n // 4
        no_of_odd_days = math.ceil(days / 2)
        no_of_even_days = days - no_of_odd_days
        weightGain = 0
        while no_of_odd_days > 0:
            weightGain += pizzas.pop(0)
            no_of_odd_days -= 1
        
        i = 1
        while no_of_even_days > 0:
            weightGain += pizzas[i]
            no_of_even_days -= 1
            i += 2
        
        return weightGain