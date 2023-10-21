from utils import get_sql_query, connect_to_postgres

def calculate_sum_hashrate():

    conn = connect_to_postgres()
    cur = conn.cursor()

    try:
        cur.execute(get_sql_query('sqls/select_sum_hashrate.sql'))
        results = cur.fetchall()
        insert_miner_type_summary = get_sql_query('sqls/insert_miner_type_summary.sql')
        for miner_type, sum_hashrate in results:
            cur.execute(insert_miner_type_summary, (sum_hashrate, miner_type))
        conn.commit()    
    except Exception as e:
        print(f"Error: {e}")

    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    calculate_sum_hashrate()
