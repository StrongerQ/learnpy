/*
Navicat MySQL Data Transfer

Source Server         : 666
Source Server Version : 50716
Source Host           : localhost:3306
Source Database       : authdb

Target Server Type    : MYSQL
Target Server Version : 50716
File Encoding         : 65001

Date: 2016-11-01 17:33:02
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for permission
-- ----------------------------
DROP TABLE IF EXISTS `permission`;
CREATE TABLE `permission` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `caption` varchar(32) NOT NULL,
  `module` varchar(32) DEFAULT NULL,
  `func` varchar(32) NOT NULL,
  PRIMARY KEY (`nid`),
  UNIQUE KEY `caption` (`caption`),
  UNIQUE KEY `module` (`module`,`func`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of permission
-- ----------------------------
INSERT INTO `permission` VALUES ('1', '添加用户', 'src.auth.user', 'add_user');
INSERT INTO `permission` VALUES ('2', '删除用户', 'src.auth.user', 'del_user');
INSERT INTO `permission` VALUES ('3', '添加订单', 'src.auth.order', 'add');
INSERT INTO `permission` VALUES ('4', '添加用户类型', 'src.auth.user_type', 'add_type');

-- ----------------------------
-- Table structure for user_info
-- ----------------------------
DROP TABLE IF EXISTS `user_info`;
CREATE TABLE `user_info` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `password` varchar(64) NOT NULL,
  `email` varchar(64) DEFAULT NULL,
  `find_code` char(6) DEFAULT NULL,
  `send_time` datetime DEFAULT NULL,
  `user_type_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`nid`),
  UNIQUE KEY `username` (`username`),
  KEY `email` (`email`) USING BTREE,
  KEY `user_type_id` (`user_type_id`),
  CONSTRAINT `user_info_ibfk_1` FOREIGN KEY (`user_type_id`) REFERENCES `user_type` (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_info
-- ----------------------------
INSERT INTO `user_info` VALUES ('1', 'root', '202cb962ac59075b964b07152d234b70', '424662508@qq.com', null, null, '2');
INSERT INTO `user_info` VALUES ('2', 'seven', '202cb962ac59075b964b07152d234b70', 'seven@live.com', null, null, '1');

-- ----------------------------
-- Table structure for user_type
-- ----------------------------
DROP TABLE IF EXISTS `user_type`;
CREATE TABLE `user_type` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `caption` varchar(32) NOT NULL,
  PRIMARY KEY (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_type
-- ----------------------------
INSERT INTO `user_type` VALUES ('1', '用户管理员');
INSERT INTO `user_type` VALUES ('2', '超级管理员');
INSERT INTO `user_type` VALUES ('3', '大傻叉');

-- ----------------------------
-- Table structure for user_type_to_permission
-- ----------------------------
DROP TABLE IF EXISTS `user_type_to_permission`;
CREATE TABLE `user_type_to_permission` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `user_type_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`nid`),
  UNIQUE KEY `user_type_id` (`user_type_id`,`permission_id`),
  KEY `permission_id` (`permission_id`),
  CONSTRAINT `user_type_to_permission_ibfk_1` FOREIGN KEY (`user_type_id`) REFERENCES `user_info` (`nid`),
  CONSTRAINT `user_type_to_permission_ibfk_2` FOREIGN KEY (`permission_id`) REFERENCES `permission` (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_type_to_permission
-- ----------------------------
INSERT INTO `user_type_to_permission` VALUES ('1', '1', '1');
INSERT INTO `user_type_to_permission` VALUES ('2', '1', '2');
INSERT INTO `user_type_to_permission` VALUES ('3', '2', '1');
INSERT INTO `user_type_to_permission` VALUES ('4', '2', '2');
INSERT INTO `user_type_to_permission` VALUES ('5', '2', '3');
INSERT INTO `user_type_to_permission` VALUES ('6', '2', '4');
