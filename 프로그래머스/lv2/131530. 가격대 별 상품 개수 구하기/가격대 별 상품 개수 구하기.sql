-- 코드를 입력하세요
# SET @PR = -10000;

# SELECT (@PR := @PR + 10000) AS PRICE_GROUP,
# (SELECT COUNT(*)
# FROM PRODUCT
# WHERE @PR <= PRICE AND PRICE < @PR+10000) AS PRODUCTS
# FROM PRODUCT
# WHERE @PR < PRICE
# ORDER BY PRICE_GROUP;

# set @a = 0;

# select (@a := @a + 10000) as PRICE_GROUP,
#         (select count(*)
#             from PRODUCT
#             where @a <= price and price < @a+10000) as PRODUCTS 
#     from PRODUCT
#     where @a < price  
#     order by PRICE_GROUP;

SELECT  floor(price / 10000) * 10000 as PRICE_GROUP, count(*) as PRODUCTS
    from PRODUCT
    group by floor(price / 10000) * 10000
    order by 1;