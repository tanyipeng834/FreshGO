-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 30, 2023 at 03:03 PM
-- Server version: 8.0.27
-- PHP Version: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `profile`
--
CREATE DATABASE IF NOT EXISTS `profile` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `profile`;

-- --------------------------------------------------------

--
-- Table structure for table `crop_purchased`
--

DROP TABLE IF EXISTS `crop_purchased`;
CREATE TABLE IF NOT EXISTS `crop_purchased` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `purchase_id` int NOT NULL,
  `crop_name` varchar(32) NOT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`order_id`),
  KEY `purchase_id` (`purchase_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `profile`
--

DROP TABLE IF EXISTS `profile`;
CREATE TABLE IF NOT EXISTS `profile` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(30) NOT NULL,
  `password` char(255) NOT NULL,
  `profile_type` char(255) NOT NULL,
  `name` varchar(30) NOT NULL,
  `phone` varchar(30) NOT NULL,
  `address` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10009 DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `profile`
--

INSERT INTO `profile` (`id`, `email`, `password`, `profile_type`, `name`, `phone`, `address`) VALUES
(10001, 'hello@gmail.com', 'hello', 'customer', 'hello', '96642813', 'woodlands'),
(10002, 'hello446111@gmail.com', '$2b$12$E4O/QNQsU8ClvWXLw7Z17.PrU5XYPcsYvfwWE.CtJSZR06VExk1be', 'customer', 'Tan Yi Peng', '96642813', '80 Stamford Rd, Singapore 1789'),
(10003, 'wuhao@gmail.com', '$2b$12$LoBgkM56rRfViOON./klOO9ofAMIncJRlt1x10EAI/vqvTl/IwG1y', 'staff', 'wuhao', '93486088', '80 Stamford Rd, Singapore 1789'),
(10004, 'yipeng1234@gmail.com', '$2b$12$1rL48P.jkN7bXzACaIzsFeC9pDXP2mb4oy4NFajKcNeODO2t3p9PW', 'customer', 'yipeng', '96642813', '80 Stamford Rd, Singapore 1789'),
(10005, 'yipeng123456@gmail.com', '$2b$12$nHXkgfWFgVIv1GrOWr7Iq.YG1yHlBOKTHkRozjLZKaZE4KOmJOLiu', 'farmer', 'yipeng', '93486088', '80 Stamford Rd, Singapore 1789'),
(10006, 'customer@gmail.com', '$2b$12$am7cKRlbgmIiqKrfWqRAs.dxRa9fOROK1AxMXilO8IuWyZcjhvfwO', 'customer', 'Tan Yi Peng', '96642813', '80 Stamford Rd, Singapore 1789'),
(10007, 'delivery@gmail.com', '$2b$12$am7cKRlbgmIiqKrfWqRAs.y9i/7Pih0EHdwixR/Yt5.0hkUxHHX2m', 'staff', 'Tan Yi Peng', '96642813', '80 Stamford Rd, Singapore 1789'),
(10008, 'delivery123@gmail.com', '$2b$12$ozFejAt5UM16RV6EMxO4YOg/w88IJoOHb/otz1we9MRnnStWD4hbe', 'staff', 'hello', '96642813', 'bdasfa');

-- --------------------------------------------------------

--
-- Table structure for table `purchase_activity`
--

DROP TABLE IF EXISTS `purchase_activity`;
CREATE TABLE IF NOT EXISTS `purchase_activity` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int NOT NULL,
  `customer_location` int NOT NULL,
  `transaction_amount` float NOT NULL,
  `status` varchar(32) NOT NULL DEFAULT 'Ongoing/New',
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `crop_purchased`
--
ALTER TABLE `crop_purchased`
  ADD CONSTRAINT `crop_purchased_ibfk_1` FOREIGN KEY (`purchase_id`) REFERENCES `purchase_activity` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
