drop database db_poo;

create database db_poo;

use db_poo;

CREATE TABLE usuario (
  id int(5) NOT NULL primary key auto_increment,
  codigo varchar(50) NOT NULL,
  nombre varchar(50) NOT NULL,
  username varchar(50) NOT NULL,
  clave varchar(50) NOT NULL,
  tipo varchar(50) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=latin1;