-- prepares a MySQL server for running tests on the project
CREATE DATABASE IF NOT EXISTS vit_test_db;
CREATE USER IF NOT EXISTS 'vit_test'@'localhost';
SET PASSWORD FOR 'vit_test'@'localhost' = 'vit_test_pwd';
GRANT USAGE ON *.* TO 'vit_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'vit_test'@'localhost';
GRANT ALL PRIVILEGES ON `vit_test_db`.* TO 'vit_test'@'localhost';
FLUSH PRIVILEGES;
