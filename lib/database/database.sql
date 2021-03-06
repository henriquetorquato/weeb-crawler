-- MySQL Script generated by MySQL Workbench
-- Sun Nov 19 20:45:28 2017
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema weeb_crawler
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema weeb_crawler
-- -----------------------------------------------------
CREATE DATABASE IF NOT EXISTS `weeb_crawler` DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
USE `weeb_crawler` ;

-- -----------------------------------------------------
-- Table `weeb_crawler`.`manga`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `weeb_crawler`.`manga` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `muID` VARCHAR(6) NULL,
  `page_url` VARCHAR(200) NOT NULL,
  `release_year` CHAR(4) NULL,
  `official_title` VARCHAR(250) NOT NULL,
  `description` VARCHAR(2000) NOT NULL,
  `status` VARCHAR(45) NOT NULL,
  `available` TINYINT NOT NULL,
  `rank` INT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  UNIQUE INDEX `official_title_UNIQUE` (`official_title` ASC),
  UNIQUE INDEX `page_url_UNIQUE` (`page_url` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `weeb_crawler`.`titles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `weeb_crawler`.`titles` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(150) NOT NULL,
  `manga_id` INT NOT NULL,
  PRIMARY KEY (`id`, `manga_id`),
  INDEX `fk_Titles_manga_idx` (`manga_id` ASC),
  CONSTRAINT `fk_Titles_manga`
    FOREIGN KEY (`manga_id`)
    REFERENCES `weeb_crawler`.`manga` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `weeb_crawler`.`authors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `weeb_crawler`.`authors` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(150) NOT NULL,
  `manga_id` INT NOT NULL,
  PRIMARY KEY (`id`, `manga_id`),
  INDEX `fk_authors_manga1_idx` (`manga_id` ASC),
  CONSTRAINT `fk_authors_manga1`
    FOREIGN KEY (`manga_id`)
    REFERENCES `weeb_crawler`.`manga` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `weeb_crawler`.`artists`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `weeb_crawler`.`artists` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `manga_id` INT NOT NULL,
  PRIMARY KEY (`id`, `manga_id`),
  INDEX `fk_artists_manga1_idx` (`manga_id` ASC),
  CONSTRAINT `fk_artists_manga1`
    FOREIGN KEY (`manga_id`)
    REFERENCES `weeb_crawler`.`manga` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `weeb_crawler`.`gender_tags`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `weeb_crawler`.`gender_tags` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tag_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `tag_name_UNIQUE` (`tag_name` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `weeb_crawler`.`manga_gender_tags`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `weeb_crawler`.`manga_gender_tags` (
  `gender_tags_id` INT NOT NULL,
  `manga_id` INT NOT NULL,
  PRIMARY KEY (`gender_tags_id`, `manga_id`),
  INDEX `fk_gender_tags_has_manga_manga1_idx` (`manga_id` ASC),
  INDEX `fk_gender_tags_has_manga_gender_tags1_idx` (`gender_tags_id` ASC),
  CONSTRAINT `fk_gender_tags_has_manga_gender_tags1`
    FOREIGN KEY (`gender_tags_id`)
    REFERENCES `weeb_crawler`.`gender_tags` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_gender_tags_has_manga_manga1`
    FOREIGN KEY (`manga_id`)
    REFERENCES `weeb_crawler`.`manga` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `weeb_crawler`.`chapter`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `weeb_crawler`.`chapter` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `number` VARCHAR(50) NOT NULL,
  `chapter_url` VARCHAR(200) NOT NULL,
  `all_pages` TINYINT NULL,
  `manga_id` INT NOT NULL,
  PRIMARY KEY (`id`, `manga_id`),
  INDEX `fk_chapters_manga1_idx` (`manga_id` ASC),
  CONSTRAINT `fk_chapters_manga1`
    FOREIGN KEY (`manga_id`)
    REFERENCES `weeb_crawler`.`manga` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `weeb_crawler`.`cover`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `weeb_crawler`.`cover` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `url` VARCHAR(200) NOT NULL,
  `width` INT NOT NULL,
  `height` INT NOT NULL,
  `manga_id` INT NOT NULL,
  PRIMARY KEY (`id`, `manga_id`),
  INDEX `fk_cover_manga1_idx` (`manga_id` ASC),
  CONSTRAINT `fk_cover_manga1`
    FOREIGN KEY (`manga_id`)
    REFERENCES `weeb_crawler`.`manga` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `weeb_crawler`.`page`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `weeb_crawler`.`page` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `img_url` VARCHAR(200) NOT NULL,
  `chapter_id` INT NOT NULL,
  `manga_id` INT NOT NULL,
  PRIMARY KEY (`id`, `chapter_id`, `manga_id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  INDEX `fk_page_chapter1_idx` (`chapter_id` ASC, `manga_id` ASC),
  CONSTRAINT `fk_page_chapter1`
    FOREIGN KEY (`chapter_id` , `manga_id`)
    REFERENCES `weeb_crawler`.`chapter` (`id` , `manga_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
