create or replace view dim_hello_girls as
    select * from hello	--where gender='F'
    union all
    select * from hello2 --where gender='F'
   