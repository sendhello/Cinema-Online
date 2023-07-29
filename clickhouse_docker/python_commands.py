from clickhouse_driver import Client

client = Client(host='localhost')
client.execute('SHOW DATABASES')
client.execute(
    'CREATE DATABASE IF NOT EXISTS example ON CLUSTER company_cluster'
)
client.execute(
    'CREATE TABLE example.regular_table ON CLUSTER company_cluster (id Int64, x Int32) Engine=MergeTree() ORDER BY id'
)
client.execute(
    'INSERT INTO example.regular_table (id, x) VALUES (1, 10), (2, 20)'
)
client.execute('SELECT * FROM example.regular_table')
client.execute(
    'INSERT INTO default.test (id, event_time) VALUES (1, today()), (2, today()), (3, now())'
)
client.execute('SELECT * FROM default.test')
