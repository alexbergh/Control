-- MariaDB dump 10.19  Distrib 10.8.3-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: control
-- ------------------------------------------------------
-- Server version	10.8.3-MariaDB-1:10.8.3+maria~jammy

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `control`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `control` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `control`;

--
-- Table structure for table `cat-subcat_rel`
--

DROP TABLE IF EXISTS `cat-subcat_rel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cat-subcat_rel` (
  `category` varchar(8) NOT NULL,
  `subcategory` tinyint(4) NOT NULL,
  PRIMARY KEY (`category`,`subcategory`),
  KEY `cat_subcat_rel_FK_1` (`subcategory`),
  CONSTRAINT `cat_subcat_rel_FK` FOREIGN KEY (`category`) REFERENCES `category` (`name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `cat_subcat_rel_FK_1` FOREIGN KEY (`subcategory`) REFERENCES `subcategory` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cat-subcat_rel`
--

LOCK TABLES `cat-subcat_rel` WRITE;
/*!40000 ALTER TABLE `cat-subcat_rel` DISABLE KEYS */;
INSERT INTO `cat-subcat_rel` VALUES
('ОТ',18),
('ОТ',19),
('ОТ',20),
('ОТ',21),
('ОТ',22),
('ОТ',23),
('ОТ',24),
('ОТ',25),
('ОТ',26),
('ОТ',35),
('ОТ',37),
('ПБ',21),
('ПБ',25),
('ПБ',26),
('ПБ',27),
('ПБ',28),
('ПБ',29),
('ПБ',30),
('ПБ',31),
('ПБ',35),
('ПБ',37),
('ПрБ',21),
('ПрБ',22),
('ПрБ',23),
('ПрБ',33),
('ПрБ',34),
('ПрБ',35),
('ПрБ',37),
('ТЭ',21),
('ТЭ',32),
('ТЭ',33),
('ТЭ',34),
('ТЭ',35),
('ТЭ',36),
('ТЭ',37),
('ЭБ',21),
('ЭБ',24),
('ЭБ',25),
('ЭБ',26),
('ЭБ',35),
('ЭБ',37);
/*!40000 ALTER TABLE `cat-subcat_rel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `category` (
  `name` varchar(8) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES
('ОТ'),
('ПБ'),
('ПрБ'),
('ТЭ'),
('ЭБ');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `department` (
  `name` varchar(16) NOT NULL,
  `responsible` bit(1) DEFAULT b'0',
  `inspector` bit(1) DEFAULT b'0',
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES
('АД','\0','\0'),
('АХО','','\0'),
('ГОиЧС','\0','\0'),
('Здравпункт','\0','\0'),
('КТЦ','',''),
('ОБиР','\0','\0'),
('ОЗПиСК','\0','\0'),
('ОИТиТ','',''),
('ОМТСиУЗ','',''),
('ООТиПБ','\0',''),
('ОРТПиР','',''),
('ОСРиРТЭ','\0','\0'),
('ОТД','',''),
('ОУП','\0','\0'),
('ОЦО','\0','\0'),
('ОЭ','',''),
('Пресс-Служба','\0','\0'),
('ПТО','','\0'),
('ПЭО','\0','\0'),
('СЧ','\0','\0'),
('ФО','\0','\0'),
('ХЦ','',''),
('ЦАСУТП','',''),
('ЦТиИК','',''),
('ЦХЛ','',''),
('ЦЦР','',''),
('ЭЦ','',''),
('ЮО','\0','\0');
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inspection`
--

DROP TABLE IF EXISTS `inspection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inspection` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `work_id` varchar(32) DEFAULT NULL,
  `created` datetime DEFAULT current_timestamp(),
  `level` tinyint(4) unsigned DEFAULT NULL,
  `type` varchar(16) DEFAULT NULL,
  `department` varchar(16) DEFAULT NULL,
  `inspector` varchar(128) DEFAULT NULL,
  `shift` tinyint(4) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inspection`
--

LOCK TABLES `inspection` WRITE;
/*!40000 ALTER TABLE `inspection` DISABLE KEYS */;
INSERT INTO `inspection` VALUES
(1,'a','2023-08-21 23:03:09',1,'Обход','ЦАСУТП','Иванов И.И.',1),
(2,'a','2023-08-21 23:03:09',1,'Обход','КТЦ','Иванов И.И.',2),
(3,'abc','2023-08-21 23:03:09',1,'Предписание','ЦАСУТП','Иванов И.И.',1),
(4,'abc','2022-08-21 23:03:09',1,'Обход','ЦАСУТП','Иванов И.И.',1),
(5,'abc','2022-08-21 23:03:09',1,'Обход','ЭЦ','Иванов И.И.',1);
/*!40000 ALTER TABLE `inspection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `issue`
--

DROP TABLE IF EXISTS `issue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `issue` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `inspection_id` int(11) unsigned DEFAULT NULL,
  `place` text DEFAULT NULL,
  `issue` text DEFAULT NULL,
  `repair_before` datetime DEFAULT NULL,
  `responsible` varchar(16) DEFAULT NULL,
  `category` varchar(8) DEFAULT NULL,
  `subcategory` varchar(128) DEFAULT NULL,
  `measures` text DEFAULT NULL,
  `repair_date` datetime DEFAULT NULL,
  `repair_department` varchar(16) DEFAULT NULL,
  `repair_user` varchar(128) DEFAULT NULL,
  `repair_comment` text DEFAULT NULL,
  `confirmation_date` datetime DEFAULT NULL,
  `confirmation_department` varchar(16) DEFAULT NULL,
  `confirmation_user` varchar(128) DEFAULT NULL,
  `confirmation_comment` text DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `issue_FK` (`inspection_id`),
  CONSTRAINT `issue_FK` FOREIGN KEY (`inspection_id`) REFERENCES `inspection` (`id`) ON DELETE SET NULL ON UPDATE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `issue`
--

LOCK TABLES `issue` WRITE;
/*!40000 ALTER TABLE `issue` DISABLE KEYS */;
INSERT INTO `issue` VALUES
(1,1,'place','text','2023-08-21 23:03:09','ЦАСУТП','ОТ','Средства индивидуальной и коллективной защиты','fix all','2023-08-21 23:03:09','ASUTP','user','repair text','2023-08-21 23:03:09','ЦАСУТП','user','1'),
(2,1,'place','text','2023-08-21 23:03:09','ЦАСУТП','ОТ','Средства индивидуальной и коллективной защиты','fix all','2023-08-21 23:03:09','ASUTP','user','repair text','2023-08-21 23:03:09','OT','user','1'),
(3,2,'place','text','2023-08-21 23:03:09','КТЦ','ОТ','Средства индивидуальной и коллективной защиты','fix all','2023-08-21 23:03:09','ASUTP','user','repair text','2023-08-21 23:03:09','ec','user','1'),
(4,2,'place','text','2023-08-21 23:03:09','ЦАСУТП','ОТ','Средства индивидуальной и коллективной защиты','fix all','2023-08-21 23:03:09','ASUTP','user','repair text','2023-08-21 23:03:09','aa','user','1'),
(5,1,'place','text','2023-08-21 23:03:09','ЦАСУТП','ОТ','Средства индивидуальной и коллективной защиты','fix all','2023-08-21 23:03:09','ASUTP','user','repair text','2023-08-21 23:03:09','ewq','user','1');
/*!40000 ALTER TABLE `issue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `position`
--

DROP TABLE IF EXISTS `position`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `position` (
  `name` varchar(128) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `position`
--

LOCK TABLES `position` WRITE;
/*!40000 ALTER TABLE `position` DISABLE KEYS */;
INSERT INTO `position` VALUES
('Аппаратчик по приготовлению химреагентов'),
('Аппаратчик химводоочистки электростанции'),
('Ведущий инженер'),
('Ведущий инженер Группа учета ТЭП'),
('Ведущий инженер группы ИВС'),
('Ведущий инженер группы испытаний измерений метрологии'),
('Ведущий инженер группы РЗА'),
('Ведущий инженер по зданиям и сооружениям'),
('Ведущий инженер по инновациям и энергитической эффективности'),
('Ведущий инженер по охране окружающей среды'),
('Ведущий инженер по ремонту '),
('Ведущий инженер по средствам связи'),
('Ведущий инженер по тепломеханическому оборудованию'),
('Ведущий инженер по эксплуатации'),
('Ведущий инженер по ЭО,КИПиА'),
('Ведущий инженер-программист'),
('Ведущий инженер-технолог'),
('Ведущий инженер-технолог по ремонту'),
('Ведущий инженер-технолог по эксплуатации'),
('Ведущий инженер-электроник группы ФГУ и ТЗ'),
('Ведущий программист группы ПО ИВС'),
('Ведущий специалист'),
('Ведущий специалист группы складской логистики'),
('Ведущий специалист по договорной работе '),
('Ведущий специалист по организации ТОиР и ТПиР'),
('Ведущий специалист по персоналу'),
('Ведущий экономист'),
('Главный инженер'),
('Главный специалист'),
('Главный специалист по антитеррористической защите'),
('Главный специалист по ГО и ЧС'),
('Главный специалист по экономической безопасности'),
('Директор'),
('Директор по безопасности и режиму '),
('Заведующий складом '),
('Заместитель главного инженера по ремонту '),
('Заместитель главного инженера по эксплуатации '),
('Заместитель директора по экономике и снабжению'),
('Заместитель начальника цеха по ремонту'),
('Заместитель начальника цеха по эксплуатации'),
('Изолировщик'),
('Инженер'),
('Инженер -электронник 1 категории Группы ИВС'),
('Инженер 1 категории  Группа ИТ'),
('Инженер 1 категории Группа наладки оборудования'),
('Инженер 1 категории Группы СДТУ'),
('Инженер 2 категории Группы СДТУ'),
('Инженер группы испытаний измерений метрологии'),
('Инженер группы по эксплуатации оборудования'),
('Инженер группы РЗА'),
('Инженер по эксплуатации'),
('Инженер электросвязи Группы СДТУ'),
('Инженер-програмист 1 категории Группы программного обеспечения ИВС'),
('Инженер-химик'),
('Инженер-электроник'),
('Инженер-электроник  группы ФГУ и ТЗ'),
('Инженер-электроник 1 категории '),
('Инженер-электроник 2 категории  Группа ИТ'),
('Инженер-электроник Группы ФГУ и ТЗ'),
('Лаборант химического анализа'),
('Мастер группы  по ремонту электрооборудования в котлотурбинном цехе'),
('Мастер группы электрогазосварки и металлообработки'),
('Мастер по обслуживанию внутренних и водопроводных сетей'),
('Мастер по обслуживанию систем вентиляции и кондиционирования'),
('Мастер по ремонту тепловых сетей'),
('Мастер участка группы КИП и СИ'),
('Мастер участка группы ТЗЭЗиА'),
('Машинист блочной системы управления агрегатами (котел-турбина)'),
('Машинист крана (крановщик)'),
('Машинист энергоблока'),
('Машинист-обходчик турбинного оборудования'),
('Менеджер по персоналу (оплата труда)'),
('Менеджер по персоналу (Оценка и развитие персонала)'),
('Начальник лаборатории'),
('Начальник отдела'),
('Начальник смены станции'),
('Начальник смены цеха'),
('Начальник цеха'),
('Начальник ЭТЛ'),
('Огнеупорщик'),
('Оператор АГРС'),
('Оператор котельной'),
('Программист  группы ПО ИВС'),
('Руководитель направления ИБОКИИ'),
('Руководитель пресс-службы'),
('Слесарь по  обслуживанию систем вентиляции и кондиционирования'),
('Слесарь по обслуживанию тепловых сетей'),
('Слесарь по ремонту грузоподъемных механизмов'),
('Слесарь по ремонту оборудования котельных и пылеприготовительных цехов'),
('Слесарь по ремонту оборудования тепловых сетей'),
('Слесарь по ремонту парогазотурбинного оборудования котлотурбинного цеха'),
('Слесарь сантехник'),
('Специалист'),
('Специалист  по охране труда'),
('Специалист 1 категории'),
('Специалист 1 категории по управлению имуществом'),
('Специалист 2 категории'),
('Специалист по организации ТОиР и ТПиР'),
('Специалист по промышленной безопасности'),
('Старший инспектор по технической эксплуатации'),
('Старший инспектор по эксплуатации'),
('Старший кладовщик '),
('Старший мастер'),
('Старший мастер по ремонту парогазотурбинного оборудования котлотурбинного цеха'),
('Старший машинист котельного оборудования'),
('Старший машинист котлотурбинного цеха'),
('Старший начальник смены электростанции '),
('Старший электромонтер по обслуживанию электрооборудования электростанций (занятый обслуживанием котельного и турбинного оборудов'),
('Стропальщик'),
('Токарь'),
('Экономист 1 категории'),
('Экономист 2 категории'),
('Электрогазосварщик (занятый на резке и ручной сварке)'),
('Электромонтер по обслуживанию электрооборудования электростанций (занятый обслуживанием котельного и турбинного оборудования)'),
('Электромонтер по ремонту аппаратуры релейной защиты'),
('Электросварщик ручной сварки'),
('Электрослесарь по обслуживанию автоматики и средств измерений 7 разряда (занятый обслуживанием котельного и турбинного оборудова'),
('Электрослесарь по ремонту и обслуживанию автоматики и средств измерений электростанции группы КИП и СИ'),
('Электрослесарь по ремонту и обслуживанию автоматики и средств измерений электростанции группы ТЗЭЗиА'),
('Электрослесарь по ремонту электрооборудования электростанций (занятый ремонтом котельного и турбинного оборудования)');
/*!40000 ALTER TABLE `position` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subcategory`
--

DROP TABLE IF EXISTS `subcategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subcategory` (
  `id` tinyint(4) NOT NULL,
  `name` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subcategory`
--

LOCK TABLES `subcategory` WRITE;
/*!40000 ALTER TABLE `subcategory` DISABLE KEYS */;
INSERT INTO `subcategory` VALUES
(0,'-'),
(18,'Средства индивидуальной и коллективной защиты'),
(19,'Нарушения по наряду-допуску, акту-допуску'),
(20,'Станочное оборудование, инструменты, приспособления'),
(21,'Наличие разрешительной и организационной документации'),
(22,'Нарушения при производстве работ ПС и ГЗП'),
(23,'Подъём и транспортировка тяжестей'),
(24,'Санитарно-гигиеническое состояние помещений, рабочих мест'),
(25,'Содержание территории'),
(26,'Организация складского хозяйства'),
(27,'Содержание средств пожаротушения, связи'),
(28,'Содержание противопожарного водоснабжения, ПГ, насосы, завесы'),
(29,'Содержание установок автоматической противопожарной защиты'),
(30,'Хранение ГЖ, ЛВЖ, химреактивов, угольный склад'),
(31,'Огневые работы'),
(32,'Нарушения при эксплуатации ЭУ'),
(33,'Нарушения при эксплуатации оборудования'),
(34,'Нарушения графиков регламентного обслуживания оборудования (ТО, ремонты и т.п.)'),
(35,'Нарушения производственной дисциплины'),
(36,'Нарушения по ведению оперативной документации  и ведению оперативных переговоров'),
(37,'Нарушения порядка работы с персоналом');
/*!40000 ALTER TABLE `subcategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `type`
--

DROP TABLE IF EXISTS `type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `type` (
  `name` varchar(16) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `type`
--

LOCK TABLES `type` WRITE;
/*!40000 ALTER TABLE `type` DISABLE KEYS */;
INSERT INTO `type` VALUES
('Акт ДОТ'),
('Аудит'),
('Обход'),
('ППРМ'),
('Предложение ПЧ'),
('Предписание');
/*!40000 ALTER TABLE `type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` smallint(11) unsigned NOT NULL AUTO_INCREMENT,
  `login` varchar(64) NOT NULL,
  `password` varchar(64) NOT NULL,
  `last_name` varchar(64) DEFAULT NULL,
  `first_name` varchar(64) DEFAULT NULL,
  `middle_name` varchar(64) DEFAULT NULL,
  `department` varchar(16) DEFAULT NULL,
  `position` varchar(128) DEFAULT NULL,
  `created` datetime DEFAULT current_timestamp(),
  `deleted` datetime DEFAULT NULL,
  `access` tinyint(3) unsigned DEFAULT NULL,
  `level` tinyint(4) unsigned DEFAULT NULL,
  `shift` tinyint(4) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `login_UNIQUE` (`login`),
  KEY `user_FK` (`department`),
  KEY `user_FK_1` (`position`),
  CONSTRAINT `user_FK` FOREIGN KEY (`department`) REFERENCES `department` (`name`) ON DELETE SET NULL ON UPDATE SET NULL,
  CONSTRAINT `user_FK_1` FOREIGN KEY (`position`) REFERENCES `position` (`name`) ON DELETE SET NULL ON UPDATE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES
(1,'admin','admin','Фамилия','Имя','Отчество','ЦАСУТП','Ведущий инженер','2023-08-20 03:37:30',NULL,255,3,NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'control'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-11  5:11:35
