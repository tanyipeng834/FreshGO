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
CREATE DATABASE IF NOT EXISTS `profile` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `profile`;

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `profile`;
CREATE TABLE IF NOT EXISTS `profile` (
  `id` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `customer`;
CREATE TABLE IF NOT EXISTS `customer` (
  `name` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `phone` int(8) NOT NULL,
  `address` varchar(30) NOT NULL,
  `id` int(10) NOT NULL,
  FOREIGN KEY (`id`) REFERENCES profile(`id`),
  PRIMARY KEY (`phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `staff`;
CREATE TABLE IF NOT EXISTS `staff` (
  `name` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `phone` int(8) NOT NULL,
  `id` int(10) NOT NULL,
  FOREIGN KEY (`id`) REFERENCES profile(`id`),
  PRIMARY KEY (`phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `farmer`;
CREATE TABLE IF NOT EXISTS `farmer` (
  `name` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `phone` int(8) NOT NULL,
  `address` varchar(30) NOT NULL,
  `id` int(10) NOT NULL,
  FOREIGN KEY (`id`) REFERENCES profile(`id`),
  PRIMARY KEY (`phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Dumping data for table `customer`
--
INSERT INTO `profile` (`id`) VALUES
(1111111111),(2222222222);
COMMIT;

INSERT INTO `customer` (`id`, `name`, `email`, `phone`, `address`) VALUES
(1111111111, 'Please', 'Work@gmail.com', '12345678', 'Earth');
COMMIT;

INSERT INTO `staff` (`id`, `name`, `email`, `phone`) VALUES
(2222222222, 'Please', 'Work@gmail.com', '13213315');
COMMIT;



/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
