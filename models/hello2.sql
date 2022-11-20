create table if not exists hello2 (
    name varchar(40),
    gender varchar(1)
);
delete from hello2;
insert into hello2 values 
            ('Julia', 'F'), ('Adria', 'M'), ('Debora', 'F');