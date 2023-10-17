UPDATE miner_stats 
SET hashrate = %s, fan_speeds = %s, miner_type = %s, elapsed_time = %s 
WHERE ip = %s;