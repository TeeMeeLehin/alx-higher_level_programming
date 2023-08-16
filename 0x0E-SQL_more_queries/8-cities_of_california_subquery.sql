-- listing cities records in DB
SELECT * FROM CITIES WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
