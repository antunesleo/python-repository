PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
INSERT INTO heat_map VALUES(1,'some/path','An awesome map!');
INSERT INTO heat_map VALUES(2,'some/path','Another awesome map!');
INSERT INTO heat_map VALUES(3,'some/path','One more awesome map!');
INSERT INTO car VALUES(1,'red');
INSERT INTO wheel VALUES(1,1,'new');
INSERT INTO wheel VALUES(2,1,'new');
INSERT INTO wheel VALUES(3,1,'old');
INSERT INTO wheel VALUES(4,1,'old');
COMMIT;