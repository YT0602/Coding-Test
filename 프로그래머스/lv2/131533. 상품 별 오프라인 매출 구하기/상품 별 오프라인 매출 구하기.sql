-- 코드를 입력하세요
SELECT A.PRODUCT_CODE, SUM(A.PRICE * B.SALES_AMOUNT) AS SALES
FROM PRODUCT A
LEFT JOIN OFFLINE_SALE B
ON A.PRODUCT_ID = B.PRODUCT_ID
WHERE OFFLINE_SALE_ID IS NOT NULL
GROUP BY A.PRODUCT_CODE
ORDER BY SALES DESC, A.PRODUCT_CODE