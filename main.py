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


def correct_solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

from collections import deque
def correct_solution2(prices):
    answer = []
    prices = deque(prices)
    while prices:
        compared_prices = prices.popleft()

        count = 0
        for i in prices:
            if compared_prices > i:
                count += 1
                break
            count += 1
        answer.append(count)

    return answer

prices = [5, 6, 3, 5, 2]
print(f'{solution(prices)}')
print(f'{correct_solution(prices)}')
print(f'{correct_solution2(prices)}')