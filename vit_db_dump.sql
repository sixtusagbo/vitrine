-- MySQL dump 10.13  Distrib 8.0.33, for Linux (x86_64)
--
-- Host: localhost    Database: vit_db
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `brands`
--

DROP TABLE IF EXISTS `brands`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `brands` (
  `name` varchar(49) NOT NULL,
  `handle` varchar(15) NOT NULL,
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `statement` varchar(128) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `is_solopreneur` tinyint(1) DEFAULT NULL,
  `cover_image` varchar(128) DEFAULT NULL,
  `detail_lead` varchar(255) DEFAULT NULL,
  `detail_image` varchar(128) DEFAULT NULL,
  `whatsapp_no` varchar(15) DEFAULT NULL,
  `twitter_url` varchar(255) DEFAULT NULL,
  `instagram_url` varchar(255) DEFAULT NULL,
  `youtube_url` varchar(255) DEFAULT NULL,
  `telegram_url` varchar(255) DEFAULT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brands`
--

LOCK TABLES `brands` WRITE;
/*!40000 ALTER TABLE `brands` DISABLE KEYS */;
INSERT INTO `brands` VALUES ('Nature\'s Bounty','naturesbounty','info@naturesbounty.com','bounty@123','369 Pine Street, Town','Harnessing the power of nature','We offer natural and organic products for a healthy lifestyle.',0,'https://source.unsplash.com/random/800x400?naturesbounty','About Nature\'s Bounty','https://source.unsplash.com/random/800x400?naturesbounty-detail','+3692581470','https://twitter.com/naturesbounty','https://instagram.com/naturesbounty','https://youtube.com/naturesbounty','https://t.me/naturesbounty','02e8f4cf-537c-45e3-916c-2620ff0a6a97','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Luxe Haven','luxehaven','info@luxehaven.com','haven@123','789 Maple Street, Town','Indulge in luxury and elegance','We offer exquisite and opulent experiences for discerning individuals.',0,'https://source.unsplash.com/random/800x400?luxehaven','About Luxe Haven','https://source.unsplash.com/random/800x400?luxehaven-detail','+9876543210','https://twitter.com/luxehaven','https://instagram.com/luxehaven','https://youtube.com/luxehaven','https://t.me/luxehaven','19ab9edf-4a6c-40ae-a099-13424992e960','2023-07-07 00:27:13','2023-07-07 00:27:13'),('Creative Minds','creativeminds','info@creativeminds.com','creative@123','456 Oak Street, City','Unleashing creativity and imagination','We foster artistic expression and innovation.',0,'https://source.unsplash.com/random/800x400?creativeminds','About Creative Minds','https://source.unsplash.com/random/800x400?creativeminds-detail','+4567891230','https://twitter.com/creativeminds','https://instagram.com/creativeminds','https://youtube.com/creativeminds','https://t.me/creativeminds','3099368a-e852-4be6-8bd0-b17ba42e6f02','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Acme Corporation','acmecorp','info@acmecorp.com','acme@123','123 Main Street, City','Providing top-notch products','We are a leading provider of innovative solutions.',0,'https://source.unsplash.com/random/800x400?acmecorp','About Acme Corporation','https://source.unsplash.com/random/800x400?acmecorp-detail','+1234567890','https://twitter.com/acmecorp','https://instagram.com/acmecorp','https://youtube.com/acmecorp','https://t.me/acmecorp','4113bf98-bef4-4c5d-a015-9635cd6bac89','2023-07-07 00:27:11','2023-07-07 00:27:11'),('Infinite Innovations','infiniteinnov','info@infiniteinnov.com','innovate@123','456 Park Avenue, Town','Empowering the future with innovation','We strive to create revolutionary solutions.',0,'https://source.unsplash.com/random/800x400?infiniteinnov','About Infinite Innovations','https://source.unsplash.com/random/800x400?infiniteinnov-detail','+9876543210','https://twitter.com/infiniteinnov','https://instagram.com/infiniteinnov','https://youtube.com/infiniteinnov','https://t.me/infiniteinnov','44663478-fac6-4ab5-9808-8e7e312e2476','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Elevate Fashion','elevatefashion','info@elevatefashion.com','elevate@123','246 Elm Street, City','Redefining style with elegance','We curate the latest trends for fashion enthusiasts.',0,'https://source.unsplash.com/random/800x400?elevatefashion','About Elevate Fashion','https://source.unsplash.com/random/800x400?elevatefashion-detail','+2468135790','https://twitter.com/elevatefashion','https://instagram.com/elevatefashion','https://youtube.com/elevatefashion','https://t.me/elevatefashion','7a301f04-51a4-43c8-a588-f8104ebf33a8','2023-07-07 00:27:12','2023-07-07 00:27:12'),('EcoEssentials','ecoessentials','info@ecoessentials.com','eco@123','246 Forest Avenue, City','Promoting eco-friendly and sustainable living','We offer a wide range of eco-friendly products for a greener lifestyle.',0,'https://source.unsplash.com/random/800x400?ecoessentials','About EcoEssentials','https://source.unsplash.com/random/800x400?ecoessentials-detail','+1234567890','https://twitter.com/ecoessentials','https://instagram.com/ecoessentials','https://youtube.com/ecoessentials','https://t.me/ecoessentials','8154060a-be0a-4738-b238-9fa7c056ed77','2023-07-07 00:27:13','2023-07-07 00:27:13'),('Green Earth','greenearth','info@greenearth.com','green@123','123 Park Avenue, Town','Preserving our planet for future generations','We promote eco-friendly practices and sustainable living.',1,'https://source.unsplash.com/random/800x400?greenearth','About Green Earth','https://source.unsplash.com/random/800x400?greenearth-detail','+1234567890','https://twitter.com/greenearth','https://instagram.com/greenearth','https://youtube.com/greenearth','https://t.me/greenearth','9f4b02ce-0d4f-46ab-8c2b-ce82ecb062a8','2023-07-07 00:27:12','2023-07-07 00:27:12'),('TechVision','techvision','info@techvision.com','tech@123','789 Elm Street, City','Envisioning the future of technology','We explore innovative tech solutions for a digital world.',0,'https://source.unsplash.com/random/800x400?techvision','About TechVision','https://source.unsplash.com/random/800x400?techvision-detail','+7894561230','https://twitter.com/techvision','https://instagram.com/techvision','https://youtube.com/techvision','https://t.me/techvision','acab5178-35dd-4bb7-9d3d-10bfe3f881f7','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Vitality Wellness','vitalitywell','info@vitalitywell.com','vitality@123','789 Oak Street, Village','Nurturing mind, body, and soul','We are dedicated to promoting holistic well-being.',1,'https://source.unsplash.com/random/800x400?vitalitywell','About Vitality Wellness','https://source.unsplash.com/random/800x400?vitalitywell-detail','+1357924680','https://twitter.com/vitalitywell','https://instagram.com/vitalitywell','https://youtube.com/vitalitywell','https://t.me/vitalitywell','c5bdc7a1-3d18-4f69-872a-b4a4441a1187','2023-07-07 00:27:12','2023-07-07 00:27:12');
/*!40000 ALTER TABLE `brands` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detail_points`
--

DROP TABLE IF EXISTS `detail_points`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detail_points` (
  `content` varchar(128) NOT NULL,
  `brand_id` varchar(60) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `brand_id` (`brand_id`),
  CONSTRAINT `detail_points_ibfk_1` FOREIGN KEY (`brand_id`) REFERENCES `brands` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detail_points`
--

LOCK TABLES `detail_points` WRITE;
/*!40000 ALTER TABLE `detail_points` DISABLE KEYS */;
INSERT INTO `detail_points` VALUES ('Bringing balance to your life','c5bdc7a1-3d18-4f69-872a-b4a4441a1187','0d454e96-a90f-40ad-857d-cc74996f2811','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Promoting sustainable alternatives for everyday living','8154060a-be0a-4738-b238-9fa7c056ed77','2a29b032-47e4-4a79-a7a7-839430f34670','2023-07-07 00:27:13','2023-07-07 00:27:13'),('Advocating for a greener future','9f4b02ce-0d4f-46ab-8c2b-ce82ecb062a8','2b67a637-ae79-4e58-aeba-3fe60ccfc5c4','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Pioneering new technology since 2010','44663478-fac6-4ab5-9808-8e7e312e2476','2dd09d90-86a2-498b-914a-7384fa2859a9','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Nurturing artistic talent','3099368a-e852-4be6-8bd0-b17ba42e6f02','392396a8-346a-435f-b0a5-5b33e7a44daf','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Promoting self-care and mindfulness','c5bdc7a1-3d18-4f69-872a-b4a4441a1187','3aa88ba9-8224-444f-8b5e-54d226336cbb','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Harvesting the best from nature','02e8f4cf-537c-45e3-916c-2620ff0a6a97','5b4c4383-0b2c-444f-b739-2e00d35ceda5','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Established in 2005','4113bf98-bef4-4c5d-a015-9635cd6bac89','5d481df7-b375-4226-9a30-52fa1746a0a6','2023-07-07 00:27:11','2023-07-07 00:27:11'),('Inspiring innovation through creativity','3099368a-e852-4be6-8bd0-b17ba42e6f02','60fd4823-c93f-4cf1-a0ef-e9e5063a25d3','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Curating fashion trends since 2012','7a301f04-51a4-43c8-a588-f8104ebf33a8','6910c513-0a79-46d5-b214-83788a3264ce','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Exploring cutting-edge technology','acab5178-35dd-4bb7-9d3d-10bfe3f881f7','6d65ec45-634c-4e0f-8f49-8fd26024d382','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Promoting well-being through natural remedies','02e8f4cf-537c-45e3-916c-2620ff0a6a97','7f00c376-c5ed-4b59-b89b-7400e38121c1','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Personalized services for a memorable experience','19ab9edf-4a6c-40ae-a099-13424992e960','a963df1b-2798-4ba2-8932-952c0e17ff8b','2023-07-07 00:27:13','2023-07-07 00:27:13'),('Ethically sourced and environmentally friendly products','8154060a-be0a-4738-b238-9fa7c056ed77','b4a3fe98-a147-4db2-ae68-8f0e07cb8cda','2023-07-07 00:27:13','2023-07-07 00:27:13'),('Transforming industries with our innovations','44663478-fac6-4ab5-9808-8e7e312e2476','da971f9e-30a9-4492-89d9-3b01704386f8','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Unleashing your unique sense of style','7a301f04-51a4-43c8-a588-f8104ebf33a8','e01fdc01-f800-47d8-8d43-7adec6197bc7','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Award-winning products','4113bf98-bef4-4c5d-a015-9635cd6bac89','e0eaebde-2242-4e59-940c-53d068d46c37','2023-07-07 00:27:11','2023-07-07 00:27:11'),('Driving digital transformation','acab5178-35dd-4bb7-9d3d-10bfe3f881f7','e1321e1d-7758-428e-8785-feb30d612679','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Unparalleled luxury and comfort','19ab9edf-4a6c-40ae-a099-13424992e960','f80596c5-388b-4888-80a2-e685f12465f1','2023-07-07 00:27:13','2023-07-07 00:27:13'),('Promoting sustainable living','9f4b02ce-0d4f-46ab-8c2b-ce82ecb062a8','f912fbd1-ca24-41a3-ace4-94a31e9d399a','2023-07-07 00:27:12','2023-07-07 00:27:12');
/*!40000 ALTER TABLE `detail_points` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `works`
--

DROP TABLE IF EXISTS `works`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `works` (
  `title` varchar(128) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `image_url` varchar(128) NOT NULL,
  `brand_id` varchar(60) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `brand_id` (`brand_id`),
  CONSTRAINT `works_ibfk_1` FOREIGN KEY (`brand_id`) REFERENCES `brands` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `works`
--

LOCK TABLES `works` WRITE;
/*!40000 ALTER TABLE `works` DISABLE KEYS */;
INSERT INTO `works` VALUES ('Renewable Energy Solutions','Harness clean energy for a greener world','https://source.unsplash.com/random/800x400?renewable-energy','9f4b02ce-0d4f-46ab-8c2b-ce82ecb062a8','023c39cf-48c7-44a2-b3fa-6ab4f6748b0b','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Organic Gardening','Grow your own food sustainably','https://source.unsplash.com/random/800x400?organic-gardening','9f4b02ce-0d4f-46ab-8c2b-ce82ecb062a8','0466ee19-6e06-4e52-af95-9315db69313f','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Project Z','Creating sustainable solutions for a better future','https://source.unsplash.com/random/800x400?project-z','44663478-fac6-4ab5-9808-8e7e312e2476','08054840-1ce4-44ef-a6dc-bec2c2d8261d','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Blockchain Development','Secure and transparent decentralized solutions','https://source.unsplash.com/random/800x400?blockchain-development','acab5178-35dd-4bb7-9d3d-10bfe3f881f7','240eaa7a-1744-447f-970f-43eca90974e0','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Organic Superfoods Collection','Nourish your body with nutrient-rich superfoods','https://source.unsplash.com/random/800x400?organic-superfoods','02e8f4cf-537c-45e3-916c-2620ff0a6a97','29c608fd-987c-4f67-aa32-55c13b35be05','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Creative Writing Contest','Encouraging literary excellence','https://source.unsplash.com/random/800x400?creative-writing','3099368a-e852-4be6-8bd0-b17ba42e6f02','2e33f4df-6c13-433c-8d66-81ea28eef2dd','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Zero Waste Lifestyle','Tips and products to reduce waste','https://source.unsplash.com/random/800x400?zero-waste','9f4b02ce-0d4f-46ab-8c2b-ce82ecb062a8','31782a04-7016-4446-8bac-7ecb98bad65b','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Fall/Winter Campaign','Stay cozy and chic during the colder months','https://source.unsplash.com/random/800x400?fall-winter-campaign','7a301f04-51a4-43c8-a588-f8104ebf33a8','3eb1625a-30c9-4fe5-8fbb-caa250f369c0','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Mindfulness Meditation Program','Guided meditation for stress relief and relaxation','https://source.unsplash.com/random/800x400?meditation','c5bdc7a1-3d18-4f69-872a-b4a4441a1187','5a9ead1e-ef33-42e6-9795-ebdf4e3ed212','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Essential Oils','Experience the therapeutic benefits of pure essential oils','https://source.unsplash.com/random/800x400?essential-oils','02e8f4cf-537c-45e3-916c-2620ff0a6a97','5f954a05-ed21-4cff-b6f2-49bc3edf1ffa','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Luxury Accommodations','Experience lavish stays in our exclusive properties','https://source.unsplash.com/random/800x400?luxury-accommodations','19ab9edf-4a6c-40ae-a099-13424992e960','60975bcb-1456-4166-b004-13e1189ae122','2023-07-07 00:27:13','2023-07-07 00:27:13'),('Fine Dining Experiences','Savor exquisite cuisine prepared by renowned chefs','https://source.unsplash.com/random/800x400?fine-dining','19ab9edf-4a6c-40ae-a099-13424992e960','725e0d31-cadf-48b5-bb70-c67eebbd8946','2023-07-07 00:27:13','2023-07-07 00:27:13'),('Herbal Supplements','Unlock the healing power of herbs','https://source.unsplash.com/random/800x400?herbal-supplements','02e8f4cf-537c-45e3-916c-2620ff0a6a97','727e18cb-50a3-4728-9c49-37e549eb4fb7','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Sustainable Home Solutions','Create an eco-conscious home with our sustainable products','https://source.unsplash.com/random/800x400?sustainable-home','8154060a-be0a-4738-b238-9fa7c056ed77','7c1787ee-9a8c-4ea8-9c70-e408cf395c62','2023-07-07 00:27:13','2023-07-07 00:27:13'),('Natural Personal Care Products','Nurture yourself with organic and chemical-free essentials','https://source.unsplash.com/random/800x400?personal-care','8154060a-be0a-4738-b238-9fa7c056ed77','840c9530-9083-459f-b14f-ebfb576861b4','2023-07-07 00:27:13','2023-07-07 00:27:13'),('Art Gallery Exhibition','Showcasing diverse works of art','https://source.unsplash.com/random/800x400?art-gallery','3099368a-e852-4be6-8bd0-b17ba42e6f02','8447db53-e5c5-40ca-9847-532e5dd6aacf','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Spring Collection','Discover the freshest styles for the season','https://source.unsplash.com/random/800x400?spring-collection','7a301f04-51a4-43c8-a588-f8104ebf33a8','928f9064-46c1-4f5a-a21a-52496cb9f86a','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Product B','The next generation of high-performance devices','https://source.unsplash.com/random/800x400?product-b','4113bf98-bef4-4c5d-a015-9635cd6bac89','9f279576-712d-4e28-9255-a1591ec9cde1','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Digital Art Showcase','Exploring the intersection of art and technology','https://source.unsplash.com/random/800x400?digital-art','3099368a-e852-4be6-8bd0-b17ba42e6f02','a3848960-40b9-4b79-9c03-36464e3a187e','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Project X','Revolutionizing the way we interact with technology','https://source.unsplash.com/random/800x400?project-x','44663478-fac6-4ab5-9808-8e7e312e2476','b51e1328-c600-42d3-ae0e-11f4870f63e2','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Healthy Cooking Workshop','Learn to prepare delicious and nutritious meals','https://source.unsplash.com/random/800x400?cooking-workshop','c5bdc7a1-3d18-4f69-872a-b4a4441a1187','c31b4f78-3f2a-44b3-9d2f-dfc1fb225433','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Product A','Revolutionary product for everyday use','https://source.unsplash.com/random/800x400?product-a','4113bf98-bef4-4c5d-a015-9635cd6bac89','c96a9bd6-4bac-45b7-8c2c-33b00f53f3f2','2023-07-07 00:27:11','2023-07-07 00:27:11'),('Project Y','Breaking barriers with advanced AI solutions','https://source.unsplash.com/random/800x400?project-y','44663478-fac6-4ab5-9808-8e7e312e2476','cf18c93e-496f-4364-a939-272e4b28e0fd','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Internet of Things (IoT) Integration','Connect and automate your devices','https://source.unsplash.com/random/800x400?iot-integration','acab5178-35dd-4bb7-9d3d-10bfe3f881f7','de709e08-15d0-468f-9efc-89b7a208bfab','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Yoga Retreat','Immerse yourself in a rejuvenating yoga experience','https://source.unsplash.com/random/800x400?yoga-retreat','c5bdc7a1-3d18-4f69-872a-b4a4441a1187','e1c9aeae-8802-48b5-a7b9-715541fa431d','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Artificial Intelligence Solutions','Unlock the power of AI for your business','https://source.unsplash.com/random/800x400?ai-solutions','acab5178-35dd-4bb7-9d3d-10bfe3f881f7','ed8cedc4-4455-4b8a-9c10-0cf0771b1c65','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Summer Lookbook','Get ready for summer with our trendy outfits','https://source.unsplash.com/random/800x400?summer-lookbook','7a301f04-51a4-43c8-a588-f8104ebf33a8','f4c6a9aa-caca-4d3f-9f18-67d3b9d35fdf','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Product C','Solving complex problems with cutting-edge technology','https://source.unsplash.com/random/800x400?product-c','4113bf98-bef4-4c5d-a015-9635cd6bac89','f9469cbe-35dd-4bf3-8ad2-fc919321d38b','2023-07-07 00:27:12','2023-07-07 00:27:12'),('Reusable Lifestyle Collection','Discover eco-friendly alternatives to single-use items','https://source.unsplash.com/random/800x400?reusable-collection','8154060a-be0a-4738-b238-9fa7c056ed77','f9bb901f-c4eb-4c23-b6ee-3d4b7900e788','2023-07-07 00:27:13','2023-07-07 00:27:13'),('Spa and Wellness Retreats','Rejuvenate your mind, body, and soul in luxurious surroundings','https://source.unsplash.com/random/800x400?spa-retreats','19ab9edf-4a6c-40ae-a099-13424992e960','fbe79375-8992-48c3-98f0-466e8ff842ba','2023-07-07 00:27:13','2023-07-07 00:27:13');
/*!40000 ALTER TABLE `works` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-07  0:28:31
