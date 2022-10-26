CREATE TABLE IF NOT EXISTS monster_name (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    stars VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS monster_type (
    mtid INT PRIMARY KEY AUTO_INCREMENT,
    type VARCHAR(20),
    fk_nameid INT,
    FOREIGN KEY(fk_nameid) REFERENCES monster_name(id)
);
