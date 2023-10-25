import time
from datetime import datetime
import random

def create_response():
	response = {
      "STATUS": {
            "STATUS": "S",
            "when": int(time.time()),
            "Msg": "stats",
            "api_version": "1.0.0"},
      "INFO": {"miner_version": "uart_trans.1.3",
               "CompileTime": f"{str(datetime.now().strftime('%A, %B %d, %Y at %I:%M:%S %p'))}",
               "type": f"Antminer S{random.randint(1, 1000)} XP"},
      "STATS": [{"elapsed": random.randint(1, 1000),
            "hashrate": float(random.randint(50000, 1000000)),
			"rate_30m": float(random.randint(100000, 500000)),
			"rate_avg": float(random.randint(100000, 500000)),
			"rate_ideal": 141000.0,
			"rate_unit": "GH/s",
            "chain_num": 3,
            "fan_num": 4,
            "fan": [6000, 6000, 6000, 6000],             
            "hwp_total": 0.0,
            "miner-mode": 0,
            "freq-level": 100}]}
	return response