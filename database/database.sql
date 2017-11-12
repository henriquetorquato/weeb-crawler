-- MySQL Script generated by MySQL Workbench
-- Sun Nov 12 20:20:49 2017
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
CREATE DATABASE IF NOT EXISTS `weeb_crawler` DEFAULT CHARACTER SET utf8 ;
USE `weeb_crawler` ;

-- -----------------------------------------------------
-- Table `weeb_crawler`.`manga`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `weeb_crawler`.`manga` ;

CREATE TABLE IF NOT EXISTS `weeb_crawler`.`manga` (
  `id` INT NOT NULL,
  `muID` VARCHAR(6) NOT NULL,
  `release_year` CHAR(4) NOT NULL,
  `official_title` VARCHAR(250) NOT NULL,
  `available` TINYINT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  UNIQUE INDEX `official_title_UNIQUE` (`official_title` ASC),
  UNIQUE INDEX `muID_UNIQUE` (`muID` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `weeb_crawler`.`titles`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `weeb_crawler`.`titles` ;

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
DROP TABLE IF EXISTS `weeb_crawler`.`authors` ;

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
DROP TABLE IF EXISTS `weeb_crawler`.`artists` ;

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
-- Table `weeb_crawler`.`status_tags`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `weeb_crawler`.`status_tags` ;

CREATE TABLE IF NOT EXISTS `weeb_crawler`.`status_tags` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tag_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `tag_name_UNIQUE` (`tag_name` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `weeb_crawler`.`manga_status_tags`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `weeb_crawler`.`manga_status_tags` ;

CREATE TABLE IF NOT EXISTS `weeb_crawler`.`manga_status_tags` (
  `status_tags_id` INT NOT NULL,
  `manga_id` INT NOT NULL,
  `state` TINYINT NOT NULL,
  PRIMARY KEY (`status_tags_id`, `manga_id`),
  INDEX `fk_status_tags_has_manga_manga1_idx` (`manga_id` ASC),
  INDEX `fk_status_tags_has_manga_status_tags1_idx` (`status_tags_id` ASC),
  CONSTRAINT `fk_status_tags_has_manga_status_tags1`
    FOREIGN KEY (`status_tags_id`)
    REFERENCES `weeb_crawler`.`status_tags` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_status_tags_has_manga_manga1`
    FOREIGN KEY (`manga_id`)
    REFERENCES `weeb_crawler`.`manga` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `weeb_crawler`.`gender_tags`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `weeb_crawler`.`gender_tags` ;

CREATE TABLE IF NOT EXISTS `weeb_crawler`.`gender_tags` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tag_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `weeb_crawler`.`manga_gender_tags`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `weeb_crawler`.`manga_gender_tags` ;

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
-- Table `weeb_crawler`.`volumes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `weeb_crawler`.`volumes` ;

CREATE TABLE IF NOT EXISTS `weeb_crawler`.`volumes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(200) NOT NULL,
  `manga_id` INT NOT NULL,
  PRIMARY KEY (`id`, `manga_id`),
  INDEX `fk_volumes_manga1_idx` (`manga_id` ASC),
  CONSTRAINT `fk_volumes_manga1`
    FOREIGN KEY (`manga_id`)
    REFERENCES `weeb_crawler`.`manga` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `weeb_crawler`.`chapters`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `weeb_crawler`.`chapters` ;

CREATE TABLE IF NOT EXISTS `weeb_crawler`.`chapters` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `number` VARCHAR(10) NOT NULL,
  `title` VARCHAR(150) NOT NULL,
  `volumes_id` INT NOT NULL,
  `manga_id` INT NOT NULL,
  PRIMARY KEY (`id`, `volumes_id`, `manga_id`),
  INDEX `fk_chapters_volumes1_idx` (`volumes_id` ASC, `manga_id` ASC),
  CONSTRAINT `fk_chapters_volumes1`
    FOREIGN KEY (`volumes_id` , `manga_id`)
    REFERENCES `weeb_crawler`.`volumes` (`id` , `manga_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `weeb_crawler`.`cover`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `weeb_crawler`.`cover` ;

CREATE TABLE IF NOT EXISTS `weeb_crawler`.`cover` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `url` VARCHAR(200) NOT NULL,
  `width` INT NOT NULL,
  `height` INT NOT NULL,
  `volumes_id` INT NOT NULL,
  `manga_id` INT NOT NULL,
  PRIMARY KEY (`id`, `volumes_id`, `manga_id`),
  INDEX `fk_cover_volumes1_idx` (`volumes_id` ASC, `manga_id` ASC),
  CONSTRAINT `fk_cover_volumes1`
    FOREIGN KEY (`volumes_id` , `manga_id`)
    REFERENCES `weeb_crawler`.`volumes` (`id` , `manga_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
