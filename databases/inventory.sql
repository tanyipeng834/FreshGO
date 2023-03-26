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
  `quantity` int NOT NULL,
  `price` decimal(5,2) NOT NULL,
  `type` varchar(30) NOT NULL,
  `status` varchar(30) NOT NULL,
  PRIMARY KEY (`name`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- Inserting some data into the inventory table


INSERT INTO `inventory` (`name`, `quantity`,`price`, `type`,`status`) VALUES 
("Xiao Bai Cai", 15,5,"Vegetable", "Low");
COMMIT;








/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


