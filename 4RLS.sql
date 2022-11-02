-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 02, 2022 at 08:20 AM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `4RLS`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `user_id` int(50) NOT NULL,
  `fname` text NOT NULL,
  `lname` text NOT NULL,
  `surname` text NOT NULL,
  `email` varchar(20) NOT NULL,
  `phone` varchar(200) NOT NULL,
  `status` text NOT NULL DEFAULT 'inactive',
  `password` varchar(200) NOT NULL,
  `gender` text NOT NULL,
  `role` tinytext NOT NULL,
  `reg_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `otp` varchar(100) DEFAULT NULL,
  `otptime` varchar(50) NOT NULL DEFAULT '0',
  `prof_pic` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`user_id`, `fname`, `lname`, `surname`, `email`, `phone`, `status`, `password`, `gender`, `role`, `reg_date`, `otp`, `otptime`, `prof_pic`) VALUES
(1, 'Qaz', 'Qhaz', 'Qaza', 'email@gmail.com', 'gAAAAABjIY4JInrU9a2hOrdMZul8p6L_KgwqAbywpIOpDgv-j3dxWecD9t48y8pD1uErP4uK4OW90ljWj-n338aKTcCGx8QkKA==', 'active', '$2b$12$GcEMIU8inJS5UMbazI9MUOKgZDK6ubmnF4RFPn4OtpxU8e3smq17q', 'Male', 'admin', '2022-10-17 12:12:26', '$2b$12$rUX03niVMTVV3e7I0p28/.oYQDZ3l/TRgxhKQc.Tutr7d8/nA0DRa', '2022-10-17 15:12:26.374589', 'admin1.jpeg'),
(3, 'Jessie', 'Shades', 'Wattson', 'jshades@gmail.com', 'gAAAAABjIYbnFiP8PfdjsVSVr-2-tC-gICjYREviWzPDUlcGOkTKYT88h4MALhVsAEtewlA5KEL4ZM6cXF-L0BVE4gkuzwLCuQ==', 'active', '$2b$12$ZKLNtq2Td3H6m.N2ZxgFOeNiC5n1vhYfvrV.hYoAC.JvlsnCNBxFi', 'Female', 'admin', '2022-11-02 06:35:03', '$2b$12$1N96zcLvdTrZWdu8Z.2VMe7KkfzxOa4u2387Jm32LWlWB098XzCDm', '2022-11-02 09:35:02.768072', 'admin2.jpeg'),
(4, 'Caesear', 'Julius', 'Bandana', 'bandana@gmail.com', 'gAAAAABjIYbnFiP8PfdjsVSVr-2-tC-gICjYREviWzPDUlcGOkTKYT88h4MALhVsAEtewlA5KEL4ZM6cXF-L0BVE4gkuzwLCuQ==', 'active', '$2b$12$GcEMIU8inJS5UMbazI9MUOKgZDK6ubmnF4RFPn4OtpxU8e3smq17q', 'Male', 'operations', '2022-10-03 06:52:04', '$2b$12$k5NcSGIMR/a4mMnRYhpTvO0AIcFqGfYKYRlGuy4iz3JEKed/WMgc2', '2022-09-27 11:57:40.187380', NULL),
(5, 'etgwtg', 'etew', 'ewt', 'werr@gmail.com', 'gAAAAABjNW_kfAevkgRxV8cd_svkKmWEa_c_Vlu3of9OEkfYHrtpkMnr6l_YgLfMXavIz-yto0aAOn-Q91cJvkJAo6po5pieyQ==', 'inactive', '$2b$12$xQjF2hDU8dPLLOMpEPokGuZ0cIKdoDa7iKw8GHZHg6azsDI3aD8d2', 'Male', 'guest', '2022-10-03 06:51:53', NULL, '0', NULL),
(6, 'Jimmy', 'Not', 'Ferr', 'jnf@gmail.com', 'gAAAAABjIYbnFiP8PfdjsVSVr-2-tC-gICjYREviWzPDUlcGOkTKYT88h4MALhVsAEtewlA5KEL4ZM6cXF-L0BVE4gkuzwLCuQ==', 'active', '$2b$12$GcEMIU8inJS5UMbazI9MUOKgZDK6ubmnF4RFPn4OtpxU8e3smq17q', 'Male', 'operations', '2022-10-12 08:01:07', '$2b$12$MBU76AddexTK683QP1x2B.ll21A1bNhThBK25VjmzcklZqb5vedzS', '2022-10-12 11:01:07.068960', NULL),
(7, 'Sage', 'Fears', '', 'fears@gmail.com', 'gAAAAABjT7DXlNriNfdUwnb3xBp3_1EhKyl061PuKb3AzUly2WLZfyTqh2otIvsasr83gwFpsO5IRo3MFvgxQywTGgYGZV898Q==', 'inactive', '$2b$12$kWfQa1O5GVX5/VXKJlXVF.fXbbozVVbPt05bvICDaeq5gQ6JipdyO', 'Female', 'admin', '2022-10-19 08:09:59', NULL, '0', NULL),
(8, 'Reeds', 'Laverte', '', 'reeds@gmail.com', 'gAAAAABjIYbnFiP8PfdjsVSVr-2-tC-gICjYREviWzPDUlcGOkTKYT88h4MALhVsAEtewlA5KEL4ZM6cXF-L0BVE4gkuzwLCuQ==', 'active', '$2b$12$/dY3bSpOX6P/BF4kRG9olus3gYQWzrjCRoJBkn8ozHIRP3O7pacfO', 'Male', 'mechanics', '2022-10-26 07:48:38', NULL, '0', NULL),
(9, 'Wattsy', 'David', '', 'wdavid@gmail.com', 'gAAAAABjT7FMwu6aon25PsFEVDLYSxw1GlaremyQdT3QJ5hwfiFjXVMwDz089u0JUpSfFXGbgyR83FZOMP3Ps4EGmaMa78pB6Q==', 'inactive', '$2b$12$mA6NnX2ECynVB.r74PCoO.DKvzabayeHjLHY2/7543aaACYoAleEe', 'Male', 'operations', '2022-10-19 08:11:56', NULL, '0', NULL),
(10, 'Mech', 'Two', '', 'mech@gmail.com', 'gAAAAABjWOcesDytgEnbPVsncVqt17BzT0StAcEVT3aLVfrLCMkWb1v2y0ihuG8sQQ-PVoH3ynbk1K9zXQojZOX4uyhi9l07pQ==', 'active', '$2b$12$PMu.9/6W7dQQsdVHXTvRVOqZYUrCbhlF7l0TCQqbH5exMn5QbXbt2', 'Male', 'mechanics', '2022-10-26 07:58:31', '$2b$12$eKJg2UjIQz8ej55A3gKn7.wpjmyV3oUJFzSS9Z3SdPJEzriqtczpe', '2022-10-26 10:53:26.465799', 'mech.jpeg'),
(11, 'Mech', 'Mech', '', 'mech2@gmail.com', 'gAAAAABjX51PS_4HLE9rKKrShWD1pOS_rvUQ5cVZskQjittf3cFrPdBZefZ02WiJga0JbPMIcAjAcBioz0dznwKGgsp-CduNXQ==', 'active', '$2b$12$1IFHRJ4W8EkDtpezIz1ifefxyMMpOJ4tZoKV.X0.aUpcMt90TxqFe', 'Male', 'mechanics', '2022-11-01 12:45:04', '$2b$12$56q7nl8IE7Zb/fxw08jHyuUFIZJE7V8BXiuq6FIG8WNDoAu1mu.Ly', '2022-11-01 15:45:04.054658', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `capacity`
--

CREATE TABLE `capacity` (
  `capacity_id` int(50) NOT NULL,
  `capacity_code` int(50) NOT NULL,
  `reg_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `capacity`
