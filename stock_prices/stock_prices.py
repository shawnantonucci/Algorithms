#!/usr/bin/python

import argparse

test1 = [100, 90, 80, 50, 20, 10]

def find_max_profit(prices):
  prices.reverse()
  max_profit = prices[0] - prices[1]

  for i in range(0, len(prices)):
    for j in range(i + 1, len(prices)):
      if len(prices) > j + 1:
        temp = prices[i] - prices[j]
        print(temp)
        if temp > max_profit:
          max_profit = temp

  return max_profit

print(find_max_profit(test1))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
