/*a) What is the name of the table that holds the items Northwind sells?
products

b) What is the name of the table that holds the types/categories of the items
Northwind sells?
order details 
*/

SELECT * FROM employees;
/*a) Who is the Northwind employee whose name makes it look like she’s a bird?
EmployeeID 4, Ms. Margaret Peacock 
*/

SELECT * FROM products;
#SELECT * FROM products LIMIT 0, 10
/* a) How many records does your query return? Using the toolbar options at the top of
the query pane, how can you change your query to retrieve only 10 rows? Include
the answer as a comment underneath the SELECT statement.
77
*/

SELECT * FROM categories;
/* c) What is the category id of seafood? 
8 
*/

SELECT OrderID, OrderDate, ShipName, ShipCountry 
FROM orders 
LIMIT 50;