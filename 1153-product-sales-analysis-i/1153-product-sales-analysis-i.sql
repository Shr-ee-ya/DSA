# Write your MySQL query statement below
select Product.product_name, year, price
from Sales
join Product
where sales.product_id=product.product_id;