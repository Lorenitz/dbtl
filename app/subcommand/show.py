def show_details():
    details= """prod warehouse:
  redshift: examplecluster.abc123xyz789.us-west-1.redshift.amazonaws.com
  dbname:   bookshop

test warehouse:
  postgres: localhost
  dbname:   bookshop

sql files:
  models/lorem.sql
  models/ipsum.sql
  models/dolor.sql
 """
        
    print(details)