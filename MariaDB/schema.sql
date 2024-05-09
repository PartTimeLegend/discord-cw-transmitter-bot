CREATE TABLE transmissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sender VARCHAR(255),
    frequency DECIMAL(10, 2),
    message TEXT,
    cw_message TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
