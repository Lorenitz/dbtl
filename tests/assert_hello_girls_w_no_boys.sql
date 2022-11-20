-- Assert that dim_hello only contains girls.
-- Therefore, this query should return 0 rows.
select * from dim_hello_girls 
where gender <> 'F'
