import psycopg2
import json
from get_sql_query import get_sql_query


def calculate_sum_hashrate():

    # Connect to postgres
    conn = psycopg2.connect(
        database='postgres',
        user='postgres',
        password='postgres',
        host='localhost', 
        port='5432')

    cur = conn.cursor()
    try:
        select_sum_hashrate = get_sql_query('sqls/select_sum_hashrate.sql')
        cur.execute(select_sum_hashrate)
        results = cur.fetchall()

        # Insert result in miner_type_summary table
        insert_miner_type_summary = get_sql_query('sqls/insert_miner_type_summary.sql')
        for miner_type, sum_hashrate in results:
            cur.execute(insert_miner_type_summary, (sum_hashrate, miner_type))
        conn.commit()    
    except Exception as e:
        print(f"Error: {e}")

    finally:
        cur.close()
        conn.close()

