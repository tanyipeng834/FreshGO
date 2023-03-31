SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

CREATE DATABASE IF NOT EXISTS `crop_management` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `crop_management`;

DROP TABLE IF EXISTS `crop`;
CREATE TABLE IF NOT EXISTS `crop`(
  `batch` int(10) NOT NULL,
  `name` varchar(50) NOT NULL,
  `height` decimal(10, 2) NOT NULL,
  `water_used` decimal(10,2) NOT NULL,
  `quantity` int(10) NOT NULL,
  `fertiliser_used` decimal(10,2) NOT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT PK_NAME PRIMARY KEY (`batch`, `name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;;

INSERT INTO `crop` (`batch`, `name`, `height`, `water_used`, `quantity`,`fertiliser_used`) VALUES 
(1, "Xiao Bai Cai", 2, 50, 12,5),
(2, "Xiao Bai Cai", 2, 50, 12,5),
(3, "Xiao Bai Cai", 2, 50, 12,5),
(4, "Xiao Bai Cai", 2, 50, 12,5),
(5, "Xiao Bai Cai", 2.1, 52, 12,5.1),
(6, "Xiao Bai Cai", 2.1, 53, 12,5.1),
(7, "Xiao Bai Cai", 2.1, 51, 12,5.1),
(8, "Xiao Bai Cai", 2.1, 50, 12,5.2),
(9, "Xiao Bai Cai", 2.1, 50, 12,5.1),
(10, "Xiao Bai Cai", 2.1, 52, 12,5.1),
(11, "Xiao Bai Cai", 2.2, 53, 12,5.2),
(12, "Xiao Bai Cai", 2.2, 53, 12,5.2),
(13, "Xiao Bai Cai", 2.2, 54, 12,5.2),
(14, "Xiao Bai Cai", 2.2, 53, 12,5.3),
(15, "Xiao Bai Cai", 2.2, 55, 12,5.4),
(16, "Xiao Bai Cai", 2.2, 56, 12,5.3),
(17, "Xiao Bai Cai", 2.3, 53, 12,5.2),
(18, "Xiao Bai Cai", 2.3, 57, 12,5.4),
(19, "Xiao Bai Cai", 2.3, 56, 12,5.5),
(20, "Xiao Bai Cai", 2.3, 56, 12,5.5),
(21, "Xiao Bai Cai", 2.4, 50, 12,5.5),
(22, "Xiao Bai Cai", 2.5, 50, 12,5.5),
(23, "Xiao Bai Cai", 2.5, 50, 12,5.5),
(24, "Xiao Bai Cai", 2.6, 50, 12,5.6),
(25, "Xiao Bai Cai", 2.7, 52, 12,5.5),
(26, "Xiao Bai Cai", 2.8, 53, 12,5.5),
(27, "Xiao Bai Cai", 2.8, 51, 12,5.4),
(28, "Xiao Bai Cai", 2.8, 50, 12,5.6),
(29, "Xiao Bai Cai", 3.0, 50, 12,5.5),
(30, "Xiao Bai Cai", 3.1, 52, 12,5.7),
(31, "Xiao Bai Cai", 3.0, 53, 12,5.8),
(32, "Xiao Bai Cai", 3.0, 53, 12,6.0),
(33, "Xiao Bai Cai", 3.1, 54, 12,6.0),
(34, "Xiao Bai Cai", 3.2, 53, 12,6.1),
(35, "Xiao Bai Cai", 3.2, 55, 12,6.0),
(36, "Xiao Bai Cai", 3.1, 56, 12,6.2),
(37, "Xiao Bai Cai", 3.3, 53, 12,6.3),
(38, "Xiao Bai Cai", 3.1, 57, 12,6.0),
(39, "Xiao Bai Cai", 3.2, 56, 12,6.3),
(40, "Xiao Bai Cai", 3.4, 56, 12,6.2),
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
