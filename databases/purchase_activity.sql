-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jun 12, 2020 at 02:17 AM
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
-- Database: `order`
--
CREATE DATABASE IF NOT EXISTS `PURCHASE_ACTIVITY`DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `PURCHASE_ACTIVITY`;

-- --------------------------------------------------------

--
-- Table structure for table 
--
DROP TABLE IF EXISTS `purchase_activity`;
CREATE TABLE IF NOT EXISTS `purchase_activity`(
  `id`int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `customer_id`int NOT NULL,
  `customer_location`varchar(32) NOT NULL,
  `transaction_amount` float not null,
  `status`varchar(32) NOT NULL DEFAULT 'Ongoing/New',
  `created`timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP  
) ENGINE=InnoDB DEFAULT CHARSET=utf8;;

DROP TABLE IF EXISTS `crop_purchased`;
CREATE TABLE IF NOT EXISTS `crop_purchased`(
  `order_id` int primary key not null AUTO_INCREMENT ,
  `purchase_id`int NOT NULL,
  `crop_name` varchar(32)  not null,
  `quantity` int not null,
  constraint FOREIGN KEY(`purchase_id`) REFERENCES `purchase_activity`(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;;


--

INSERT INTO `purchase_activity`(`id`, `customer_id`, `customer_location`,`transaction_amount`) VALUES
(1, 1, 100000,17.50);
INSERT INTO `crop_purchased`(`order_id`, `purchase_id`, `crop_name`, `quantity`) VALUES
(1, 1, 'Xin Hua', 1);

-- --------------------------------------------------------
--


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;