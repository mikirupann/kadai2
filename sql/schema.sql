--IF EXISTS(存在していたら消します)
DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users (
   name TEXT CHECK(0 <= LENGTH(name) and LENGTH(name) <= 20),
   age INTEGER CHECK(0 <= age and age <= 120),
   PRIMARY KEY(name)
);

