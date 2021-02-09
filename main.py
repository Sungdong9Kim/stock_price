def solution(prices):

    answer = []
    i = 0
    while i < len(prices):
        no_price_down_time = 0
        j = i + 1
        while j < len(prices):
            if (i < j):
                if (no_price_down_time == 0 and prices[i]> prices[j]):
                    no_price_down_time = 1
                    break
                elif (prices[i] <= prices[j]):
                    no_price_down_time += 1
                else :
                    no_price_down_time += 1
                    break
            j += 1
        i += 1
        answer.append(no_price_down_time)
    return answer

prices = [5, 6, 3, 5, 2]
print(f'{solution(prices)}')