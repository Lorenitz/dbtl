-- Assert that dim_hello only contains people.
-- Therefore, this query should return 0 rows.
select * from dim_hello_girls 
where gender not in('F', 'M')
