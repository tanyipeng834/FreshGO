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
-- Database: 'order'
--
CREATE DATABASE IF NOT EXISTS 'PURCHASE_ACTIVITY' DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE 'PURCHASE_ACTIVITY';

-- --------------------------------------------------------

--
-- Table structure for table 'order'
--

DROP TABLE IF EXISTS 'purchase_activity';
CREATE TABLE IF NOT EXISTS 'purchase_activity' (
  'purchase_id' int(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
  'customer_id' varchar(32) NOT NULL,
  'crop_purchase' varchar[] NOT NULL,
  'delivery_staff_id' int(11) NOT NULL,
  'customer_location' varchar(50) NOT NULL,
  'transaction_amount' float(10) NOT NULL,
  'status' varchar(10) NOT NULL DEFAULT 'Ongoing/New',
  'created' timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  'modified' timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY ('purchase_id')
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--

/*INSERT INTO 'purchase' ('purchase_id', 'customer_id', 'status', 'created', 'modified') VALUES
(1, 'Apple TAN', 'NEW', '2020-06-12 02:14:55', '2020-06-12 02:14:55'); */

-- --------------------------------------------------------
--


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

