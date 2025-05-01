CREATE DATABASE IF NOT EXISTS library_management;
USE library_management;

CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    available BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS issued_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    member_id INT,
    issue_date DATE,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (member_id) REFERENCES members(id)
);

CREATE TABLE IF NOT EXISTS fine_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT,
    book_id INT,
    fine_amount DECIMAL(10,2),
    return_date DATE,
    FOREIGN KEY (member_id) REFERENCES members(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);
ALTER TABLE issued_books AUTO_INCREMENT = 1;
ALTER TABLE books AUTO_INCREMENT = 1;

INSERT INTO books (title, author, available) VALUES
('Harry Potter and the Sorcerer\'s Stone', 'J.K. Rowling', TRUE),
('To Kill a Mockingbird', 'Harper Lee', TRUE),
('1984', 'George Orwell', TRUE),
('The Great Gatsby', 'F. Scott Fitzgerald', TRUE),
('Pride and Prejudice', 'Jane Austen', TRUE),
('The Hobbit', 'J.R.R. Tolkien', TRUE),
('The Catcher in the Rye', 'J.D. Salinger', TRUE),
('The Lord of the Rings', 'J.R.R. Tolkien', TRUE),
('The Alchemist', 'Paulo Coelho', TRUE),
('The Chronicles of Narnia', 'C.S. Lewis', TRUE);

SELECT * FROM issued_books;
SELECT * FROM members;

