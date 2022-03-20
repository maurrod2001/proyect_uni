-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3307
-- Tiempo de generación: 20-03-2022 a las 01:27:36
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `proyect_uni`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiante`
--

CREATE TABLE `estudiante` (
  `Id_estudiante` int(11) NOT NULL,
  `Id_usuario` int(11) NOT NULL,
  `Semestre` varchar(20) NOT NULL,
  `Estado` tinyint(1) DEFAULT NULL,
  `Fecha` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `estudiante`
--

INSERT INTO `estudiante` (`Id_estudiante`, `Id_usuario`, `Semestre`, `Estado`, `Fecha`) VALUES
(1, 1, '6', 1, '2019-03-22'),
(2, 2, '5', 1, '2019-03-22');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grupo`
--

CREATE TABLE `grupo` (
  `Id_grupo` int(11) NOT NULL,
  `Estado` tinyint(1) DEFAULT NULL,
  `Fecha` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grupo_estu`
--

CREATE TABLE `grupo_estu` (
  `Id_grupo_estu` int(11) NOT NULL,
  `Id_grupo` int(11) DEFAULT NULL,
  `Id_estudiante` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `materia`
--

CREATE TABLE `materia` (
  `Id_materia` int(11) NOT NULL,
  `Nombre` varchar(20) NOT NULL,
  `Estado` tinyint(1) DEFAULT NULL,
  `Fecha` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `materia`
--

INSERT INTO `materia` (`Id_materia`, `Nombre`, `Estado`, `Fecha`) VALUES
(1, 'biologia', 1, '2019-03-22'),
(2, 'literatura', 1, '2019-03-22');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `nota`
--

CREATE TABLE `nota` (
  `Id_nota` int(11) NOT NULL,
  `Id_proyecto` int(11) NOT NULL,
  `Nota` float(1,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profesor`
--

CREATE TABLE `profesor` (
  `Id_profesor` int(11) NOT NULL,
  `Id_usuario` int(11) NOT NULL,
  `Facultad` varchar(20) NOT NULL,
  `Estado` tinyint(1) DEFAULT NULL,
  `Fecha` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `profesor`
--

INSERT INTO `profesor` (`Id_profesor`, `Id_usuario`, `Facultad`, `Estado`, `Fecha`) VALUES
(1, 6, 'leyes y derecho', 1, '2019-03-22');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyecto`
--

CREATE TABLE `proyecto` (
  `Id_proyecto` int(11) NOT NULL,
  `Id_grupo` int(11) NOT NULL,
  `Id_materia` int(11) NOT NULL,
  `Nombre` varchar(20) NOT NULL,
  `Estado` tinyint(1) DEFAULT NULL,
  `Fecha` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol`
--

CREATE TABLE `rol` (
  `Id_rol` int(11) NOT NULL,
  `Nombre` varchar(20) NOT NULL,
  `Estado` tinyint(1) DEFAULT NULL,
  `Fecha` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `rol`
--

INSERT INTO `rol` (`Id_rol`, `Nombre`, `Estado`, `Fecha`) VALUES
(1, 'Estudiante', 1, '0000-00-00'),
(2, 'profesor ', 1, '0000-00-00'),
(3, 'admin', 1, '0000-00-00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `Id_usuario` int(11) NOT NULL,
  `Tipo_doc` varchar(20) NOT NULL,
  `Num_doc` int(20) NOT NULL,
  `Nombre` varchar(20) NOT NULL,
  `Apellido` varchar(20) NOT NULL,
  `Id_rol` int(11) NOT NULL,
  `Estado` tinyint(1) DEFAULT NULL,
  `Fecha` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`Id_usuario`, `Tipo_doc`, `Num_doc`, `Nombre`, `Apellido`, `Id_rol`, `Estado`, `Fecha`) VALUES
(1, 'cc', 346789784, 'sam', 'ying', 1, 1, '2019-02-22'),
(2, 'ti', 35455555, 'miriam', 'gonzales', 1, 1, '2019-02-22'),
(6, 'cc', 2248590, 'bryan', 'myers', 2, 1, '2019-02-22'),
(35, 'ctac', 355, 'asdfa', 'goesdgña', 3, 1, '2019-02-22');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `estudiante`
--
ALTER TABLE `estudiante`
  ADD PRIMARY KEY (`Id_estudiante`),
  ADD KEY `Id_usuario` (`Id_usuario`);

--
-- Indices de la tabla `grupo`
--
ALTER TABLE `grupo`
  ADD PRIMARY KEY (`Id_grupo`);

--
-- Indices de la tabla `grupo_estu`
--
ALTER TABLE `grupo_estu`
  ADD PRIMARY KEY (`Id_grupo_estu`),
  ADD KEY `Id_grupo` (`Id_grupo`),
  ADD KEY `Id_estudiante` (`Id_estudiante`);

--
-- Indices de la tabla `materia`
--
ALTER TABLE `materia`
  ADD PRIMARY KEY (`Id_materia`);

--
-- Indices de la tabla `nota`
--
ALTER TABLE `nota`
  ADD PRIMARY KEY (`Id_nota`),
  ADD KEY `Id_proyecto` (`Id_proyecto`);

--
-- Indices de la tabla `profesor`
--
ALTER TABLE `profesor`
  ADD PRIMARY KEY (`Id_profesor`),
  ADD KEY `Id_usuario` (`Id_usuario`);

--
-- Indices de la tabla `proyecto`
--
ALTER TABLE `proyecto`
  ADD PRIMARY KEY (`Id_proyecto`),
  ADD UNIQUE KEY `Nombre` (`Nombre`),
  ADD KEY `Id_grupo` (`Id_grupo`),
  ADD KEY `Id_materia` (`Id_materia`);

--
-- Indices de la tabla `rol`
--
ALTER TABLE `rol`
  ADD PRIMARY KEY (`Id_rol`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`Id_usuario`),
  ADD UNIQUE KEY `Num_doc` (`Num_doc`),
  ADD KEY `Id_rol` (`Id_rol`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `estudiante`
--
ALTER TABLE `estudiante`
  MODIFY `Id_estudiante` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `grupo_estu`
--
ALTER TABLE `grupo_estu`
  MODIFY `Id_grupo_estu` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `materia`
--
ALTER TABLE `materia`
  MODIFY `Id_materia` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `nota`
--
ALTER TABLE `nota`
  MODIFY `Id_nota` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `profesor`
--
ALTER TABLE `profesor`
  MODIFY `Id_profesor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `proyecto`
--
ALTER TABLE `proyecto`
  MODIFY `Id_proyecto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `rol`
--
ALTER TABLE `rol`
  MODIFY `Id_rol` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `Id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1334524;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `estudiante`
--
ALTER TABLE `estudiante`
  ADD CONSTRAINT `estudiante_ibfk_1` FOREIGN KEY (`Id_usuario`) REFERENCES `usuario` (`Id_usuario`);

--
-- Filtros para la tabla `grupo_estu`
--
ALTER TABLE `grupo_estu`
  ADD CONSTRAINT `grupo_estu_ibfk_1` FOREIGN KEY (`Id_grupo`) REFERENCES `grupo` (`Id_grupo`),
  ADD CONSTRAINT `grupo_estu_ibfk_2` FOREIGN KEY (`Id_estudiante`) REFERENCES `estudiante` (`Id_estudiante`);

--
-- Filtros para la tabla `nota`
--
ALTER TABLE `nota`
  ADD CONSTRAINT `nota_ibfk_1` FOREIGN KEY (`Id_proyecto`) REFERENCES `proyecto` (`Id_proyecto`);

--
-- Filtros para la tabla `profesor`
--
ALTER TABLE `profesor`
  ADD CONSTRAINT `profesor_ibfk_1` FOREIGN KEY (`Id_usuario`) REFERENCES `usuario` (`Id_usuario`);

--
-- Filtros para la tabla `proyecto`
--
ALTER TABLE `proyecto`
  ADD CONSTRAINT `proyecto_ibfk_1` FOREIGN KEY (`Id_grupo`) REFERENCES `grupo` (`Id_grupo`),
  ADD CONSTRAINT `proyecto_ibfk_2` FOREIGN KEY (`Id_materia`) REFERENCES `materia` (`Id_materia`);

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`Id_rol`) REFERENCES `rol` (`Id_rol`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
