import sys

def maxProfit(prices):
    profit = 0
    min_price = sys.maxsize

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices))


"""
아무리해도 시간초과로 답안을 봄..

위 for문을 통해 O(n)의 속도로 계산 가능
현재값을 매번 저점과 비교해나가면서 수행.
"""