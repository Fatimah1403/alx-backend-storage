-- Create a trigger to decrease item quantity after adding a new order
CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.quantity
WHERE name = NEW.item_name;
