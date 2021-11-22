CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20), species
VARCHAR(20), sex CHAR(1), checkups SMALLINT UNSIGNED, birth DATE,
death DATE);

INSERT INTO pet (name,owner,species,sex,checkups,birth,death)VALUES
('Fluffy','Harold','cat','f',5,'2001-02-04',''),
('Claws','Gwen','cat','m',2,'2000-03-17',''),
('Buffy','Harold','dog','f',7,'1999-05-13',''),
('Fang','Benny','dog','m',4,'2000-08-27',''),
('Bowser','Diane','dog','m',8,'1998-08-31','2001-07-29'),
('Chirpy','Gwen','bird','f',0,'2002-09-11',''),
('Whistler','Gwen','bird','',1,'2001-12-09',''),
('Slim','Benny','snake','m',5,'2001-04-29','');

/* Q1-1 */

.print 'Q1-1' 
SELECT name, owner FROM pet WHERE sex = "f";
.print

/* Q1-2 */

.print 'Q1-2' 
SELECT name, birth FROM pet WHERE species = "dog";
.print

/* Q1-3 */

.print 'Q1-3' 
SELECT DISTINCT owner FROM pet WHERE species = "bird";
.print

/* Q1-4 */

.print 'Q1-4' 
SELECT species FROM pet WHERE sex = "f";
.print

/* Q1-5 */

.print 'Q1-5' 
SELECT name, birth FROM pet WHERE species = "cat" OR species = "bird";
.print

/* Q1-6 */

.print 'Q1-6' 
SELECT name, species FROM pet WHERE species = "cat" OR species = "bird" AND sex = "f";  
.print
------------------------------------------------------------------------------------------

/* Q2-1 */

.print 'Q2-1'
SELECT owner, name FROM pet WHERE SUBSTR(name, -2, 2) == "er" OR SUBSTR(name, -3, 3) == "all"; 
.print

/* Q2-2 */

.print 'Q2-2'
SELECT name FROM pet WHERE owner like "%e%";
.print

/* Q2-3 */

.print 'Q2-3'
SELECT name FROM pet WHERE SUBSTR(name, -2, 2) != "fy";
.print

/* Q2-4 */

.print 'Q2-4'
SELECT name FROM pet WHERE length(owner) > 4;
.print

/* Q2-5 */

.print 'Q2-5'
SELECT owner FROM pet WHERE (SUBSTR(owner, 1, 1) = "A" OR SUBSTR(owner, 1, 1) = "B" OR  SUBSTR(owner, 1, 1) = "C" OR  SUBSTR(owner, 1, 1) = "D" OR  SUBSTR(owner, 1, 1) = "E") AND (SUBSTR(owner, -1, 1) = "a" OR SUBSTR(owner, -1, 1) = "b" OR  SUBSTR(owner, -1, 1) = "c" OR  SUBSTR(owner, -1, 1) = "d" OR  SUBSTR(owner, -1, 1) = "e");
.print
------------------------------------------------------------------------------------------

/* Q3-1 */

.print 'Q3-1'
SELECT owner, AVG(checkups) FROM pet GROUP BY owner;
.print 

/* Q3-2 */

.print 'Q3-2'
SELECT species, count(species) as SpeciesCount FROM pet GROUP BY species ORDER BY count(species) ASC;
.print

/* Q3-3 */

.print 'Q3-3'
SELECT owner, species, count(species) FROM pet GROUP BY species, owner ORDER BY owner ASC;
.print

/* Q3-4 */ 

.print 'Q3-4'
 SELECT owner, count(DISTINCT species) FROM pet GROUP BY owner ORDER BY count(species) ASC;
.print

/* Q3-5 */

.print 'Q3-5'
 SELECT sex, count(sex) FROM pet WHERE sex = "m" OR sex = "f" GROUP by sex;
.print

/* Q3-6 */

.print 'Q3-6'
 SELECT owner, species, count(species) FROM pet WHERE species = "bird" GROUP by owner;
.print

/* Q3-7 */

.print 'Q3-7'
 SELECT owner, sum(checkups) FROM pet GROUP BY owner;
.print
