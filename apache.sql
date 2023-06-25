create database Apache_logs;
use Apache_logs;

Create table access_logs 
(          
         id INT PRIMARY KEY AUTO_INCREMENT,
                ip_address VARCHAR(255),
                datee  varchar(25) not null,
                timee varchar(25) not null,
                request_method VARCHAR(255) not null,
                request_uri VARCHAR(1024) not null,
                http_version VARCHAR(255) not null,
                status_code VARCHAR(255) not null,
                byte_count varchar(255) not null
                
                
        
);
drop table access_logs;
select * from access_logs