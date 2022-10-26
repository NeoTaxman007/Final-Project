CREATE TABLE IF NOT EXISTS monstertype (
    mtid INT PRIMARY KEY AUTO_INCREMENT,
    type VARCHAR(20)
    fk_nameid INT,
    FOREIGN KEY(fk_nameid) REFERENCES monstername(id)
);

CREATE TABLE IF NOT EXISTS monstername (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50)
    stars VARCHAR(20)
);