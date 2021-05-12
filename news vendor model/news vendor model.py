

"""
報童問題之最佳訂貨量（進階版）
我們想要找出能最大化預期利潤的最佳訂貨量 q∗，以及在此訂貨量之下能得到的預期利潤 π(q∗) 無條件捨去到整數位。
如果有數個訂貨量會導致一模一樣的預期利潤，將使用比較小的那一個當最佳訂貨量。
"""

# 範例測資
# cost = 2
# price = 10
# N = 10
# remain = 1
# lst = [0.06, 0.15, 0.22, 0.22, 0.17, 0.1, 0.05, 0.02, 0.01, 0.0, 0.0]

# input
cost = int(input('Cost:'))  # 單位進貨成本
price = int(input('Price:'))  # 單位零售價格
N = int(input('N:'))  # 需求可能數
remain = int(input('Remain:'))  # 殘餘值

lst = []  # 用list儲存需求機率
max_exp_profit = 0  # 最佳期望利潤
optimal_buy = 0  # 最佳訂購量
ttl_exp_profit = 0  # 期望利潤總和
last_prob = 1  # 用來計算購買量的最後一個機率，e.g.(1-prob1-prob2-...)

# 輸入需求機率並儲存於lst
for i in range(N+1):
    prob = float(input('Prob{}:'.format(i+5)))
    lst.append(prob)

# 計算每個訂購量的期望利潤，並找出最佳訂購量
for quantity in range(N+1):
    for demand in range(quantity+1):
        if demand < quantity:
            exp_profit = (demand * price - quantity * cost + remain * (quantity-demand)) * lst[demand]
            ttl_exp_profit += exp_profit
            last_prob -= lst[demand]
        else:
            exp_profit = (demand * price - quantity * cost) * last_prob
            ttl_exp_profit += exp_profit
            # print(int(ttl_exp_profit))  # 可印出每個訂購量的期望利潤
    if ttl_exp_profit > max_exp_profit:
        max_exp_profit = ttl_exp_profit  # 找最佳期望利潤
        optimal_buy = quantity # 找最佳訂購量

    # 將ttl_exp_profit和last_prob回到預設值
    ttl_exp_profit = 0
    last_prob = 1

# output
print(optimal_buy, int(max_exp_profit))
