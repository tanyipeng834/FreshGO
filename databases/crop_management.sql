SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

CREATE DATABASE IF NOT EXISTS `crop_management` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `crop_management`;

DROP TABLE IF EXISTS `crops`;
CREATE TABLE IF NOT EXISTS `crops`(
  `batch` int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `name` varchar(50) NOT NULL,
  `max_height` decimal(10, 2) NOT NULL,
  `recommended_water_level` decimal(10, 2) NOT NULL,
  `recommended_fertiliser_level` decimal(10, 2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


INSERT INTO `crops` (`batch`, `name`, `max_height`, `recommended_water_level`, `recommended_fertiliser_level`) VALUES 
(1, "Xin Gua", 10.2, 10.2, 10.2),
(2, "Xin Gua", 10.5, 10.5, 10.5),
(3, "Gua Xin", 2.5, 2.5, 2.5),
(4, "Gua Xin", 5.7, 5.7, 5.7);
COMMIT;




-- DROP TABLE IF EXISTS `crops`;
-- CREATE TABLE crops (
--     id SERIAL PRIMARY KEY,
--     water_level INTEGER NOT NULL,
--     fertiliser INTEGER NOT NULL,
--     height INTEGER NOT NULL,
--     date DATE NOT NULL
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- PREVIOUS TABLE FOR REFERENCE

-- DROP TABLE IF EXISTS `CropData`;
-- CREATE TABLE IF NOT EXISTS `CropData` (
--     `name` varchar(30) NOT NULL,
--     `batch` int(5) NOT NULL AUTO_INCREMENT,
--     `humidity` decimal(10,2) NOT NULL,
--     `water` decimal (10,2) NOT NULL,
--     `fertiliser` decimal(10,2) NOT NULL,
--     PRIMARY KEY(`batch`)
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- DROP TABLE IF EXISTS `CropMeasurements`;
-- CREATE TABLE IF NOT EXISTS `CropMeasurements` (
--     `name` varchar(30) NOT NULL,
--     `batch` int(5) NOT NULL,
--     `date_measured` DATE NOT NULL,
--     `current_height` decimal(10,2) NOT NULL,
--     PRIMARY KEY(`name`),
--     FOREIGN KEY (`name`) REFERENCES `inventory`(`name`) ON DELETE CASCADE
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8;



-- INSERT INTO `CropData` (`name`, `batch`, `humidity`, `water`, `fertiliser`) VALUES
-- ('Xin Hua', 1, 2.0, 3.0, 3.0),
-- ('Xin Hua', 2, 2.0, 2.0, 2.0),
-- ('Xin Hua', 3, 2.0, 3.0, 2.0),
-- ('Xin Hua', 4, 2.0, 5.0, 3.0),
-- ('Xin Hua', 5, 2.0, 1.0, 4.0);
-- COMMIT;

-- INSERT INTO `CropMeasurements` (`name`, `batch`, `date_measured`, `current_height`) VALUES
-- ('Xin Hua', 1, '2021-02-02', 3.0),
-- ('Xin Hua', 2, '2021-02-03', 3.0),
-- ('Xin Hua', 3, '2021-02-04', 4.0),
-- ('Xin Hua', 4, '2021-02-05', 3.0),
-- ('Xin Hua', 5, '2021-02-06', 2.0);
-- COMMIT;
