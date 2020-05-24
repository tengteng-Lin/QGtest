drop database if EXISTS QG_11

use QG_11;


create table triple3(
    `dataset_local_id` INTEGER NOT NULL ,
    `triple_id` INTEGER NOT NULL ,
    `subject` INTEGER NOT NULL ,
    `predicate` INTEGER NOT NULL ,
    `object` INTEGER NOT NULL ,
    PRIMARY KEY (`triple_id`),
)engine=innodb DEFAULT charset=utf8;

create table uri_label_id3(
    `dataset_local_id` INTEGER NOT NULL ,
    `id` INTEGER NOT NULL ,
    `is_literal` INTEGER NOT NULL ,
    `uri` VARCHAR (40) ,
    `label` VARCHAR (20),
    PRIMARY KEY (`id`),
)engine=innodb DEFAULT charset=utf8;

-- create table dataset3(
--     `local_id` INTEGER NOT NULL ,
--     ``
--
-- )engine=innodb DEFAULT charset=utf8;

