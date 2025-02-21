/* TASK 5: SQL Data Migration Write SQL scripts to migrate the data from the lightweight database system (used for Task 3) to the SQL 
database you designed in Task 4 */

BEGIN TRANSACTION
INSERT INTO Fund (id, name, manager_name, description, nav, performance, created_at)
VALUES
('123e4567-e89b-12d3-a456-426614174000', 'Growth Fund', 'Alice Smith', 'A fund focused on growth stocks.', 1500000.00, 8.75, '2025-02-20');

INSERT INTO Fund (id, name, manager_name, description, nav, performance, created_at)
VALUES
('223e4567-e89b-12d3-a456-426614174001', 'Income Fund', 'Bob Johnson', 'A fund focused on income-generating assets.', 2500000.00, 5.50, '2025-02-21');

INSERT INTO Fund (id, name, manager_name, description, nav, performance, created_at)
VALUES
('323e4567-e89b-12d3-a456-426614174002', 'Balanced Fund', 'Carol Brown', 'A balanced fund with a mix of stocks and bonds.', 2000000.00, 7.25, '2025-02-22');

SELECT * FROM Fund
COMMIT
-- Be sure to uncomment rollback to undo the insertions
-- ROLLBACK