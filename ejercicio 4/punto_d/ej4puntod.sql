-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 22-03-2019 a las 04:21:02
-- Versión del servidor: 10.1.26-MariaDB
-- Versión de PHP: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ej4puntod`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tabla_prueba`
--

CREATE TABLE `tabla_prueba` (
  `id_tabla` smallint(2) NOT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `apellido` varchar(255) DEFAULT NULL,
  `correo` varchar(255) DEFAULT NULL,
  `celular` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tabla_prueba`
--

INSERT INTO `tabla_prueba` (`id_tabla`, `nombre`, `apellido`, `correo`, `celular`) VALUES
(1, 'daniel', 'cardozo', 'daniel@hotmail.com', '3219807444');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tabla_prueba`
--
ALTER TABLE `tabla_prueba`
  ADD PRIMARY KEY (`id_tabla`),
  ADD UNIQUE KEY `id_tabla` (`id_tabla`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tabla_prueba`
--
ALTER TABLE `tabla_prueba`
  MODIFY `id_tabla` smallint(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
