SELECT *
FROM Products
WHERE description REGEXP '(^| )(?-i:SN)[0-9]{4}-[0-9]{4}( |$)'
ORDER BY product_id;
