from flask import Flask, request, jsonify
from utils import get_sql_query, connect_to_postgres
import random

app = Flask(__name__)

@app.route('/api/receive', methods=['POST'])
def insert_post_json_to_postgres():
    json_response = request.get_json()
    print(json_response)
    # Parse input json
    ip = json_response['ip']
    ip = f'{random.randint(10, 99)}.{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}' 
    hashrate = json_response['STATS'][0]['hashrate']
    fan_speeds = json_response['STATS'][0]['fan']
    miner_type = json_response['INFO']['type']
    elapsed_time = json_response['STATS'][0]['elapsed']

    conn = connect_to_postgres()
    cur = conn.cursor()
    try:
        cur.execute(get_sql_query('sqls/select_miner_stats.sql'), (ip,))
        ip_exists = cur.fetchone()
        if ip_exists:
            cur.execute(get_sql_query('sqls/update_miner_stats.sql'), (hashrate, fan_speeds, miner_type, elapsed_time, ip))
        else:
            cur.execute(get_sql_query('sqls/insert_miner_stats.sql'), (ip, hashrate, fan_speeds, miner_type, elapsed_time))
        conn.commit()
  
    except Exception as e:
        print(f"Error: {e}")

    finally:
        cur.close()
        conn.close()
        
    return jsonify({'message': 'Data received successfully!', 'received_data': json_response})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)