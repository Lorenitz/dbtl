create or replace view dim_hello as
    select * from hello	
    union all
    select * from hello2; 