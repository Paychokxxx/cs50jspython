SELECT * FROM users WHERE (username = username) and (password = password);

SELECT * FROM users WHERE (username = 'alice') and (password = '12345');

SELECT * FROM users WHERE (username = 'hacker') and (password = '1' OR '1' = '1');