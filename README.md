# client_server_response
The project contains next topics airflow, socket, multithreading, postgres etc.

1) The surveyor server server asks miners to send JSON 
(poll_miner.py)
2) Miners sends the JSON to the server 
(mainer_server.py)
3) The surveyor server gets the JSON and sends to Google Cloud Server 
(poll_miner.py)
4) Main server get POST request, parses the JSON and inserts JSON data into miner_stats table in Postgres 
(insert_post_json_to_postgres.py)
5) Main server aggregates the data in miner_stats table in Postgres
 and insert it into miner_type_summary table in Postgres 
 (calculate_sum_hashrate.py)
6) Steps 1-4 are executed by poll_mainer_dag.py every 2 minutes
(poll_mainer_dag.py)
7) Step 5 executed by calculate_sum_hashrate_dag every 5 minutes
(calculate_sum_hashrate_dag.py)