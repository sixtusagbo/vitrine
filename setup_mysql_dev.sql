-- prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS vit_db;
CREATE USER IF NOT EXISTS 'vit_dev'@'localhost';
SET PASSWORD FOR 'vit_dev'@'localhost' = 'vit_dev_pwd';
GRANT USAGE ON *.* TO 'vit_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'vit_dev'@'localhost';
GRANT ALL PRIVILEGES ON `vit_db`.* TO 'vit_dev'@'localhost';
FLUSH PRIVILEGES;
