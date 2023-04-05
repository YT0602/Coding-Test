-- 코드를 입력하세요
SELECT distinct CART_ID
FROM CART_PRODUCTS
WHERE NAME like '%Milk%' and cart_id IN (SELECT cart_id
                         FROM CART_PRODUCTS
                         WHERE NAME like '%Yogurt%')
ORDER BY CART_ID