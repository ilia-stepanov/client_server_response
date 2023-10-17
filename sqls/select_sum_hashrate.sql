SELECT miner_type, SUM(hashrate) 
FROM miner_stats
GROUP BY miner_type;