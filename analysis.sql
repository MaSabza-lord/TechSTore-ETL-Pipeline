-- Calculate total value per category
SELECT 
    Category, 
    COUNT(*) as TotalItems, 
    SUM(Price) as TotalValue
FROM Products
GROUP BY Category
ORDER BY TotalValue DESC;