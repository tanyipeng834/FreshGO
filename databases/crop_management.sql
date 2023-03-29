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
(1, "Xiao Bai Cai", 2, 100, 12,100),
(2, "Xiao Bai Cai", 3, 110, 13,101),
(1, "Xin Hua", 4, 100,12, 120),
(2, "Xin Hua", 5, 120, 11,150),
(1, "Xin Ba", 2.5, 121, 11,102),
(1, "Xin Ma", 5.7, 130, 11,120),
(3,"Xiao Bai Cai", 2.5, 120, 14, 102),
(4,"Xiao Bai Cai", 3.2, 130, 15, 103),
(5,"Xiao Bai Cai", 3.8, 140, 16, 104),
(6,"Xiao Bai Cai", 4.1, 150, 17, 105),
(7,"Xiao Bai Cai", 4.5, 160, 18, 106),
(8,"Xiao Bai Cai", 5.0, 170, 19, 107),
(9,"Xiao Bai Cai", 5.2, 180, 20, 108),
(10,"Xiao Bai Cai", 5.5, 190, 21, 109),
(11,"Xiao Bai Cai", 5.8, 200, 22, 110),
(12,"Xiao Bai Cai", 6.0, 210, 23, 111),
(13,"Xiao Bai Cai", 6.2, 220, 24, 112),
(14,"Xiao Bai Cai", 6.4, 230, 25, 113),
(15,"Xiao Bai Cai", 6.6, 240, 26, 114),
(16,"Xiao Bai Cai", 6.8, 250, 27, 115),
(17,"Xiao Bai Cai", 7.0, 260, 28, 116),
(18,"Xiao Bai Cai", 7.2, 270, 29, 117),
(19,"Xiao Bai Cai", 7.4, 280, 30, 118),
(20,"Xiao Bai Cai", 7.6, 290, 31, 119),
(21,"Xiao Bai Cai", 7.8, 300, 32, 120),
(22,"Xiao Bai Cai", 8.0, 310, 33, 121);
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
