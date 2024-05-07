-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 07 May 2024, 22:07:04
-- Sunucu sürümü: 10.4.32-MariaDB
-- PHP Sürümü: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `python_ecza`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `ilaclar`
--

CREATE TABLE `ilaclar` (
  `id` int(11) NOT NULL,
  `ilac_adi` text NOT NULL,
  `turu` text NOT NULL,
  `kategori` text NOT NULL,
  `kullanim` text NOT NULL,
  `stk` text NOT NULL,
  `Stok` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `ilaclar`
--

INSERT INTO `ilaclar` (`id`, `ilac_adi`, `turu`, `kategori`, `kullanim`, `stk`, `Stok`) VALUES
(1, 'Vermidon', 'Ağrı kesici', 'Tablet', 'Tok Sabah-öğle-akşam', '12.02.2028', 7),
(2, 'Paramin', 'Ağrı kesici', 'Tablet', 'Tok karına Sabah-Akşam', '02.12.2029', 9),
(3, 'Croxilex', 'Antibiyotik', 'Tablet', 'Tok karına Sabah-Akşam', '11.09.2028', 11),
(4, 'Augmentin', 'Antibiyotik', 'Şurup', 'Tok karına Sabah-Akşam ', '12.11.2029', 20),
(5, 'Vitamin-C', 'Vitamin', 'Tablet', 'Tok karına günde 1 kere', '12.02.2029', 120),
(6, 'Calpop', 'Ağrı kesici', 'Şurup', 'Aç/tok karına Sabah-Akşam', '11.11.2025', 1),
(7, 'Pedifen', 'Ağrı kesici', 'Şurup', 'Aç/tok karına Sabah-Akşam', '09.12.2029', 90),
(8, 'TYLOL', 'Ağrı kesici', 'Şurup', 'Aç/tok karına Sabah-Akşam', '12.12.2028', 8),
(9, 'Arveles', 'Ağrı kesici', 'Tablet', 'Tok karına Sabah-Öğle-Akşam', '12.12.2028', 12),
(10, 'Majezik', 'Ağrı kesici', 'Tablet', 'Tok karına Sabah-Öğle-Akşam', '12.12.2029', 11),
(11, 'Dexday', 'Ağrı kesici', 'Tablet', 'Tok karına Sabah-Öğle-Akşam', '07.12.2027', 7),
(12, 'Klamoks', 'Antibiyotik', 'Şurup', 'Tok karına Sabah-Akşam', '12.09.2026', 3),
(13, 'Zimaks', 'Antibiyotik', 'Şurup', 'Tok karına Sabah-Akşam', '12.09.2026', 4),
(14, 'Macrol', 'Antibiyotik', 'Şurup', 'Tok karına Sabah-Akşam', '12.12.2028', 7),
(15, 'Klavunat', 'Antibiyotik', 'Şurup', 'Tok karına Sabah-Akşam', '12.12.2028', 22),
(16, 'Amoklavin', 'Antibiyotik', 'Tablet', 'Tok karına Sabah-Akşam', '12.12.2028', 17),
(17, 'Devamox', 'Antibiyotik', 'Tablet', 'Tok karına Sabah-Akşam', '12.12.2025', 10),
(18, 'Cefaks', 'Antibiyotik', 'Tablet', 'Tok karına Sabah-Akşam', '12.09.2030', 25),
(19, 'Miraderm-C', 'Vitamin', 'Tablet', 'Tok karına Günde 1 kere', '12.12.2030', 13),
(20, 'Nutraxin-A', 'Vitamin', 'Tablet', 'Tok karına Günde 1 kere', '12.12.2030', 18),
(21, 'Nutraxin-M', 'Vitamin', 'Tablet', 'Tok karına Günde 1 kere', '12.12.2030', 5),
(22, 'Multidyn-B', 'Vitamin', 'Tablet', 'Tok karına Günde 1 kere', '12.12.2030', 23),
(23, 'Vitagil-M', 'Vitamin', 'Şurup', 'Tok karına Günde 1 kere', '12.12.2030', 11),
(24, 'Dina-A', 'Vitamin', 'Şurup', 'Tok karına Günde 1 kere', '12.12.2030', 0),
(25, 'Orzax-D', 'Vitamin', 'Şurup', 'Tok karına Günde 1 kere', '12.12.2030', 7),
(26, 'Nutri-B', 'Vitamin', 'Şurup', 'Tok karına Günde 1 kere', '12.11.2028', 12),
(27, 'MVC-M', 'Vitamin', 'Krem', 'El-Kol-Ayak bölgesine uygulanır', '08.10.2027', 11),
(28, 'Numbuzin-D', 'Vitamin', 'Krem', 'El-Kol-Ayak bölgesine uygulanır', '03.10.2028', 33),
(32, 'Vitavy-D', 'Vitamin', 'Krem', 'El-Kol-Ayak bölgesine uygulanır', '12.09.2028', 2),
(35, 'Riemser', 'Ağrı kesici', 'Krem', 'Ağrı bölgesine uygulanır', '12.02.2027', 0),
(36, 'Estesua', 'Ağrı kesici', 'krem', 'Ağrı bölgesine uygulanır', '12.02.2026', 6);

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `ilaclar`
--
ALTER TABLE `ilaclar`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `ilaclar`
--
ALTER TABLE `ilaclar`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
