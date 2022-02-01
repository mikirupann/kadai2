--IF EXISTS(存在していたら消します)
DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users (
   name TEXT NOT NULL,
   age INTEGER
);

