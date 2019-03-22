-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 22-03-2019 a las 04:19:32
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
-- Base de datos: `chatmulticliente`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mensajes`
--

CREATE TABLE `mensajes` (
  `Codigo` int(6) NOT NULL COMMENT 'Identificador único de cada registro',
  `texto` varchar(255) NOT NULL COMMENT 'mensaje almacenado',
  `fecha_enviado` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'fecha de envío',
  `emisor_usuario` varchar(255) NOT NULL COMMENT 'emisor del mensaje',
  `remitente_usuario` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='se almacenan mensajes de los usuarios';

--
-- Volcado de datos para la tabla `mensajes`
--

INSERT INTO `mensajes` (`Codigo`, `texto`, `fecha_enviado`, `emisor_usuario`, `remitente_usuario`) VALUES
(12, '\'hola\'', '2019-03-18 14:29:38', 'daniel', 'daniel'),
(13, '\'hola\'', '2019-03-18 14:30:00', 'danie', 'daniel'),
(14, '\'hola\'', '2019-03-18 14:30:00', 'danie', 'danie'),
(15, '\'holaa\'', '2019-03-18 14:30:22', 'luis', 'daniel'),
(16, '\'holaa\'', '2019-03-18 14:30:22', 'luis', 'danie'),
(17, '\'holaa\'', '2019-03-18 14:30:22', 'luis', 'luis'),
(18, '\'volvi\'', '2019-03-19 02:39:42', 'danie', 'danie');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `codigo` int(4) NOT NULL,
  `usuario` varchar(255) NOT NULL,
  `fecha_ingreso` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`codigo`, `usuario`, `fecha_ingreso`) VALUES
(6, 'daniel', '2019-03-20 04:00:39'),
(8, 'danie', '2019-03-19 02:40:08'),
(9, 'luis', '2019-03-18 14:31:26'),
(10, '{salir}', '2019-03-19 03:12:20'),
(11, '', '2019-03-19 01:44:40');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `mensajes`
--
ALTER TABLE `mensajes`
  ADD PRIMARY KEY (`Codigo`),
  ADD KEY `fk_codigo_usuario` (`emisor_usuario`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`codigo`),
  ADD UNIQUE KEY `usuario` (`usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `mensajes`
--
ALTER TABLE `mensajes`
  MODIFY `Codigo` int(6) NOT NULL AUTO_INCREMENT COMMENT 'Identificador único de cada registro', AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `codigo` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
