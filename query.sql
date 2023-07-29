-- SQLite
-- CREATE TABLE PREFERENCE (user_id INTEGER NOT NULL PRIMARY KEY, song TEXT, album TEXT, artist TEXT);

-- INSERT INTO users (user_id, username, password, email)
-- VALUES ("1000000", "johndoe2", "johndoe2spassword", "johndoe2@gmail.com");

-- INSERT INTO preference (user_id, song, album, artist)
-- VALUES("0000000", "John's Song", "John's Album", "John Doe");

-- SELECT email FROM users WHERE username LIKE "j%e";

-- ALTER TABLE preference RENAME TO PREFERENCES;

-- UPDATE users SET email="notjoe@gmail.com" WHERE username = "joe";

SELECT * FROM users;
SELECT * FROM preferences;
-- DELETE FROM preferences WHERE user_id = 1000001;
-- SELECT DISTINCT * FROM preferences LEFT JOIN users WHERE preferences.user_id = users.user_id;

