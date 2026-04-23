USE northwind; 


/*1. Write a query to find the price of the cheapest item that Northwind sells. Then write a
second query to find the name of the product that has that price.*/
SELECT MIN(UnitPrice) AS CheapestItem
FROM products;

SELECT ProductName, UnitPrice
FROM products
WHERE UnitPrice = 
	(SELECT MIN(UnitPrice)
    FROM products);

/*2. Write a query to find the average price of all items that Northwind sells.
(Bonus: Once you have written a working query, try asking Claude or ChatGPT for help
using the ROUND function to round the average price to the nearest cent.)*/
SELECT ROUND(AVG(UnitPrice), 2) AS avgPrice
FROM products;

/*3. Write a query to find the price of the most expensive item that Northwind sells. Then
write a second query to find the name of the product with that price, plus the name of
the supplier for that product.*/

SELECT ROUND(MAX(UnitPrice), 2) AS mostExpItem
FROM products;

SELECT ProductName, UnitPrice
FROM products 
WHERE UnitPrice =(
	SELECT MAX(UnitPrice) 
	FROM products
    );

/*4. Write a query to find total monthly payroll (the sum of all the employees’ monthly
salaries).*/
SELECT ROUND(SUM(Salary) , 2) AS totalMonthlyPayroll
FROM employees;

/*5. Write a query to identify the highest salary and the lowest salary amounts which any
employee makes. (Just the amounts, not the specific employees!)*/
SELECT MAX(Salary) AS MaxSal, MIN(Salary) AS MinSal
FROM employees;

/*Write a query to find the name and supplier ID of each supplier and the number of
items they supply. Hint: Join is your friend here.*/
SELECT CompanyName, Suppliers.supplierID, COUNT(ProductID) AS ProductCount
FROM suppliers
JOIN products
ON suppliers.SupplierID = products.SupplierID
GROUP BY suppliers.SupplierID, CompanyName;


/*Write a query to find the list of all category names and the average price for items in
each category.*/
SELECT CategoryName, ROUND(AVG(UnitPrice), 2) AS avgPriceOfItems
FROM categories 
JOIN products
ON categories.CategoryID = products.CategoryID
GROUP BY CategoryName; 

/* Write a query to find, for all suppliers that provide at least 5 items to Northwind, what
is the name of each supplier and the number of items they supply.*/
SELECT CompanyName, COUNT(ProductID) AS ItemCount
FROM suppliers
JOIN products
ON suppliers.SupplierID = products.SupplierID
GROUP BY CompanyName
HAVING COUNT(ProductID) >= 5;

/*
9. Write a query to list products currently in inventory by the product id, product name,
and inventory value (calculated by multiplying unit price by the number of units on
hand). Sort the results in descending order by value. If two or more have the same
value, order by product name. If a product is not in stock, leave it off the list.*/
SELECT ProductID, ProductName, UnitPrice*UnitsInStock AS InventoryVal
FROM products
WHERE UnitsInStock > 0
ORDER BY ProductName ASC, InventoryVal DESC;

