/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - personal_safety
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`personal_safety` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `personal_safety`;

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `pcid` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL,
  `pid` int(11) NOT NULL,
  `complaint` varchar(50) NOT NULL,
  `date` varchar(15) NOT NULL,
  `replay` varchar(50) NOT NULL,
  PRIMARY KEY (`pcid`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`pcid`,`uid`,`pid`,`complaint`,`date`,`replay`) values 
(11,20,13,'ok','2022-01-06','ok'),
(12,20,14,'please','2022-01-06','why');

/*Table structure for table `emergency` */

DROP TABLE IF EXISTS `emergency`;

CREATE TABLE `emergency` (
  `eid` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL,
  `pid` int(11) NOT NULL,
  `message` varchar(50) NOT NULL,
  `latitude` float NOT NULL,
  `longitude` float NOT NULL,
  `date_time` datetime DEFAULT NULL,
  PRIMARY KEY (`eid`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `emergency` */

insert  into `emergency`(`eid`,`uid`,`pid`,`message`,`latitude`,`longitude`,`date_time`) values 
(14,20,13,'Help me',11.2604,75.7813,'2022-01-06 14:43:12');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `loginid` int(11) NOT NULL,
  `type` varchar(50) NOT NULL,
  `fback_cmnd` varchar(50) NOT NULL,
  `rating` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `replay` varchar(50) NOT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`fid`,`loginid`,`type`,`fback_cmnd`,`rating`,`date`,`replay`) values 
(8,13,'police','good','4','2022-01-06','pending'),
(19,16,'user','ok','4.0','2022-01-06','pending'),
(20,20,'user','ok','4.0','2022-01-06','pending'),
(21,13,'police','hiii','1','2022-01-06','pending'),
(22,20,'user','perfect','3.0','2022-01-06','pending');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `loginid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`loginid`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`loginid`,`username`,`password`,`type`) values 
(1,'jss','psa','admin'),
(13,'kalpetta','Kalpetta123','police'),
(14,'mananthavady','Mananthavady123','police'),
(20,'achu','achu','user');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `pid` int(11) NOT NULL,
  `notification` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  PRIMARY KEY (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`nid`,`pid`,`notification`,`date`) values 
(27,13,'ertyui','2022-01-06'),
(28,14,'alert','2022-01-06');

/*Table structure for table `police_station_details` */

DROP TABLE IF EXISTS `police_station_details`;

CREATE TABLE `police_station_details` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `pname` varchar(50) NOT NULL,
  `pphone` bigint(20) NOT NULL,
  `pmail` varchar(50) NOT NULL,
  `place` varchar(50) NOT NULL,
  `post` varchar(50) NOT NULL,
  `pin` int(11) NOT NULL,
  `latitude` float NOT NULL,
  `longitude` float NOT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `police_station_details` */

insert  into `police_station_details`(`pid`,`lid`,`pname`,`pphone`,`pmail`,`place`,`post`,`pin`,`latitude`,`longitude`) values 
(9,13,'kalpetta',9074664644,'shisamolkr@gmail.com','kalpetta','KALPETTA',673121,74.456,11.654),
(10,14,'mananthavady',6238083618,'jancyraju756@gmail.com','mananthavady','MANANTHAVADY',673593,76.45,11.6596);

/*Table structure for table `user_details` */

DROP TABLE IF EXISTS `user_details`;

CREATE TABLE `user_details` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `loginid` int(11) NOT NULL,
  `firstname` varchar(50) NOT NULL,
  `lastname` varchar(50) NOT NULL,
  `phoneno` bigint(20) NOT NULL,
  `mailid` varchar(50) NOT NULL,
  `age` int(11) NOT NULL,
  `gender` varchar(30) NOT NULL,
  `place` varchar(50) NOT NULL,
  `post` varchar(50) NOT NULL,
  `pin` bigint(20) NOT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `user_details` */

insert  into `user_details`(`uid`,`loginid`,`firstname`,`lastname`,`phoneno`,`mailid`,`age`,`gender`,`place`,`post`,`pin`) values 
(8,20,'achu','s',7025954857,'123sangeethadas@gmail.com',22,'female','kochi','kochi',673245);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
