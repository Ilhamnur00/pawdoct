-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 04, 2024 at 07:26 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pawdoct_diagnose`
--

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('72c48cd1a38b');

-- --------------------------------------------------------

--
-- Table structure for table `diagnosa`
--

CREATE TABLE `diagnosa` (
  `id` int(11) NOT NULL,
  `nama_kucing` varchar(255) NOT NULL,
  `jenis_kelamin` varchar(10) NOT NULL,
  `hasil_diagnosa` text NOT NULL,
  `tanggal` datetime DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `gejala_dipilih` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `diagnosa`
--

INSERT INTO `diagnosa` (`id`, `nama_kucing`, `jenis_kelamin`, `hasil_diagnosa`, `tanggal`, `user_id`, `gejala_dipilih`) VALUES
(2, 'pedro', 'jantan', 'Scabies (0.00%), Otitis (0.00%), Cacingan (0.00%), Ringworm (0.00%), Rabies (0.00%)', '2024-11-18 00:42:43', 2, ''),
(3, 'uu', 'jantan', 'Scabies (0.00%), Otitis (0.00%), Cacingan (0.00%), Ringworm (0.00%), Rabies (0.00%)', '2024-11-18 01:01:10', 2, ''),
(4, 'a7', 'jantan', 'Scabies (0.00%), Otitis (0.00%), Cacingan (0.00%), Ringworm (0.00%), Rabies (0.00%)', '2024-11-18 01:03:21', 2, ''),
(5, '99', 'jantan', 'Scabies (0.00%), Otitis (0.00%), Cacingan (0.00%), Ringworm (0.00%), Rabies (0.00%)', '2024-11-18 01:03:47', 2, ''),
(6, 'oyoy', 'jantan', 'Scabies (37.50%), Otitis (0.00%), Cacingan (0.00%), Ringworm (0.00%), Rabies (41.18%)', '2024-11-18 01:53:44', 2, ''),
(7, 'jono', 'jantan', 'Scabies (100.00%), Otitis (25.00%), Cacingan (0.00%), Ringworm (0.00%), Rabies (47.06%)', '2024-11-18 02:16:45', 2, ''),
(8, 'rudi', 'betina', 'Scabies (100.00%), Otitis (40.00%), Cacingan (33.33%), Ringworm (0.00%), Rabies (0.00%)', '2024-11-18 02:30:57', 2, ''),
(9, '00', 'jantan', 'Scabies (0.00%), Otitis (0.00%), Cacingan (0.00%), Ringworm (0.00%), Rabies (0.00%)', '2024-11-18 03:06:01', 2, ''),
(10, 'yono', 'jantan', 'Scabies (100.00%), Otitis (55.00%), Cacingan (33.33%), Ringworm (62.50%), Rabies (35.29%)', '2024-11-18 03:27:11', 2, 'g1, g2, g3, g6, g8, g10, g13, g16, g19'),
(11, 'ii', 'jantan', 'Scabies (0.00%), Otitis (0.00%), Cacingan (0.00%), Ringworm (0.00%), Rabies (0.00%)', '2024-11-18 04:34:05', 2, ''),
(12, 'oo', 'jantan', 'Scabies (100.00%), Otitis (15.00%), Cacingan (0.00%), Ringworm (0.00%), Rabies (0.00%)', '2024-11-18 04:34:35', 2, 'g1, g2, g5'),
(13, 'ubek', 'jantan', 'Scabies (100.00%), Otitis (30.00%), Cacingan (0.00%), Ringworm (0.00%), Rabies (0.00%)', '2024-11-18 05:45:58', 2, 'g1, g2, g3, g6, g9'),
(14, 'uno', 'jantan', 'Scabies (0.00%), Otitis (0.00%), Cacingan (0.00%), Ringworm (62.50%), Rabies (0.00%)', '2024-11-18 07:13:09', 2, 'g13'),
(15, 'uno', 'jantan', 'Scabies (0.00%), Otitis (0.00%), Cacingan (0.00%), Ringworm (62.50%), Rabies (0.00%)', '2024-11-18 07:13:12', 2, 'g13'),
(16, 'yadi', 'jantan', 'Scabies (100.00%), Otitis (25.00%), Cacingan (0.00%), Ringworm (0.00%), Rabies (0.00%)', '2024-11-18 07:59:54', 2, 'g1, g2, g7'),
(17, 'am', 'jantan', 'Scabies (100.00%), Otitis (30.00%), Cacingan (0.00%), Ringworm (0.00%), Rabies (0.00%)', '2024-11-18 13:10:52', 2, 'g1, g2, g3, g7'),
(18, 'yono', 'jantan', 'Scabies (100.00%), Otitis (50.00%), Cacingan (0.00%), Ringworm (0.00%), Rabies (0.00%)', '2024-11-18 13:46:07', 2, 'g1, g2, g3, g4, g5, g6'),
(19, 'jago', 'jantan', 'Scabies (37.50%), Otitis (50.00%), Cacingan (100.00%), Ringworm (0.00%), Rabies (0.00%)', '2024-11-18 15:31:42', 2, 'g1, g7, g8, g9, g10, g11, g12'),
(20, 'ringgo', 'jantan', 'Scabies (0.00%), Otitis (0.00%), Cacingan (33.33%), Ringworm (100.00%), Rabies (64.71%)', '2024-11-18 15:38:30', 2, 'g12, g13, g14, g15, g16, g19'),
(21, 'uno', 'betina', 'Scabies (37.50%), Otitis (40.00%), Cacingan (100.00%), Ringworm (0.00%), Rabies (35.29%)', '2024-11-18 15:42:03', 2, 'g1, g5, g7, g10, g11, g12, g16, g19'),
(22, 'yolo', 'jantan', 'Scabies (100.00%), Otitis (50.00%), Cacingan (33.33%), Ringworm (62.50%), Rabies (29.41%)', '2024-11-19 05:27:51', 2, 'g1, g2, g7, g8, g12, g13, g16'),
(23, 'pawpaw', 'jantan', 'Scabies (37.50%), Otitis (25.00%), Cacingan (100.00%), Ringworm (100.00%), Rabies (94.12%)', '2024-11-19 07:00:11', 2, 'g1, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, g18'),
(24, 'yanti', 'jantan', 'Scabies (62.50%), Otitis (0.00%), Cacingan (33.33%), Ringworm (100.00%), Rabies (100.00%)', '2024-11-19 08:53:02', 2, 'g2, g12, g13, g14, g15, g16, g17, g18, g19'),
(25, 'inang', 'jantan', 'Scabies (100.00%), Otitis (5.00%), Cacingan (0.00%), Ringworm (0.00%), Rabies (0.00%)', '2024-11-19 08:54:12', 2, 'g1, g2, g3'),
(26, 'ireng', 'jantan', 'Scabies (100.00%), Otitis (75.00%), Cacingan (0.00%), Ringworm (0.00%), Rabies (0.00%)', '2024-11-19 09:11:25', 2, 'g1, g2, g3, g4, g5, g6, g7'),
(27, 'ang ang', 'jantan', 'Scabies (37.50%), Otitis (65.00%), Cacingan (66.67%), Ringworm (37.50%), Rabies (41.18%)', '2024-12-04 04:05:39', 8, 'g1, g5, g6, g7, g10, g11, g14, g17, g18, g19'),
(28, 'yolo', 'jantan', 'Scabies (100.00%), Otitis (55.00%), Cacingan (33.33%), Ringworm (0.00%), Rabies (23.53%)', '2024-12-04 04:13:21', 8, 'g1, g2, g3, g6, g7, g10, g17, g19'),
(29, 'amam', 'jantan', 'Scabies (100.00%), Otitis (55.00%), Cacingan (33.33%), Ringworm (62.50%), Rabies (29.41%)', '2024-12-04 05:14:06', 8, 'g1, g2, g3, g6, g8, g11, g13, g15');

-- --------------------------------------------------------

--
-- Table structure for table `gejala`
--

CREATE TABLE `gejala` (
  `id` int(11) NOT NULL,
  `kode_gejala` varchar(10) NOT NULL,
  `gejala` varchar(255) NOT NULL,
  `bobot` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `gejala`
--

INSERT INTO `gejala` (`id`, `kode_gejala`, `gejala`, `bobot`) VALUES
(1, 'g1', 'Bulu rontok yang menyebabkan kebotakan', 3),
(2, 'g2', 'Ada kerak berwarna putih di sekitar daun telinga', 5),
(3, 'g3', 'Kulit terlihat bersisik', 1),
(4, 'g4', 'Gatal sekitar telinga', 1),
(5, 'g5', 'Sering mengoyangkan/menggelengkan kepala', 3),
(6, 'g6', 'Sering menggaruk telinga hingga terdapat luka', 5),
(7, 'g7', 'Muncul cairan yang berbau tidak sedap dari dalam telinga', 5),
(8, 'g8', 'Posisi kepala yang selalu miring-miring dan tidak mampu berjalan lurus', 5),
(9, 'g9', 'Mata belekan', 3),
(10, 'g10', 'Perut buncit tapi badan kurus', 5),
(11, 'g11', 'Diare', 5),
(12, 'g12', 'Keluar cacing saat muntah atau pada kotoran kucing', 5),
(13, 'g13', 'Ada kerontokan bulu yang berbentuk lingkaran', 5),
(14, 'g14', 'Sering menggaruk badan', 3),
(15, 'g15', 'Agresif (sering menggigit dengan ganas)', 5),
(16, 'g16', 'Sensitif (sering mencakar bila disentuh)', 5),
(17, 'g17', 'Tidak nafsu makan', 3),
(18, 'g18', 'Gelisah/suka bersembunyi/takut air', 3),
(19, 'g19', 'Lemas/Lesu', 1);

-- --------------------------------------------------------

--
-- Table structure for table `penyakit`
--

CREATE TABLE `penyakit` (
  `id` int(11) NOT NULL,
  `nama_penyakit` varchar(255) NOT NULL,
  `deskripsi` text NOT NULL,
  `solusi` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `penyakit`
--

INSERT INTO `penyakit` (`id`, `nama_penyakit`, `deskripsi`, `solusi`) VALUES
(1, 'Scabies', 'Merupakan penyakit kulit yang disebabkan oleh tungau (sejenis kutu) scabies/sarcoptes. Penyakit ini sering menyerang anjing, kucing, kelinci.', 'Halo Pawrents, jangan panik ya apabila kucing Anda terdeteksi menderita Scabies, ikuti prosedur penanganan yang tepat sebelum terlambat! Penanganan scabies pada kucing meliputi diagnosis oleh dokter hewan, perawatan dengan obat topikal seperti salep atau krim anti-parasit, serta pemberian obat sistemik seperti ivermectin atau selamectin untuk membasmi tungau secara menyeluruh. Mandi dengan shampoo anti-parasit dan pemberian suplemen untuk memperbaiki nutrisi juga membantu mempercepat pemulihan. Kucing yang terinfeksi perlu diisolasi untuk mencegah penularan, sementara lingkungan seperti kandang dan tempat tidur harus dibersihkan secara rutin menggunakan desinfektan. Pencegahan penyakit tambahan dilakukan dengan memastikan kucing tidak menjilat area yang diolesi obat menggunakan kerah pelindung. Kontrol rutin ke dokter hewan diperlukan hingga kucing sembuh sepenuhnya, dan pencegahan jangka panjang dengan pemberian obat antiparasit secara berkala dapat mencegah kekambuhan atau infestasi baru.'),
(2, 'Otitis', 'Merupakan penyakit yang dapat disebabkan oleh beberapa macam kondisi seperti serangan tungau, bakteri, jamur, kanker, alergi, gangguan sistem kekebalan tubuh, dan lain-lain. Otitis dapat terjadi pada salah satu bagian telinga (luar, tengah, dan dalam).', 'Liat Kucing kita terkena Otitis bikin hati pawrents teriris yaa:( Jangan Sedih, tetap tenang dan ikuti step penanganannya. Penanganan otitis pada kucing dimulai dengan diagnosis oleh dokter hewan untuk menentukan penyebabnya, seperti infeksi bakteri, jamur, parasit (tungau), atau alergi. Telinga kucing perlu dibersihkan secara rutin menggunakan cairan pembersih telinga khusus untuk menghilangkan kotoran dan menjaga kebersihannya. Obat topikal, seperti tetes telinga yang mengandung antibiotik, antijamur, atau antiparasit, diberikan sesuai penyebabnya, dan terkadang obat antiinflamasi untuk mengurangi peradangan. Jika diperlukan, dokter dapat meresepkan obat sistemik seperti antibiotik atau antijamur oral untuk infeksi berat. Hindari membersihkan telinga terlalu dalam agar tidak melukai saluran telinga. Pemantauan rutin dilakukan untuk memastikan kondisi membaik, sementara perawatan preventif seperti menjaga kebersihan telinga dan mencegah infestasi tungau penting untuk mencegah kekambuhan.'),
(3, 'Cacingan', 'Merupakan endoparasit (parasit yang hidup dalam tubuh) yang sering menyerang kucing. Sebagian besar cacing menular melalui telur yang biasanya terdapat pada kotoran kucing atau tertular dari air susu induk kucing. Cacing yang sering menyerang kucing ada 2 jenis yaitu cacing gelang (gilig) dan cacing pita.', 'Udah jaga kebersihan,tapi yang namanya penyakit emang tak terhindar ya Pawrent. Tapi tenang, penanganan cacingan pada kucing cukup mudah kok. Caranya dengan melakukan pemberian obat cacing sesuai jenis cacing yang menginfeksi, seperti pyrantel pamoate, praziquantel, atau fenbendazole, yang diberikan sesuai dosis dan petunjuk dokter hewan. Kebersihan lingkungan kucing harus dijaga dengan membersihkan tempat tidur, litter box, dan area bermain secara rutin untuk mencegah reinfeksi. Suplemen dapat diberikan untuk memperbaiki kondisi tubuh kucing yang lemah akibat infestasi cacing. Pencegahan dilakukan dengan pemberian obat cacing secara rutin setiap 3-6 bulan, menjaga kebersihan makanan dan minuman, serta mencegah kontak dengan hewan liar atau lingkungan yang terkontaminasi.'),
(4, 'Ringworm', 'Merupakan penyakit yang disebabkan oleh jamur yang hidup di kulit dan bulu. Salah satu spesies jamur yang sering menyerang kucing dan anjing adalah Microsporum canis.', 'Saat Kucing sakit, kita jangan langsung panik ya, ikuti langkah penanganannya dengan cara memberi obat antijamur topikal seperti krim atau shampoo yang mengandung miconazole atau ketoconazole, serta obat antijamur oral seperti itraconazole untuk infeksi yang parah. Lingkungan kucing harus rutin dibersihkan dan didisinfeksi untuk mencegah penyebaran spora jamur. Kucing yang terinfeksi perlu diisolasi hingga sembuh sepenuhnya. Pencegahan dilakukan dengan menjaga kebersihan, menghindari kontak dengan hewan yang terinfeksi, dan memastikan daya tahan tubuh kucing tetap baik melalui pola makan sehat dan perawatan rutin.'),
(5, 'Rabies', 'Merupakan penyakit menular yang akut yang dapat menular pada manusia, yang disebabkan oleh virus rabies jenis Rhabdho virus.', 'Rabies bikin worry ya Pawrents:( Penanganan rabies pada kucing tidak dapat dilakukan setelah gejala muncul, sehingga pencegahan adalah kunci utama. Kucing harus diberikan vaksin rabies secara rutin sesuai jadwal yang ditetapkan dokter hewan. Jika kucing digigit atau terpapar hewan yang dicurigai rabies, segera bawa ke dokter hewan untuk evaluasi. Kucing yang menunjukkan gejala rabies harus diisolasi, dan pihak berwenang wajib diberitahu untuk tindakan lebih lanjut sesuai peraturan. Pencegahan tambahan mencakup membatasi interaksi kucing dengan hewan liar dan menjaga lingkungan tetap aman.');

-- --------------------------------------------------------

--
-- Table structure for table `penyakit_gejala`
--

CREATE TABLE `penyakit_gejala` (
  `id` int(11) NOT NULL,
  `penyakit_id` int(11) NOT NULL,
  `kode_gejala` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `penyakit_gejala`
--

INSERT INTO `penyakit_gejala` (`id`, `penyakit_id`, `kode_gejala`) VALUES
(1, 1, 'g1'),
(2, 1, 'g2'),
(3, 2, 'g3'),
(4, 2, 'g4'),
(5, 2, 'g5'),
(6, 2, 'g6'),
(7, 2, 'g7'),
(8, 2, 'g8'),
(9, 3, 'g10'),
(10, 3, 'g11'),
(11, 3, 'g12'),
(12, 4, 'g13'),
(13, 4, 'g14'),
(14, 5, 'g15'),
(15, 5, 'g16'),
(16, 5, 'g17'),
(17, 5, 'g18'),
(18, 5, 'g19');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `address` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `email`, `phone`, `gender`, `address`) VALUES
(1, 'ata', 'scrypt:32768:8:1$bpXbG3Gsg5DxXKs9$39ab229a92c3f0d9faa721b9ed894490fe4df2a0a835b3a80e48cf361664a752b927e0479db427faff3d215664aff839605e87e48cacab16149d7b575514d42b', 'ilhamnurfjri@student.telkomuniversity.ac.id', NULL, NULL, NULL),
(2, 'am2', 'scrypt:32768:8:1$3GgVVFhwDH4qxl9v$e9846b37e346521ccd5f80771237058edca4621d3c89bf627d09d1b49712e0628a96bd959d01d943069df0aa4d641b068882f762e3658d5eb5f06cfb1021d713', '2211102295@ittelkom-pwt.ac.id', '081476652111', 'male', 'purwokerto'),
(4, 'oi', 'scrypt:32768:8:1$CECDzeHVunW8zT61$fef1b364fbafcfdb6beade38babe66b27ade9f3866f497b633b72f344db7ad432965511c929f9ca0e48d83fd2e185f07e968e09609c1ed2b66584952c53e7dbc', 'ferlanddonella239@hotmail.com', '081476652833', 'male', 'jl.sudagaran 2'),
(5, 'pawpaw12', 'scrypt:32768:8:1$9EMMXIl0Bkt2o4et$f9346a81f2e078d8c3f838f49a979087bf74e94bb82017ca8273d8fd52786f07f50e10dd2e3d1ece219dbb2ae10e394dbd8cd4ed66a97f4ef3a1a7f0ceb2c0e6', 'ilham.nurfajri121@gmail.com', '085962506547', 'male', 'tegal'),
(6, 'adhel', 'scrypt:32768:8:1$3VHKthrBW3tXPXtc$84e406540f46cb5fd6fe3abbd3e650fc37ebc30d582b317bb00110d6eedc60373d56c176a85c8ea5d695074a5fb73bafff735fbe54fe35f4367a7e8ddede1077', 'adhel@gmail.com', '081476652833', 'female', 'pwt usyara'),
(7, 'amam', 'pbkdf2:sha256:260000$WeYimPPWvVLIVnyb$0d7394eca41f75bcdd1daa4f77c4ac8473efae22bcf99b5d2477cacb5cdd1c50', 'amam@gmail.com', '081483625257', 'female', 'pwt usyara'),
(8, 'ayo', 'pbkdf2:sha256:260000$Zs4ZSDXXKFRJqOMr$f87a626f01022ba10dfa935ce04496d6068be69e23c5f18934434f016c8b4cb7', 'aliwafacreew@gmail.com', '0814836252500', 'male', 'pwt usyara'),
(9, 'pawdoct', 'pbkdf2:sha256:260000$xUPrVGLOJigmz6Uq$df6a79f5e32d06e00bf56bc9b5831f507f5d2e50c407a0740379110ee0de572a', '1pawdoct@gmail.com', '081483625257', 'male', 'pwt usyara');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `diagnosa`
--
ALTER TABLE `diagnosa`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `gejala`
--
ALTER TABLE `gejala`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `kode_gejala` (`kode_gejala`);

--
-- Indexes for table `penyakit`
--
ALTER TABLE `penyakit`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `penyakit_gejala`
--
ALTER TABLE `penyakit_gejala`
  ADD PRIMARY KEY (`id`),
  ADD KEY `kode_gejala` (`kode_gejala`),
  ADD KEY `penyakit_id` (`penyakit_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `diagnosa`
--
ALTER TABLE `diagnosa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `gejala`
--
ALTER TABLE `gejala`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `penyakit`
--
ALTER TABLE `penyakit`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `penyakit_gejala`
--
ALTER TABLE `penyakit_gejala`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `diagnosa`
--
ALTER TABLE `diagnosa`
  ADD CONSTRAINT `diagnosa_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `penyakit_gejala`
--
ALTER TABLE `penyakit_gejala`
  ADD CONSTRAINT `penyakit_gejala_ibfk_1` FOREIGN KEY (`kode_gejala`) REFERENCES `gejala` (`kode_gejala`),
  ADD CONSTRAINT `penyakit_gejala_ibfk_2` FOREIGN KEY (`penyakit_id`) REFERENCES `penyakit` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
