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

/*Data for the table `bonuses` */

/*Data for the table `currencies` */

/*Data for the table `exchanges` */

/*Data for the table `firms` */

/*Data for the table `persons` */

insert  into `persons`(`id`,`userId`,`firstName`,`lastName`,`address`,`email`,`phone`,`updated`,`deleted`) values 
(1,2,'Kis','Kata','witgw','kiskata@freemail.hu',4294967295,'2024-11-06 11:36:59',0);

/*Data for the table `transactions` */

/*Data for the table `user` */

/*Data for the table `userlevel` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