--

INSERT INTO `capacity` (`capacity_id`, `capacity_code`, `reg_date`) VALUES
(1, 1000, '2022-10-06 10:26:00'),
(2, 5500, '2022-10-06 10:26:00');

-- --------------------------------------------------------

--
-- Table structure for table `contracts`
--

CREATE TABLE `contracts` (
  `con_id` int(50) NOT NULL,
  `con_name` tinytext NOT NULL,
  `reg_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contracts`
--

INSERT INTO `contracts` (`con_id`, `con_name`, `reg_date`) VALUES
(1, 'DRiver 1', '2022-10-05 12:18:46');

-- --------------------------------------------------------

--
-- Table structure for table `drivers`
--

CREATE TABLE `drivers` (
  `driver_id` int(50) NOT NULL,
  `fname` tinytext NOT NULL,
  `surname` tinytext DEFAULT NULL,
  `lname` tinytext NOT NULL,
  `phone` varchar(100) NOT NULL,
  `email` varchar(50) NOT NULL,
  `dl_no` varchar(50) NOT NULL,
  `dl_no_expiry` date NOT NULL,
  `passport_pic` varchar(255) NOT NULL,
  `loc_id` int(50) NOT NULL,
  `dob` date NOT NULL,
  `con_id` int(50) DEFAULT NULL,
  `password` varchar(200) NOT NULL,
  `user_id` int(50) NOT NULL,
  `status` text NOT NULL DEFAULT 'Not allocated'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `drivers`
--

INSERT INTO `drivers` (`driver_id`, `fname`, `surname`, `lname`, `phone`, `email`, `dl_no`, `dl_no_expiry`, `passport_pic`, `loc_id`, `dob`, `con_id`, `password`, `user_id`, `status`) VALUES
(1, 'Huges', 'Bna', 'Bandana', 'gAAAAABjPXuZ-qdBxYpZ2ywhbiOx5Wem3EnZht9rFOV2ybmwIwrpTUk4nY_u_d8XhcDe7_dlPJtaX6L51b3TeTPJ5WNB-iR-Lw==', 'bandanahug@gmail.com', '8989', '2022-10-20', '6UV3T0wallpaperbetter_30.jpg', 3, '2022-09-26', 1, '$2b$12$MqItcF6MPvYgnHkxsss7sulC3YsjJPUQmqD0V7s4cKvfhMBLnVbjO', 3, 'Not allocated'),
(10, 'Marvin', 'Keith', 'Ogola', 'gAAAAABjT6RqoG-NZ_-xJK1y38wXjDzk4poXcaFgsman5QdSOn08XBojM5C5hee_eAYhsWHrWXOEKu1kNgtrl3x80bKwXdOL-Q==', 'mogola@gmail.com', '123456', '2022-10-29', 'ZFDJQIdownload.jpeg', 4, '2022-10-06', 1, '$2b$12$IXQ9a/K/LkfOAfabdhguGuL724zY1yUciQerDDS.dTEN7VBYTtZSG', 3, 'Allocated'),
(12, 'Raz', '', 'Raza', 'gAAAAABjT7I3ZYXkZiuQy8b0CuAkjhddN3uqPXCQJGPhcNmu3hnTS5aZglKBhHpzEmavGutpbiCj4PCigfIXsRB3raZLYgSlqA==', 'raz@gmail.com', '156465', '2022-10-29', 'DFMI6Kwallpaperbetter_27.jpg', 5, '2022-10-06', 1, '$2b$12$VOH0Dyzy7kiKPj57ZMBIZ.Dm0OrS7bfvBsqtAkHxHpB5X2ieuCsRi', 3, 'Not allocated');

-- --------------------------------------------------------

--
-- Table structure for table `driver_allocations`
--

CREATE TABLE `driver_allocations` (
  `alloc_id` int(50) NOT NULL,
  `driver_id` int(50) NOT NULL,
  `reg_no` varchar(50) NOT NULL,
  `alloc_status` varchar(50) NOT NULL DEFAULT 'active',
  `reg_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `driver_allocations`
--

INSERT INTO `driver_allocations` (`alloc_id`, `driver_id`, `reg_no`, `alloc_status`, `reg_date`) VALUES
(3, 10, 'KGS 45P', 'inactive', '2022-10-24 10:34:58'),
(4, 1, 'KCE 124P', 'inactive', '2022-10-24 10:35:13'),
(5, 10, 'KCE 124P', 'active', '2022-10-24 10:35:34');

-- --------------------------------------------------------

--
-- Table structure for table `locations`
--

CREATE TABLE `locations` (
  `loc_id` int(50) NOT NULL,
  `loc_name` text NOT NULL,
  `reg_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `locations`
--

INSERT INTO `locations` (`loc_id`, `loc_name`, `reg_date`) VALUES
(1, 'Westlands', '2022-09-28 08:02:19'),
(2, 'Thika', '2022-09-28 08:25:08'),
(3, 'Githurai', '2022-09-28 08:25:21'),
(4, 'Donholm', '2022-09-28 09:58:11'),
(5, 'Jacaranda', '2022-10-19 08:14:28');

-- --------------------------------------------------------

--
-- Table structure for table `owners`
--

CREATE TABLE `owners` (
  `owner_id` int(50) NOT NULL,
  `fname` tinytext NOT NULL,
  `surname` tinytext DEFAULT NULL,
  `lname` tinytext NOT NULL,
  `phone` varchar(100) NOT NULL,
  `email` varchar(50) NOT NULL,
  `address` varchar(100) NOT NULL,
  `loc_id` int(50) NOT NULL,
  `passport_pic` varchar(500) DEFAULT NULL,
  `id_no` varchar(50) NOT NULL,
  `dob` date NOT NULL,
  `reg_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `user_id` int(50) NOT NULL,
  `password` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `owners`
--

INSERT INTO `owners` (`owner_id`, `fname`, `surname`, `lname`, `phone`, `email`, `address`, `loc_id`, `passport_pic`, `id_no`, `dob`, `reg_date`, `user_id`, `password`) VALUES
(10, 'Mona', 'Liza', 'Lisa', 'gAAAAABjPCd4YKrObOwAWTfcAMUzELjZgNPxjH_FuI7I3PoFiTqiRYt9Nfz7FpO5gjtDKL6aHhPg7OUnf1moRicuqht3LsUTyg==', 'monalisa@gmail.com', '1234 Haveniuer', 4, '6UV3T0wallpaperbetter_30.jpg', '200', '2022-10-06', '2022-10-12 06:43:34', 1, '$2b$12$Kb137IXVwnMhlyz./vd2vO5oYozJr5OS93g7XdjQHI67D2.I6l3fC'),
(11, 'Monal', 'Liza', 'Lisa', 'gAAAAABjPCgusv1PLEC86kerDgKKYHLjFhKiNK4lPyEPaABwA9lvrFt9gir3jOtr-yWhmuL7v8sqMgraKZQiXfpnzDXFFDgG1A==', 'monalisa@gmail.com', '1234 Haveniuer', 4, '6UV3T0wallpaperbetter_30.jpg', '300', '2022-10-06', '2022-10-12 06:43:31', 1, '$2b$12$YsDG06TBbNZcsr1lJbt5zOzKx1wVWE7tQGc1rl432p4R5dRYaXX1G'),
(12, 'Monal', 'Liza', 'Lisa', 'gAAAAABjPCkuggDiCur_p3d4mzTG9c61E-UB3oH69_J4F_qO7sO8NGu5X78Ek1QF9DGj-53pZ0oB22SkqaOWcAdExT03iikFkg==', 'monalisa@gmail.com', '1234 Haveniuer', 4, '6UV3T0wallpaperbetter_30.jpg', '410', '2022-10-06', '2022-10-12 06:43:27', 1, '$2b$12$sUFZRtFFNp776F4HwjgiHObpKYJ.1vJn2naItQS8JsSCgdDuLJ1VS'),
(13, 'Far', '6', 'Cry', 'gAAAAABjPWvizwzrIFuKdvFIlCNLJ1hXFMO9E5MnO1UQjwsvWT1Qyox78sIEUEiAHtTKI_aA9MupCGcNjN7b-cSKXb0xkb-i3w==', 'farcry6@gmail.com', '34 Cry Street', 4, '6UV3T0wallpaperbetter_30.jpg', '789', '0008-12-07', '2022-10-05 11:34:58', 3, '$2b$12$3HFjX9O2mZ09M3eE28BrPOI0Qi4fvAPe6tWZ6BJiW0Qp0rhItl9li');

-- --------------------------------------------------------

--
-- Table structure for table `processed`
--

CREATE TABLE `processed` (
  `process_id` int(50) NOT NULL,
  `service_id` int(50) NOT NULL,
  `reg_no` varchar(50) NOT NULL,
  `services` varchar(200) NOT NULL,
  `reg_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `processed`
--

INSERT INTO `processed` (`process_id`, `service_id`, `reg_no`, `services`, `reg_date`) VALUES
(4, 7, 'KCE 124P', '[\'Fuel filter-5000\', \'Air filter-2000\', \'Oil filter-6000\']', '2022-11-01 12:49:43');

-- --------------------------------------------------------

--
-- Table structure for table `vehicles`
--

CREATE TABLE `vehicles` (
  `reg_no` varchar(50) NOT NULL,
  `type_id` int(50) NOT NULL,
  `make_id` int(50) NOT NULL,
  `model_id` int(50) NOT NULL,
  `capacity_id` int(50) NOT NULL,
  `color` tinytext NOT NULL,
  `weight` varchar(50) NOT NULL,
  `no_of_pass` int(50) DEFAULT NULL,
  `vehicle_pic` varchar(255) NOT NULL,
  `yom` text NOT NULL,
  `owner_id` int(50) NOT NULL,
  `chassis_no` varchar(50) NOT NULL,
  `reg_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `user_id` int(50) NOT NULL,
  `status` text NOT NULL DEFAULT 'Not allocated'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vehicles`
--

INSERT INTO `vehicles` (`reg_no`, `type_id`, `make_id`, `model_id`, `capacity_id`, `color`, `weight`, `no_of_pass`, `vehicle_pic`, `yom`, `owner_id`, `chassis_no`, `reg_date`, `user_id`, `status`) VALUES
('KBA 123P', 4, 13, 1, 2, 'Black', '1230', 5, 'GXDSRIwallpaperbetter_32.jpg', '2022-10-03', 10, '200', '2022-10-11 09:45:05', 0, 'Not allocated'),
('KCE 124P', 4, 12, 1, 1, 'Black', '3000', 5, 'B3VTWRwallpaperbetter_39.jpg', '2022-09-30', 13, '220', '2022-10-24 10:35:34', 0, 'Allocated'),
('KDE 778O', 4, 11, 3, 1, 'Red', '2000', 4, 'N69QOEwallpaperbetter_46.jpg', '2000', 12, '5000', '2022-10-13 12:31:29', 3, 'Not allocated'),
('KGS 456P', 1, 11, 3, 1, 'Blue', '2000', 8, 'D0658Gwallpaperbetter_39.jpg', '2000', 10, '2000', '2022-10-13 12:14:19', 3, 'Not allocated'),
('KGS 45P', 1, 11, 3, 1, 'Blue', '2000', 8, 'EOACWTwallpaperbetter_39.jpg', '2000', 10, '2000', '2022-10-24 10:34:58', 3, 'Not allocated');

-- --------------------------------------------------------

--
-- Table structure for table `vehicle_make`
--

CREATE TABLE `vehicle_make` (
  `make_id` int(50) NOT NULL,
  `make_name` tinytext NOT NULL,
  `reg_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vehicle_make`
--

INSERT INTO `vehicle_make` (`make_id`, `make_name`, `reg_date`) VALUES
(1, 'Mercedes', '2022-09-28 07:27:26'),
(4, 'Toyota', '2022-09-28 07:30:51'),
(5, 'Renault', '2022-09-28 07:31:09'),
(6, 'Nissan', '2022-09-28 07:31:48'),
(7, 'MAN', '2022-09-28 07:32:50'),
(8, 'Scania', '2022-09-28 07:46:07'),
(11, 'Ferrari', '2022-09-28 09:19:06'),
(12, 'BMW', '2022-09-28 09:32:30'),
(13, 'Ford', '2022-10-03 10:15:32'),
(14, 'Porsche', '2022-10-19 08:13:01');

-- --------------------------------------------------------

--
-- Table structure for table `vehicle_model`
--

CREATE TABLE `vehicle_model` (
  `model_id` int(50) NOT NULL,
  `make_id` int(50) NOT NULL,
  `model_name` tinytext NOT NULL,
  `reg_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vehicle_model`
--

INSERT INTO `vehicle_model` (`model_id`, `make_id`, `model_name`, `reg_date`) VALUES
(1, 12, 'x5', '2022-09-28 09:57:09'),
(2, 12, 'X3', '2022-09-29 09:13:31'),
(3, 11, 'FFX', '2022-10-06 11:05:32'),
(4, 4, 'Hilux', '2022-10-19 08:14:06'),
(5, 4, 'Fielder', '2022-10-19 08:14:15');

-- --------------------------------------------------------

--
-- Table structure for table `vehicle_service`
--

CREATE TABLE `vehicle_service` (
  `service_id` int(11) NOT NULL,
  `reg_no` varchar(50) NOT NULL,
  `scheduled_date` date NOT NULL,
  `scheduled_time` time NOT NULL,
  `services` varchar(255) NOT NULL,
  `reg_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `status` varchar(50) NOT NULL DEFAULT 'Pending'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vehicle_service`
--

INSERT INTO `vehicle_service` (`service_id`, `reg_no`, `scheduled_date`, `scheduled_time`, `services`, `reg_date`, `status`) VALUES
(1, 'KCE 124P', '2022-10-28', '10:00:00', 'Oil filter', '2022-10-31 12:49:17', 'Completed'),
(2, 'KCE 124P', '2022-10-29', '11:37:00', 'Tyre', '2022-10-26 08:37:34', 'Pending'),
(3, 'KCE 124P', '2022-10-14', '13:57:00', '[]', '2022-10-27 10:58:12', 'Pending'),
(4, 'KCE 124P', '2022-09-28', '13:02:00', '[]', '2022-10-27 10:59:12', 'Pending'),
(5, 'KCE 124P', '2022-09-30', '14:00:00', '[]', '2022-10-27 11:00:40', 'Pending'),
(6, 'KCE 124P', '2022-10-29', '14:08:00', '[\'Oil change\', \'Air filter\', \'Fuel filter\']', '2022-11-01 11:24:18', 'Completed'),
(7, 'KCE 124P', '2022-11-04', '15:43:00', '[\'Oil filter\', \'Air filter\', \'Fuel filter\']', '2022-11-01 12:45:57', 'Completed');

-- --------------------------------------------------------

--
-- Table structure for table `vehicle_task_allocation`
--

CREATE TABLE `vehicle_task_allocation` (
  `task_id` int(50) NOT NULL,
  `reg_no` varchar(50) NOT NULL,
  `from` varchar(50) NOT NULL,
  `to` varchar(50) NOT NULL,
  `scheduled_date` date NOT NULL,
  `scheduled_time` time NOT NULL,
  `trip_completion_status` varchar(50) NOT NULL DEFAULT 'Pending',
  `reg_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `driver_id` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vehicle_task_allocation`
--

INSERT INTO `vehicle_task_allocation` (`task_id`, `reg_no`, `from`, `to`, `scheduled_date`, `scheduled_time`, `trip_completion_status`, `reg_date`, `driver_id`) VALUES
(1, 'KCE 124P', 'Jordan', 'Westlands', '2022-10-05', '15:28:00', 'Pending', '2022-10-24 12:25:54', 10),
(2, 'KCE 124P', 'Nyamira', 'Kakameg', '2022-10-28', '13:13:00', 'Pending', '2022-10-25 10:13:35', 10),
(3, 'KCE 124P', 'Kangemi', 'CBD', '2022-10-29', '21:41:00', 'Pending', '2022-10-26 06:41:13', 10);

-- --------------------------------------------------------

--
-- Table structure for table `vehicle_type`
--

CREATE TABLE `vehicle_type` (
  `type_id` int(50) NOT NULL,
  `type_name` tinytext NOT NULL,
  `reg_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vehicle_type`
--

INSERT INTO `vehicle_type` (`type_id`, `type_name`, `reg_date`) VALUES
(1, 'Van', '2022-09-28 10:08:20'),
(2, 'Bus', '2022-09-28 10:12:22'),
(3, 'Lorry', '2022-09-28 10:12:27'),
(4, 'Car', '2022-09-28 10:12:30'),
(5, 'Motorbike', '2022-09-28 10:12:35'),
(6, 'Pickup', '2022-10-17 10:57:31'),
(7, 'Bus', '2022-10-19 08:12:22');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `capacity`
--
ALTER TABLE `capacity`
  ADD PRIMARY KEY (`capacity_id`);

--
-- Indexes for table `contracts`
--
ALTER TABLE `contracts`
  ADD PRIMARY KEY (`con_id`);

--
-- Indexes for table `drivers`
--
ALTER TABLE `drivers`
  ADD PRIMARY KEY (`driver_id`),
  ADD UNIQUE KEY `dl_no` (`dl_no`),
  ADD KEY `drivers_fk0` (`loc_id`),
  ADD KEY `drivers_fk1` (`con_id`);

--
-- Indexes for table `driver_allocations`
--
ALTER TABLE `driver_allocations`
  ADD PRIMARY KEY (`alloc_id`),
  ADD KEY `driver_allocations_fk0` (`driver_id`),
  ADD KEY `driver_allocations_fk1` (`reg_no`);

--
-- Indexes for table `locations`
--
ALTER TABLE `locations`
  ADD PRIMARY KEY (`loc_id`);

--
-- Indexes for table `owners`
--
ALTER TABLE `owners`
  ADD PRIMARY KEY (`owner_id`),
  ADD KEY `loc_id` (`loc_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `processed`
--
ALTER TABLE `processed`
  ADD PRIMARY KEY (`process_id`),
  ADD KEY `service_id` (`service_id`);

--
-- Indexes for table `vehicles`
--
ALTER TABLE `vehicles`
  ADD PRIMARY KEY (`reg_no`),
  ADD KEY `vehicles_fk0` (`type_id`),
  ADD KEY `vehicles_fk1` (`make_id`),
  ADD KEY `vehicles_fk2` (`model_id`),
  ADD KEY `vehicles_fk3` (`capacity_id`),
  ADD KEY `vehicles_fk4` (`owner_id`);

--
-- Indexes for table `vehicle_make`
--
ALTER TABLE `vehicle_make`
  ADD PRIMARY KEY (`make_id`),
  ADD UNIQUE KEY `make_name` (`make_name`) USING HASH,
  ADD UNIQUE KEY `make_name_2` (`make_name`) USING HASH;

--
-- Indexes for table `vehicle_model`
--
ALTER TABLE `vehicle_model`
  ADD PRIMARY KEY (`model_id`),
  ADD KEY `make_id` (`make_id`);

--
-- Indexes for table `vehicle_service`
--
ALTER TABLE `vehicle_service`
  ADD PRIMARY KEY (`service_id`),
  ADD KEY `vehicle_service_fk0` (`reg_no`);

--
-- Indexes for table `vehicle_task_allocation`
--
ALTER TABLE `vehicle_task_allocation`
  ADD PRIMARY KEY (`task_id`),
  ADD KEY `vehicle_task_allocation_fk0` (`reg_no`),
  ADD KEY `driver_id` (`driver_id`);

--
-- Indexes for table `vehicle_type`
--
ALTER TABLE `vehicle_type`
  ADD PRIMARY KEY (`type_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `user_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `capacity`
--
ALTER TABLE `capacity`
  MODIFY `capacity_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `contracts`
--
ALTER TABLE `contracts`
  MODIFY `con_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `drivers`
--
ALTER TABLE `drivers`
  MODIFY `driver_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `driver_allocations`
--
ALTER TABLE `driver_allocations`
  MODIFY `alloc_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `locations`
--
ALTER TABLE `locations`
  MODIFY `loc_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `owners`
--
ALTER TABLE `owners`
  MODIFY `owner_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `processed`
--
ALTER TABLE `processed`
  MODIFY `process_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `vehicle_make`
--
ALTER TABLE `vehicle_make`
  MODIFY `make_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `vehicle_model`
--
ALTER TABLE `vehicle_model`
  MODIFY `model_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `vehicle_service`
--
ALTER TABLE `vehicle_service`
  MODIFY `service_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `vehicle_task_allocation`
--
ALTER TABLE `vehicle_task_allocation`
  MODIFY `task_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `vehicle_type`
--
ALTER TABLE `vehicle_type`
  MODIFY `type_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `drivers`
--
ALTER TABLE `drivers`
  ADD CONSTRAINT `drivers_fk0` FOREIGN KEY (`loc_id`) REFERENCES `locations` (`loc_id`),
  ADD CONSTRAINT `drivers_fk1` FOREIGN KEY (`con_id`) REFERENCES `contracts` (`con_id`);

--
-- Constraints for table `driver_allocations`
--
ALTER TABLE `driver_allocations`
  ADD CONSTRAINT `driver_allocations_fk0` FOREIGN KEY (`driver_id`) REFERENCES `drivers` (`driver_id`),
  ADD CONSTRAINT `driver_allocations_fk1` FOREIGN KEY (`reg_no`) REFERENCES `vehicles` (`reg_no`);

--
-- Constraints for table `owners`
--
ALTER TABLE `owners`
  ADD CONSTRAINT `owners_ibfk_1` FOREIGN KEY (`loc_id`) REFERENCES `locations` (`loc_id`),
  ADD CONSTRAINT `owners_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `admin` (`user_id`);

--
-- Constraints for table `processed`
--
ALTER TABLE `processed`
  ADD CONSTRAINT `processed_ibfk_1` FOREIGN KEY (`service_id`) REFERENCES `vehicle_service` (`service_id`);

--
-- Constraints for table `vehicles`
--
ALTER TABLE `vehicles`
  ADD CONSTRAINT `vehicles_fk0` FOREIGN KEY (`type_id`) REFERENCES `vehicle_type` (`type_id`),
  ADD CONSTRAINT `vehicles_fk1` FOREIGN KEY (`make_id`) REFERENCES `vehicle_make` (`make_id`),
  ADD CONSTRAINT `vehicles_fk2` FOREIGN KEY (`model_id`) REFERENCES `vehicle_model` (`model_id`),
  ADD CONSTRAINT `vehicles_fk3` FOREIGN KEY (`capacity_id`) REFERENCES `capacity` (`capacity_id`),
  ADD CONSTRAINT `vehicles_fk4` FOREIGN KEY (`owner_id`) REFERENCES `owners` (`owner_id`);

--
-- Constraints for table `vehicle_model`
--
ALTER TABLE `vehicle_model`
  ADD CONSTRAINT `vehicle_model_fk0` FOREIGN KEY (`make_id`) REFERENCES `vehicle_make` (`make_id`),
  ADD CONSTRAINT `vehicle_model_ibfk_1` FOREIGN KEY (`make_id`) REFERENCES `vehicle_make` (`make_id`);

--
-- Constraints for table `vehicle_service`
--
ALTER TABLE `vehicle_service`
  ADD CONSTRAINT `vehicle_service_fk0` FOREIGN KEY (`reg_no`) REFERENCES `vehicles` (`reg_no`);

--
-- Constraints for table `vehicle_task_allocation`
--
ALTER TABLE `vehicle_task_allocation`
  ADD CONSTRAINT `vehicle_task_allocation_fk0` FOREIGN KEY (`reg_no`) REFERENCES `vehicles` (`reg_no`),
  ADD CONSTRAINT `vehicle_task_allocation_ibfk_1` FOREIGN KEY (`driver_id`) REFERENCES `drivers` (`driver_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
