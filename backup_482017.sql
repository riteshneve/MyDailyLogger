-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: mydailylogger
-- ------------------------------------------------------
-- Server version	5.7.17-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `info`
--

DROP TABLE IF EXISTS `info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dates` int(11) DEFAULT NULL,
  `kms` int(11) DEFAULT NULL,
  `summary` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=180 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `info`
--

LOCK TABLES `info` WRITE;
/*!40000 ALTER TABLE `info` DISABLE KEYS */;
INSERT INTO `info` VALUES (23,20171201,4,'work and back'),(24,20171301,4,'work and back'),(25,20171501,13,'varun and back'),(26,20171501,8,'Bike hunt'),(36,20171601,4,'work and back'),(37,20171701,4,'work and back'),(38,20171801,4,'work and back'),(39,20171901,4,'work and back'),(40,20172001,4,'work and back'),(41,20172101,1,'breakfast'),(42,20172101,11,'nucleus and back'),(43,20172201,1,'breakfast'),(44,20172301,4,'work and back'),(45,20172401,4,'work and back'),(46,20172501,4,'work and back'),(47,20172501,315,'pune to csn'),(48,20172701,450,'shegaon trip'),(49,20172801,471,'shegaon trip'),(50,20172901,2,'around'),(51,20173001,10,'around'),(52,20173001,307,'csn to pune'),(53,20173101,4,'work and back'),(54,20173101,14,'amanora and back'),(55,20170102,6,'work and back twice'),(56,20170202,6,'work and back twice'),(57,20170302,6,'work and back twice'),(58,20170602,4,'work and back'),(59,20170702,6,'work and back twice'),(60,20170802,4,'work and back'),(61,20170902,4,'work and back'),(62,20171002,4,'work and back'),(63,20171202,13,'home to mangala'),(64,20171202,6,'shivajinagar to dandekar bridge'),(65,20171202,7,'dandekar bridge to katraj'),(66,20171202,23,'katraj to home'),(67,20171302,4,'work and back'),(68,20171402,4,'work and back'),(69,20171502,4,'work and back'),(70,20171602,4,'work and back'),(71,20171702,4,'work and back'),(72,20171802,28,'College and back'),(73,20171902,16,'Phoenix and back'),(74,20172002,4,'work and back'),(75,20172102,4,'work and back'),(76,20172202,4,'work and back'),(77,20172302,4,'work and back'),(78,20172202,2,'bajaj and back'),(79,20172402,200,'Diveagar'),(80,20172502,200,'Diveagar'),(81,20172602,5,'Around'),(84,20172702,4,'work and back'),(85,20172802,4,'work and back'),(90,20171201,4,'work and back'),(91,20171101,4,'work and back'),(92,20171001,1,'blueberry and back'),(93,20170901,4,'work and back'),(94,20170801,11,'Pune jn to home'),(95,20170801,150,'kalyan jn to pune'),(96,20170801,2,'sharada to kalyan'),(97,20170801,5,'around'),(98,20170801,25,'Vijay vatika to sharada'),(99,20170701,3,'around'),(100,20170701,8,'thane to vijay vatika'),(101,20170701,153,'swargate to thane'),(102,20170701,16,'home to swargate'),(103,20170201,4,'work and back'),(104,20170301,4,'work and back'),(105,20170401,4,'work and back'),(106,20170501,4,'work and back'),(107,20170601,4,'work and back'),(108,20170101,5,'Baner to wakad'),(109,20170101,15,'wakad to manapa JAN1'),(110,20170101,14,'manapa to home JAN1'),(111,20170103,4,'work and back'),(112,20170203,4,'work and back'),(113,20170303,4,'work and back'),(114,20170303,20,'Jehangir and back'),(115,20170403,20,'Jehangir and back'),(116,20170403,9,'phoenix and back'),(117,20170503,10,'home to jehangir'),(118,20170503,7,'jehangir to swargate'),(119,20170503,18,'swargate to bajaj'),(120,20170503,12,'around'),(121,20170503,2,'bajaj to home'),(122,20170503,10,'wagholi and back'),(123,20170603,4,'work and back'),(124,20170703,4,'work and back'),(125,20170803,4,'work and back'),(126,20170903,4,'work and back'),(127,20171003,4,'work and back'),(128,20171103,2,'breakfast'),(129,20171103,2,'lunch'),(130,20171103,8,'helmet'),(131,20171203,160,'Rajgad'),(132,20171203,20,'Jahangir and back'),(133,20171303,11,'Vimannagar and back'),(134,20171403,20,'Station and back'),(135,20171403,4,'work and back'),(136,20171503,4,'work and back'),(137,20171603,4,'work and back'),(138,20171703,4,'work and back'),(139,20171803,2,'breakfast'),(140,20171803,37,'swargate deccan home'),(141,20171903,2,'breakfast'),(142,20171903,30,'Khadki and back'),(143,20172003,4,'work and back'),(144,20172103,4,'work and back'),(145,20172203,4,'work and back'),(146,20172303,4,'work and back'),(147,20172403,4,'work and back'),(148,20172303,17,'gaurav birthday'),(149,20172403,18,'bbq'),(150,20172503,54,'Kondwa and back'),(162,20170404,5,'bajaj and back'),(163,20170304,4,'gym and back'),(164,20170304,4,'work and back'),(165,20170204,9,'phoenix and back'),(166,20172603,9,'Vimannagar and back'),(167,20172703,4,'work and back'),(168,20172703,188,'Pawana lake'),(169,20172903,4,'work and back'),(170,20173003,4,'work and back'),(171,20173103,4,'work and back'),(172,20170104,4,'gym and back'),(173,20170204,1,'breakfast'),(174,20170404,4,'gym and back'),(175,20170504,4,'work and back'),(176,20170604,4,'work and back'),(177,20170704,4,'work and back'),(178,20170704,25,'Shivajinagar and back'),(179,20170804,1,'breakfast');
/*!40000 ALTER TABLE `info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `maininfo`
--

DROP TABLE IF EXISTS `maininfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `maininfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` int(11) DEFAULT NULL,
  `kms` int(11) DEFAULT NULL,
  `desc` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maininfo`
--

LOCK TABLES `maininfo` WRITE;
/*!40000 ALTER TABLE `maininfo` DISABLE KEYS */;
INSERT INTO `maininfo` VALUES (1,20170402,2,NULL);
/*!40000 ALTER TABLE `maininfo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-04-08  8:16:40
