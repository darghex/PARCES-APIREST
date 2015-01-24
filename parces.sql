CREATE DATABASE  IF NOT EXISTS `parces` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `parces`;
-- MySQL dump 10.13  Distrib 5.5.31, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: parces
-- ------------------------------------------------------
-- Server version	5.5.31-0+wheezy1

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
-- Table structure for table `asistencias`
--

DROP TABLE IF EXISTS `asistencias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `asistencias` (
  `instancias_curso_id` bigint(20) unsigned NOT NULL COMMENT 'Llave foránea  la tabla instancias_curso',
  `estudiante` char(7) NOT NULL COMMENT 'Codigo de Estudiante. Hace referencia  al estudiante registrado en la plataforma RYCA. El codigo esta compuesto por 7 caracteres',
  `tutor` int(10) unsigned zerofill NOT NULL COMMENT 'Codigo del profesor con rol de tutor. Hace referencia  al profesor registrado en la plataforma RYCA.',
  `asistencia` tinyint(1) NOT NULL COMMENT 'Indica si el estudiante asistio (True)  o no (False)  a clase',
  KEY `estudiante` (`estudiante`,`tutor`),
  KEY `instancias_curso_id` (`instancias_curso_id`),
  CONSTRAINT `asistencias_ibfk_1` FOREIGN KEY (`estudiante`, `tutor`) REFERENCES `asignaciones` (`estudiante`, `tutor`),
  CONSTRAINT `asistencias_ibfk_2` FOREIGN KEY (`instancias_curso_id`) REFERENCES `instancias_curso` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Registra la asistencia a clase de cada estudiante en un curs';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asistencias`
--

