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
-- Database: `profile`
--
CREATE DATABASE IF NOT EXISTS `inventory_manager` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `inventory_manager`;

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `growth`;
CREATE TABLE IF NOT EXISTS `growth` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `farmer` varchar(30) NOT NULL,
  `crop` varchar(30) NOT NULL,
  `quantity` int(255) NOT NULL,
  `date_grown` DATE NOT NULL,
  `date_harvested` DATE NOT NULL,
  PRIMARY KEY (`id`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE growth AUTO_INCREMENT=10000;

-- Dumping data for table `customer`
--
-- INSERT INTO `profile` (`id`) VALUES
-- (1111111111),(2222222222);
-- COMMIT;

-- INSERT INTO `customer` (`id`, `name`, `email`, `phone`, `address`) VALUES
-- (1111111111, 'Please', 'Work@gmail.com', '12345678', 'Earth');
-- COMMIT;

-- INSERT INTO `staff` (`id`, `name`, `email`, `phone`) VALUES
-- (2222222222, 'Please', 'Work@gmail.com', '13213315');
-- COMMIT;



/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
