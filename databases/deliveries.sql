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
CREATE DATABASE IF NOT EXISTS `deliveries` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `deliveries`;

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
-- Only one crop type is able to exisit 

DROP TABLE IF EXISTS `deliveries`;
CREATE TABLE IF NOT EXISTS `deliveries` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `customer_name` varchar(30) NOT NULL,
  `customer_phone` varchar(30) NOT NULL,
  `customer_location` varchar(30) NOT NULL,
  `delivery_charge` decimal(5,2) NOT NULL,
  PRIMARY KEY (`id`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `deliveries` (`id`,`customer_name`,`customer_phone`,`customer_location`,`delivery_charge`) VALUES
('1','Tan Yi Peng','96642813','BLK 835 Woodlands Street 83',3.00);
COMMIT;