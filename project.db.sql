BEGIN TRANSACTION;
DROP TABLE IF EXISTS "currencies";
CREATE TABLE "currencies" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL DEFAULT 'EUR' CHECK("name" IN ('EUR', 'GBP', 'RUB', 'USD', 'DDM', 'FRF', 'ITL', 'HUF')),
	"defAmount"	INTEGER NOT NULL DEFAULT 1,
	"lastDate"	date NOT NULL DEFAULT '2024.10.21',
	"closed"	boolean NOT NULL DEFAULT 'false',
	"timeStamp"	TEXT NOT NULL DEFAULT 'current_timestamp()',
	PRIMARY KEY("id" AUTOINCREMENT),
	CONSTRAINT "currencies" FOREIGN KEY("id") REFERENCES "exchanges"("currId") ON UPDATE CASCADE
);
DROP TABLE IF EXISTS "exchanges";
CREATE TABLE "exchanges" (
	"id"	INTEGER NOT NULL UNIQUE,
	"userId"	INTEGER NOT NULL UNIQUE,
	"currId"	INTEGER NOT NULL UNIQUE,
	"exDate"	date,
	"value"	INTEGER NOT NULL DEFAULT 1,
	"timeStamp"	TEXT NOT NULL DEFAULT 'current_timestamp()',
	UNIQUE("currId"),
	PRIMARY KEY("id" AUTOINCREMENT),
	UNIQUE("userId")
);
DROP TABLE IF EXISTS "users";
CREATE TABLE "users" (
	"id"	INTEGER NOT NULL UNIQUE,
	"nationality"	TEXT NOT NULL DEFAULT 'Hungarian' CHECK("nationality" IN ('Hungarian', 'British', 'German', 'Russian', 'French', 'Italian', 'Other')),
	"firstName"	TEXT NOT NULL,
	"lastName"	TEXT NOT NULL,
	"taxNumber"	INTEGER NOT NULL UNIQUE,
	"address"	TEXT,
	"aemail"	TEXT,
	"phone"	INTEGER UNIQUE,
	"regDate"	TEXT NOT NULL DEFAULT 'current_timestamp()',
	"deleted"	boolean NOT NULL DEFAULT 'false',
	PRIMARY KEY("id" AUTOINCREMENT),
	CONSTRAINT "users" FOREIGN KEY("id") REFERENCES "exchanges"("userId") ON UPDATE CASCADE
);
INSERT INTO "currencies" VALUES (0,'EUR',1,'2024-10-21',0,'2024-11-06 10:56:36');
INSERT INTO "currencies" VALUES (1,'GBP',1,'2024-10-21',0,'2024-11-06 10:56:36');
INSERT INTO "currencies" VALUES (2,'RUB',1,'2024-10-21',0,'2024-11-06 10:56:36');
INSERT INTO "currencies" VALUES (3,'USD',1,'2024-10-21',0,'2024-11-06 10:56:36');
INSERT INTO "currencies" VALUES (4,'DDM',100,'1967-11-20',1,'2024-11-06 10:56:36');
INSERT INTO "currencies" VALUES (5,'FRF',1,'2002-03-29',1,'2024-11-06 10:56:36');
INSERT INTO "currencies" VALUES (6,'ITL',127,'2002-03-29',1,'2024-11-06 10:56:36');
INSERT INTO "currencies" VALUES (7,'HUF',1,'2024-10-21',0,'2024-11-29 12:45:58');
COMMIT;
