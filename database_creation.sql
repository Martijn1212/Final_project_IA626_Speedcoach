CREATE TABLE club
(
  partner_id VARCHAR(10) NOT NULL,
  name VARCHAR(25) NOT NULL,
  PRIMARY KEY (partner_id)
);

CREATE TABLE users
(
  user_id VARCHAR(10) NOT NULL,
  name VARCHAR(25) NOT NULL,
  weight_class CHAR(1) NOT NULL,
  age INT NOT NULL,
  partner_id VARCHAR(10) NOT NULL,
  PRIMARY KEY (user_id),
  FOREIGN KEY (partner_id) REFERENCES club(partner_id)
);

CREATE TABLE workouts
(
  timezone VARCHAR(3) NOT NULL,
  date VARCHAR(40) NOT NULL,
  id VARCHAR(10) NOT NULL,
  comments VARCHAR(200) NOT NULL,
  calories_total VARCHAR(20) NOT NULL,
  type VARCHAR(20) NOT NULL,
  distance NUMERIC(10.1) NOT NULL,
  stroke_rate VARCHAR(5.1) NOT NULL,
  workout_type VARCHAR(25) NOT NULL,
  time VARCHAR(40) NOT NULL,
  source VARCHAR(25) NOT NULL,
  average VARCHAR(4) NOT NULL,
  min VARCHAR(4) NOT NULL,
  max VARCHAR(4) NOT NULL,
  recovery VARCHAR(4) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE strokes
(
  strokenr VARCHAR(5) NOT NULL,
  p VARCHAR(10) NOT NULL,
  t VARCHAR(20) NOT NULL,
  d NUMERIC(10.1) NOT NULL,
  spm NUMERIC(3.1) NOT NULL,
  hr VARCHAR(4) NOT NULL,
  len NUMERIC(4.2) NOT NULL,
  id VARCHAR(10) NOT NULL,
  PRIMARY KEY (strokenr, id),
  FOREIGN KEY (id) REFERENCES workouts(id)
);

CREATE TABLE splits
(
  stroke_rate NUMERIC(3.1) NOT NULL,
  time VARCHAR(40) NOT NULL,
  distance VARCHAR(10) NOT NULL,
  Splitnr INT NOT NULL,
  calories_total VARCHAR(10) NOT NULL,
  max VARCHAR(4) NOT NULL,
  min VARCHAR(4) NOT NULL,
  rest VARCHAR(4) NOT NULL,
  average VARCHAR(4) NOT NULL,
  ending VARCHAR(4) NOT NULL,
  recovery VARCHAR(4) NOT NULL,
  id VARCHAR(10) NOT NULL,
  PRIMARY KEY (Splitnr, id),
  FOREIGN KEY (id) REFERENCES workouts(id)
);


CREATE TABLE `useige` (
  `userID` varchar(20) NOT NULL,
  `time_run` int NOT NULL,
  `lastID` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `amount_of_data` int NOT NULL,
  `date_time` date NOT NULL,
  `timed` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE workout (
    user_id VARCHAR(10) NOT NULL,
    id VARCHAR(10) NOT NULL,
    PRIMARY KEY (user_id, id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (id) REFERENCES workouts(id)
);


ALTER TABLE `workouts` ADD `Filename` VARCHAR(50) NOT NULL AFTER `average`;

ALTER TABLE `workouts` ADD UNIQUE(`Filename`);