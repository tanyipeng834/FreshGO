-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 14, 2019 at 06:42 AM
-- Server version: 5.7.19
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `book`
--
CREATE DATABASE IF NOT EXISTS `inventory` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `inventory`;

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
-- Only one crop type is able to exisit 

DROP TABLE IF EXISTS `inventory`;
CREATE TABLE IF NOT EXISTS `inventory` (
  `name` varchar(30) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `quantity` int(5) NOT NULL,
  PRIMARY KEY (`name`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `CropData`;
CREATE TABLE IF NOT EXISTS `CropData` (
    `name` varchar(30) NOT NULL,
    `batch` int(5) NOT NULL,
    `humidity` decimal(10,2) NOT NULL,
    `water` decimal (10,2) NOT NULL,
    `fertiliser` decimal(10,2) NOT NULL,
    PRIMARY KEY(`name`,`batch`),
    FOREIGN KEY (`name`,`batch`) REFERENCES `inventory`(`name`,`batch`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
DROP TABLE IF EXISTS `CropMeasurements`;
CREATE TABLE IF NOT EXISTS `CropMeasurements` (
    `name` varchar(30) NOT NULL,
    `batch` int(5) NOT NULL,
    `date_measured` DATE NOT NULL,
    `current_height` decimal(10,2) NOT NULL,
    PRIMARY KEY(`name`,`batch`),
    FOREIGN KEY (`name`,`batch`) REFERENCES `inventory`(`name`,`batch`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `inventory` (`name`, `shell_life`, `price`,`quantity`,`batch`,`type`) VALUES
('Xin Hua', '2 Years', 2.0, 3, 1,'vegetable'), 
('Xin Hua', '2 Years', 2.0, 3, 2,'vegetable'), 
('Xin Hua', '2 Years', 2.0, 3, 3,'vegetable'),
('Xin Hua', '2 Years', 2.0, 3, 4,'vegetable'),
('Xin Hua', '2 Years', 2.0, 3,5,'vegetable');
COMMIT;

INSERT INTO `CropData` (`name`, `batch`, `humidity`, `water`, `fertiliser`) VALUES
('Xin Hua', 1, 2.0, 3.0, 3.0),
('Xin Hua', 2, 2.0, 2.0, 2.0),
('Xin Hua', 3, 2.0, 3.0, 2.0),
('Xin Hua', 4, 2.0, 5.0, 3.0),
('Xin Hua', 5, 2.0, 1.0, 4.0);
COMMIT;

INSERT INTO `CropMeasurements` (`name`, `batch`, `date_measured`, `current_height`) VALUES
('Xin Hua', 1, '2021-02-02', 3.0),
('Xin Hua', 2, '2021-02-03', 3.0),
('Xin Hua', 3, '2021-02-04', 4.0),
('Xin Hua', 4, '2021-02-05', 3.0),
('Xin Hua', 5, '2021-02-06', 2.0);
COMMIT;






/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