LOCK TABLES `asistencias` WRITE;
/*!40000 ALTER TABLE `asistencias` DISABLE KEYS */;
/*!40000 ALTER TABLE `asistencias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `calificaciones`
--

DROP TABLE IF EXISTS `calificaciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `calificaciones` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Llave primaria de la tabla',
  `actividades_id` bigint(20) unsigned NOT NULL COMMENT 'LLave foranea de la tabla actividades',
  `estudiante` char(7) NOT NULL COMMENT 'Codigo de Estudiante. Hace referencia  al estudiante registrado en la plataforma RYCA. El codigo esta compuesto por 7 caracteres',
  `tutor` int(10) unsigned zerofill NOT NULL COMMENT 'Codigo del profesor con rol de tutor. Hace referencia  al profesor registrado en la plataforma RYCA.',
  `valor` float(1,1) unsigned NOT NULL COMMENT 'Calificacion obtenida respecto a la actividad según la plataforma RYCA esta se encuentra entre 0.0 y 5.0',
  PRIMARY KEY (`id`),
  KEY `actividades_id` (`actividades_id`),
  KEY `estudiante` (`estudiante`,`tutor`),
  CONSTRAINT `calificaciones_ibfk_1` FOREIGN KEY (`actividades_id`) REFERENCES `actividades` (`id`),
  CONSTRAINT `calificaciones_ibfk_2` FOREIGN KEY (`estudiante`, `tutor`) REFERENCES `asignaciones` (`estudiante`, `tutor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Almacena las calificaciones por cada actividad del estudiant';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `calificaciones`
--

LOCK TABLES `calificaciones` WRITE;
/*!40000 ALTER TABLE `calificaciones` DISABLE KEYS */;
/*!40000 ALTER TABLE `calificaciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `instancias_curso`
--

DROP TABLE IF EXISTS `instancias_curso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `instancias_curso` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Llave primaria autoincrementable de la tabla',
  `tema` char(50) NOT NULL COMMENT 'Define el nombre del tema que se dará en cada clase. Ejemplo para el el curso de Matematicas Fundamentales: Casos de Factorización',
  `corte` tinyint(3) unsigned DEFAULT NULL COMMENT 'Segmento de tiempo en el que la Universidad establece como se fragmenta un periodo académico para entregar calificaciones. Por ejemplo una Universidad que trabaje por semestres puede establecer 3 parciales para sus calificaciones (3 cortes como es el caso',
  `fecha` datetime NOT NULL COMMENT 'Fecha y hora en la que se orienta el curso',
  `curso` int(11) NOT NULL COMMENT 'codigo del curso asignado por el profesor tomado de la plataforma RYCA',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COMMENT='Almacena cada clase registrada por un usuario. Una Instancia';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `instancias_curso`
--

LOCK TABLES `instancias_curso` WRITE;
/*!40000 ALTER TABLE `instancias_curso` DISABLE KEYS */;
INSERT INTO `instancias_curso` VALUES (1,'ARBOLES BINARIOS',1,'0000-00-00 00:00:00',1),(3,'Estructuras no lineales',1,'0000-00-00 00:00:00',1),(4,'Estructuras lineales FIFO',1,'0000-00-00 00:00:00',1),(5,'Estructuras lineales FIFO',1,'0000-00-00 00:00:00',1),(6,'Estructuras lineales FIFO',1,'0000-00-00 00:00:00',1);
/*!40000 ALTER TABLE `instancias_curso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `actividades`
--

DROP TABLE IF EXISTS `actividades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `actividades` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT 'LLave primaria de la tabla',
  `instancias_curso_id` bigint(20) unsigned NOT NULL COMMENT 'Llave foránea  la tabla instancias_curso',
  `descripcion` varchar(50) NOT NULL COMMENT 'Nombre de la actividad',
  PRIMARY KEY (`id`),
  KEY `instancias_curso_id` (`instancias_curso_id`),
  CONSTRAINT `actividades_ibfk_1` FOREIGN KEY (`instancias_curso_id`) REFERENCES `instancias_curso` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Menciona cada una de las actividades académicas de cada clas';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `actividades`
--

LOCK TABLES `actividades` WRITE;
/*!40000 ALTER TABLE `actividades` DISABLE KEYS */;
/*!40000 ALTER TABLE `actividades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comentarios_propuesta`
--

DROP TABLE IF EXISTS `comentarios_propuesta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comentarios_propuesta` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'llave primaria de la tabla',
  `propuestas_matricula_id` int(10) unsigned NOT NULL COMMENT 'Relaciona el identificador de la propuesta de matricula almacenada en la plataforma RYCA',
  `mensaje` tinyblob NOT NULL COMMENT 'Comentario escrito por el estudiante o tutor respecto a la nota obtenida',
  `autor` varchar(100) NOT NULL COMMENT 'Indica el nombre de la persona que escribio el mensaje bien puede ser el estudiante o tutor',
  `fecha` date DEFAULT NULL COMMENT 'fecha en que se escribio el mensaje',
  PRIMARY KEY (`id`),
  KEY `propuestas_matricula_id` (`propuestas_matricula_id`),
  CONSTRAINT `comentarios_propuesta_ibfk_1` FOREIGN KEY (`propuestas_matricula_id`) REFERENCES `propuestas_matricula` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Relaciona los comentarios entre el tutor y estudiante respec';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comentarios_propuesta`
--

LOCK TABLES `comentarios_propuesta` WRITE;
/*!40000 ALTER TABLE `comentarios_propuesta` DISABLE KEYS */;
/*!40000 ALTER TABLE `comentarios_propuesta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `remisiones`
--

DROP TABLE IF EXISTS `remisiones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `remisiones` (
  `estudiante` char(7) NOT NULL COMMENT 'Codigo de Estudiante. Hace referencia  al estudiante registrado en la plataforma RYCA. El codigo esta compuesto por 7 caracteres',
  `tutor` int(10) unsigned zerofill NOT NULL COMMENT 'Codigo del profesor con rol de tutor. Hace referencia  al profesor registrado en la plataforma RYCA.',
  `servicios_bienestar_id` tinyint(4) NOT NULL COMMENT 'llave foranea de la tabla servicios_bienestar',
  `motivo` tinyblob NOT NULL COMMENT 'Indicar el motivo remite a un estudiante al servicio  de bienestar escogido',
  `fecha` date NOT NULL COMMENT 'Fecha de la remisión',
  KEY `estudiante` (`estudiante`,`tutor`),
  KEY `servicios_bienestar_id` (`servicios_bienestar_id`),
  CONSTRAINT `remisiones_ibfk_1` FOREIGN KEY (`estudiante`, `tutor`) REFERENCES `asignaciones` (`estudiante`, `tutor`),
  CONSTRAINT `remisiones_ibfk_2` FOREIGN KEY (`servicios_bienestar_id`) REFERENCES `servicios_bienestar` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Almacena las remision hecha por el tutor al estudiante para ';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `remisiones`
--

LOCK TABLES `remisiones` WRITE;
/*!40000 ALTER TABLE `remisiones` DISABLE KEYS */;
/*!40000 ALTER TABLE `remisiones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `propuestas_matricula`
--

DROP TABLE IF EXISTS `propuestas_matricula`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `propuestas_matricula` (
  `id` int(10) unsigned NOT NULL COMMENT 'Relaciona el identificador de la propuesta de matricula almacenada en la plataforma RYCA',
  `estudiante` char(7) NOT NULL COMMENT 'Codigo de Estudiante. Hace referencia  al estudiante registrado en la plataforma RYCA. El codigo esta compuesto por 7 caracteres',
  `tutor` int(10) unsigned zerofill NOT NULL COMMENT 'Codigo del profesor con rol de tutor. Hace referencia  al profesor registrado en la plataforma RYCA.',
  `estado` tinyint(1) NOT NULL COMMENT 'indica el estado de la propuesta de matricula (aprobado = True, desaprobado = False)',
  PRIMARY KEY (`id`),
  KEY `estudiante` (`estudiante`,`tutor`),
  CONSTRAINT `propuestas_matricula_ibfk_1` FOREIGN KEY (`estudiante`, `tutor`) REFERENCES `asignaciones` (`estudiante`, `tutor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Almacena el estado de la propuestas de matricula realizada e';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `propuestas_matricula`
--

LOCK TABLES `propuestas_matricula` WRITE;
/*!40000 ALTER TABLE `propuestas_matricula` DISABLE KEYS */;
/*!40000 ALTER TABLE `propuestas_matricula` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comentarios_calificacion`
--

DROP TABLE IF EXISTS `comentarios_calificacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comentarios_calificacion` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'llave primaria de la tabla',
  `calificaciones_id` bigint(20) unsigned NOT NULL COMMENT 'Llave foránea de la tabla calificaciones',
  `mensaje` tinyblob NOT NULL COMMENT 'Comentario escrito por el estudiante o tutor respecto a la nota obtenida',
  `autor` varchar(100) NOT NULL COMMENT 'Indica el nombre de la persona que escribio el mensaje bien puede ser el estudiante o tutor',
  `fecha` date DEFAULT NULL COMMENT 'fecha en que se escribio el mensaje',
  PRIMARY KEY (`id`),
  KEY `calificaciones_id` (`calificaciones_id`),
  CONSTRAINT `comentarios_calificacion_ibfk_1` FOREIGN KEY (`calificaciones_id`) REFERENCES `calificaciones` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Relaciona los comentarios entre el tutor y estudiante respec';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comentarios_calificacion`
--

LOCK TABLES `comentarios_calificacion` WRITE;
/*!40000 ALTER TABLE `comentarios_calificacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `comentarios_calificacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servicios_bienestar`
--

DROP TABLE IF EXISTS `servicios_bienestar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `servicios_bienestar` (
  `id` tinyint(4) NOT NULL AUTO_INCREMENT COMMENT 'llave primaria de la tabla',
  `servicio` varchar(30) NOT NULL COMMENT 'Nombre del servicio ofrecido por Bienestar Universitario',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Registra los servicios que ofrece bienestar unviersitario';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicios_bienestar`
--

LOCK TABLES `servicios_bienestar` WRITE;
/*!40000 ALTER TABLE `servicios_bienestar` DISABLE KEYS */;
/*!40000 ALTER TABLE `servicios_bienestar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `asignaciones`
--

DROP TABLE IF EXISTS `asignaciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `asignaciones` (
  `estudiante` char(7) NOT NULL COMMENT 'Codigo de Estudiante. Hace referencia  al estudiante registrado en la plataforma RYCA. El codigo esta compuesto por 7 caracteres',
  `tutor` int(10) unsigned NOT NULL COMMENT 'Codigo del profesor con rol de tutor. Hace referencia  al profesor registrado en la plataforma RYCA.',
  `fecha` date NOT NULL COMMENT 'Registra la ficha en que se relaciono la tutoria',
  PRIMARY KEY (`estudiante`,`tutor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='relaciona caules tutores tienen a cargo cuales estudiantes';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asignaciones`
--

LOCK TABLES `asignaciones` WRITE;
/*!40000 ALTER TABLE `asignaciones` DISABLE KEYS */;
INSERT INTO `asignaciones` VALUES ('3710214',1633,'2014-11-23'),('3710314',1633,'2014-11-25'),('3710614',1633,'2014-11-23');
/*!40000 ALTER TABLE `asignaciones` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-11-24  9:37:59
