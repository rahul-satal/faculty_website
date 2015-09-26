-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Sep 26, 2015 at 11:14 AM
-- Server version: 5.5.41-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `pbas_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `website_achievements`
--

CREATE TABLE IF NOT EXISTS `website_achievements` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `website_achievements`
--

INSERT INTO `website_achievements` (`id`, `name`) VALUES
(1, 'He  has received  Bachelor of Science in  Electronics from Devi Ahilya  University Indore in 1998.'),
(2, ' Master of Science in Computer Science  in  2000 and Master of Technology in Computer Science  in 2007 from School of Computer Science & IT ,DAVV ,Indore.'),
(3, 'He has Qualified UGC-NET (Computer Science and Applications) in 2005 and GATE(Computer Science and Engineering) in 2007.'),
(4, 'He has worked as Reader in Pioneer Institute of Professional Studies (PIPS) Indore  in MCA department and joined International Institute of Professional Studies (IIPS) ,Devi Ahilya University Indore, as Reader for MCA and M.Tech Courses since 2007.'),
(5, 'Presently  he is In-charge  of Development Center at IIPS D. A. University  Indore.');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
