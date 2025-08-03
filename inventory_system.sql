
-- This is optional if someone is trying to use sql using wamp server 

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

-- Database: `inventory_system`

CREATE TABLE IF NOT EXISTS `category_data` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `category_data`
--

INSERT INTO `category_data` (`id`, `name`, `description`) VALUES
(1, 'Roshukesh Pvt Limited', 'Handlooms Provider'),
(2, 'Duvyansh Corp', 'Multiple businesses'),
(3, 'Sinister Pvt', 'Spare parts of vehicles');

-- --------------------------------------------------------

--
-- Table structure for table `employee_data`
--

CREATE TABLE IF NOT EXISTS `employee_data` (
  `empid` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `dob` varchar(30) NOT NULL,
  `contact` varchar(30) NOT NULL,
  `employment_type` varchar(50) NOT NULL,
  `education` varchar(50) NOT NULL,
  `work_shift` varchar(50) NOT NULL,
  `address` varchar(100) NOT NULL,
  `doj` varchar(30) NOT NULL,
  `salary` varchar(50) NOT NULL,
  `usertype` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`empid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `employee_data`
--

INSERT INTO `employee_data` (`empid`, `name`, `email`, `gender`, `dob`, `contact`, `employment_type`, `education`, `work_shift`, `address`, `doj`, `salary`, `usertype`, `password`) VALUES
(1, 'Rishu', 'rishu@gmail.com', 'Male', '08/05/2012', '9876453122', 'Part Time', 'M.Tech', 'Evening', 'rohan ke ghar ke niche\n', '09/05/2022', '15', 'Employee', '1234'),
(2, 'Bade Bhai', 'example@gmail.com', 'Male', '11/05/1994', '9999999999', 'Intern', 'B.Sc', 'Night', 'Rishu ke ghar ke neeche', '11/05/2023', '1000', 'Employee', '8765#'),
(3, 'ridhi', 'example@gmail.com', 'Male', '16/05/2003', '3928292222', 'Casual', 'B.Com', 'Night', 'School apartments', '10/05/2024', '2', 'Admin', 'rr@@@'),
(4, 'Rohan', 'ggg@gmail.com', 'Male', '16/05/2014', '0938493849', 'Contract', 'B.Sc', 'Evening', 'Rdhi apartments', '13/05/2022', '11', 'Employee', 'ridh@gang');

-- --------------------------------------------------------

--
-- Table structure for table `product_data`
--

CREATE TABLE IF NOT EXISTS `product_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(100) NOT NULL,
  `supplier` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `discount` int(11) NOT NULL,
  `discount_price` decimal(10,2) NOT NULL,
  `quantity` int(11) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `product_data`
--

INSERT INTO `product_data` (`id`, `category`, `supplier`, `name`, `price`, `discount`, `discount_price`, `quantity`, `status`) VALUES
(1, 'Roshukesh Pvt Limited', 'Rohas', 'Doll', '20000.00', 5, '19000.00', 10, 'Active'),
(2, 'Sinister Pvt', 'Rishabh P', 'Doors of cars', '3000.00', 20, '2550.00', 20, 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `supplier_data`
--

CREATE TABLE IF NOT EXISTS `supplier_data` (
  `invoice` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `contact` varchar(15) NOT NULL,
  `description` text NOT NULL,
  PRIMARY KEY (`invoice`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `supplier_data`
--

INSERT INTO `supplier_data` (`invoice`, `name`, `contact`, `description`) VALUES
(1, 'Rohas', '1928392892', 'rreeomr'),
(2, 'Rohan', '19283928922', 'rreeomr'),
(3, 'Chometu', '9283718298', 'ROOOOOOOOOSHHHHUIIIIISUIIII'),
(4, 'Ruu', '2938291128', 'iir'),
(5, 'Rishabh P', '9876543210', 'Regular provider');

-- --------------------------------------------------------

--
-- Table structure for table `tax_table`
--

CREATE TABLE IF NOT EXISTS `tax_table` (
  `id` int(11) NOT NULL,
  `tax` decimal(5,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tax_table`
--

INSERT INTO `tax_table` (`id`, `tax`) VALUES
(1, '25.00');
