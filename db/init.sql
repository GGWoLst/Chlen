CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tracking_number VARCHAR(100),
    customer_name VARCHAR(100),
    address VARCHAR(255),
    status ENUM('Создан', 'В пути', 'Доставлен') DEFAULT 'Создан'
);
