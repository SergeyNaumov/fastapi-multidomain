CREATE USER 'svcms'@'localhost' IDENTIFIED BY '';
grant all privileges on svcms.* to svcms@localhost;
CREATE TABLE `project` (
  `project_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `header` varchar(255) CHARACTER SET cp1251 NOT NULL DEFAULT '',
  `options` text CHARACTER SET cp1251 NOT NULL,
  `registered` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `city` int(10) unsigned NOT NULL DEFAULT '0',
  `otrasl_id` int(11) DEFAULT NULL,
  `files_size` varchar(100) CHARACTER SET cp1251 NOT NULL DEFAULT '',
  `template_size` varchar(100) CHARACTER SET cp1251 NOT NULL DEFAULT '',
  `enabled` tinyint(1) unsigned NOT NULL DEFAULT '1',
  `server_type` tinyint(1) NOT NULL DEFAULT '3' COMMENT '1-CGI; 2-FACTCGI; 3-PSGI; 4-Python FastAPI',
  `comment` varchar(512) NOT NULL DEFAULT '',
  PRIMARY KEY (`project_id`),
  KEY `enabled` (`enabled`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

CREATE TABLE `domain` (
  `domain_id` int unsigned NOT NULL AUTO_INCREMENT,
  `domain` varchar(200) CHARACTER SET cp1251 NOT NULL DEFAULT '',
  `template_id` int(11) NOT NULL DEFAULT '0',
  `project_id` int(10) unsigned DEFAULT NULL,
  `dns_serial` bigint(20) unsigned NOT NULL DEFAULT '2017050915',
  `dns_enabled` tinyint(1) NOT NULL DEFAULT '1',
  `is_ssl` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '0 - not ssl ; 1 - paid_ssl ; 3 - lets encrypt',
  `lets_encrypt_status` tinyint(3) unsigned NOT NULL DEFAULT '0',
  `paid_till` date NOT NULL DEFAULT '0000-00-00',
  `last_paid_till_update` date NOT NULL DEFAULT '0000-00-00',
  `our_domain` tinyint(1) NOT NULL DEFAULT '0',
  `not_cache_nginx` tinyint(4) NOT NULL DEFAULT '0',
  `server_type` tinyint(1) NOT NULL DEFAULT '3' COMMENT '1-CGI; 2-FACTCGI; 3-PSGI',
  `need_clean_cache` tinyint(1) NOT NULL DEFAULT '0' COMMENT 'Нужно очистить кэш',
  `is_adaptive` tinyint(4) NOT NULL DEFAULT '0' COMMENT '1 - да ; 2 - нет',
  PRIMARY KEY (`domain_id`),
  UNIQUE KEY `domain` (`domain`),
  KEY `project_id` (`project_id`),
  KEY `dns_enabled` (`dns_enabled`),
  KEY `need_clean_cache` (`need_clean_cache`),
  CONSTRAINT `domain_ibfk_1` FOREIGN KEY (`project_id`) REFERENCES `project` (`project_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;


CREATE TABLE `template` (
  `template_id` int unsigned NOT NULL AUTO_INCREMENT,
  `folder` varchar(255) CHARACTER SET cp1251 NOT NULL DEFAULT '',
  `type` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `header` varchar(200) CHARACTER SET cp1251 NOT NULL DEFAULT '',
  `options` text CHARACTER SET cp1251 NOT NULL,
  `max_cache_time` int(10) unsigned NOT NULL DEFAULT '0',
  `reset_cache_time` int(10) unsigned NOT NULL DEFAULT '0',
  `not_cache_nginx` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`template_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

replace into project(project_id,header,server_type,options) values('1','site1.test',4,'');
replace into project(project_id,header,server_type,options) values('2','site2.test',4,'');

replace into template(template_id,folder,header,options) values('1','site1_test','site1.test','');
replace into template(template_id,folder,header,options) values('2','site2_test','site2.test','');

replace into domain(domain_id,domain,project_id,template_id) values(1,'site1.test',1,1);
replace into domain(domain_id,domain,project_id,template_id) values(2,'site2.test',2,2);

drop table struct_1_news;
create table struct_1_news(
  id int unsigned primary key AUTO_INCREMENT,
  header varchar(255) not null default '',
  type tinyint unsigned not null default '0',
  anons varchar(512) not null default '',
  body text,
  photo varchar(20) not null default '',
  registered timestamp
) engine=innodb default charset=utf8;

REPLACE INTO struct_1_news(id,header,anons,body,photo,registered,type)
values(1,'Новость1','анонс новости','текст новости','pic1.jpg','2019-03-12',1),
(2,'Новость2','анонс новости','текст новости','pic2.jpg','2019-06-22',2),
(3,'Новость3','анонс новости','текст новости','pic3.jpg','2020-01-17',3),
(4,'Новость4','анонс новости','текст новости','pic4.jpg','2020-09-15',2);