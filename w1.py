def apply_discount_and_sort(prices: list) -> list:
    filtered_prices = [price for price in prices if price > 0]
    
    discounted_prices = [price * 0.85 for price in filtered_prices]
    
    sorted_prices = sorted(discounted_prices, reverse=True)
    
    return sorted_prices

prices = [100, 250, 75, 150, 300]
print(apply_discount_and_sort(prices)) 

prices = []
print(apply_discount_and_sort(prices)) 
prices = [150.5, 200, 99.9, 50.25]
print(apply_discount_and_sort(prices))  

prices = [0, 300, -200, 150, 50]
print(apply_discount_and_sort(prices)) 