/* TASK 4:  SQL Database Schema Design an appropriate database schema to store investment fund data. Create SQL statements to create
the necessary tables and relationships. */
-- Since I'm using Django, the sql script doesn't have to be executed.
REATE TABLE Fund (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    manager_name VARCHAR(255) NOT NULL,
    description TEXT DEFAULT '',
    nav DECIMAL(20, 2) NOT NULL,
    performance DECIMAL(6, 2) NOT NULL,
    created_at DATE NOT NULL DEFAULT CURRENT_DATE
);