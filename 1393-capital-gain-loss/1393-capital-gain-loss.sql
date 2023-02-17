# Write your MySQL query statement below

SELECT A.stock_name, (A.sell_sum - B.buy_sum) as capital_gain_loss
from (
    select stock_name, sum(price) as sell_sum
    from Stocks
    where operation = 'Sell'
    group by stock_name
) A
inner join (
    select stock_name, sum(price) as buy_sum
    from Stocks
    where operation = 'Buy'
    group by stock_name
) B on (A.stock_name = B.stock_name)