from flask import Flask, request, jsonify #, render_template
import psycopg2
import json
from get_sql_query import get_sql_query

app = Flask(__name__)

@app.route('/api/receive', methods=['POST'])
def insert_post_json_to_postgres():
    json_response = request.get_json()
    print(json_response)
    # Parse input json
    ip = json_response['ip']
    hashrate = json_response['STATS'][0]['hashrate']
    fan_speeds = json_response['STATS'][0]['fan']
    miner_type = json_response['INFO']['type']
    elapsed_time = json_response['STATS'][0]['elapsed']

    # Connect to postgres
    conn = psycopg2.connect(
        database='postgres',
        user='postgres',
        password='postgres',
        host='localhost', 
        port='5432')

    cur = conn.cursor()
    try:
        # select ip in miner_stats table
        select_miner_stats = get_sql_query('sqls/select_miner_stats.sql')
        cur.execute(select_miner_stats, (ip,))
        ip_exists = cur.fetchone()

        # check if ip exists in miner_stats table: exist - update else - insert
        if ip_exists:
            update_miner_stats = get_sql_query('sqls/update_miner_stats.sql')
            cur.execute(update_miner_stats, (hashrate, fan_speeds, miner_type, elapsed_time, ip))
        else:
            insert_miner_stats = get_sql_query('sqls/insert_miner_stats.sql')
            cur.execute(insert_miner_stats, (ip, hashrate, fan_speeds, miner_type, elapsed_time))

        conn.commit()
  
    except Exception as e:
        print(f"Error: {e}")

    finally:
        cur.close()
        conn.close()
        
    return jsonify({'message': 'Data received successfully!', 'received_data': json_response})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)