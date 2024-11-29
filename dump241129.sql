/*
SQLyog Ultimate v12.5.1 (64 bit)
MySQL - 10.4.32-MariaDB : Database - project
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`project` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_hungarian_ci */;

USE `project`;

/*Table structure for table `currencies` */

DROP TABLE IF EXISTS `currencies`;

CREATE TABLE `currencies` (
  `id` tinyint(3) unsigned NOT NULL AUTO_INCREMENT,
  `name` enum('EUR','GBP','RUB','USD','DDM','FRF','ITL','HUF') NOT NULL,
  `defAmount` tinyint(4) NOT NULL DEFAULT 0,
  `lastDate` date NOT NULL DEFAULT '2024-10-21',
  `closed` tinyint(1) NOT NULL DEFAULT 0,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  CONSTRAINT `currencies_ibfk_1` FOREIGN KEY (`id`) REFERENCES `exchanges` (`currId`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci MAX_ROWS=8;

/*Data for the table `currencies` */

insert  into `currencies`(`id`,`name`,`defAmount`,`lastDate`,`closed`,`timestamp`) values 
(0,'EUR',1,'2024-10-21',0,'2024-11-06 10:56:36'),
(1,'GBP',1,'2024-10-21',0,'2024-11-06 10:56:36'),
(2,'RUB',1,'2024-10-21',0,'2024-11-06 10:56:36'),
(3,'USD',1,'2024-10-21',0,'2024-11-06 10:56:36'),
(4,'DDM',100,'1967-11-20',1,'2024-11-06 10:56:36'),
(5,'FRF',1,'2002-03-29',1,'2024-11-06 10:56:36'),
(6,'ITL',127,'2002-03-29',1,'2024-11-06 10:56:36'),
(7,'HUF',1,'2024-10-21',0,'2024-11-29 12:45:58');

/*Table structure for table `exchanges` */

DROP TABLE IF EXISTS `exchanges`;

CREATE TABLE `exchanges` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `userId` int(10) unsigned NOT NULL,
  `currId` tinyint(3) unsigned NOT NULL DEFAULT 1,
  `exDate` date NOT NULL,
  `value` int(11) NOT NULL DEFAULT 1,
  `timeStamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `userId` (`userId`),
  KEY `currId` (`currId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `nationality` enum('Hungarian','British','German','Russian','French','Italian','Other') NOT NULL DEFAULT 'Hungarian',
  `firstName` varchar(100) NOT NULL,
  `lastName` varchar(100) NOT NULL,
  `taxNumber` int(10) NOT NULL,
  `address` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` int(20) unsigned DEFAULT NULL,
  `regDate` timestamp NOT NULL DEFAULT current_timestamp(),
  `deleted` tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`id`) REFERENCES `exchanges` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
