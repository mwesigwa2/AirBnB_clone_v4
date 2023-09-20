--- create A database hbnb_dev_db
--- A new user hbnb_dev (in localhost)
CREATE DATABASE IF NOT EXISTS 'hbnb_dev_db'@'localhost';
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';