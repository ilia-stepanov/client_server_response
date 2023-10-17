CREATE TABLE IF NOT EXISTS miner_stats (
    ip VARCHAR(15) PRIMARY KEY,
    hashrate DECIMAL(10, 2),
    fan_speeds INT[],
    miner_type VARCHAR(50),
    elapsed_time INT
);


CREATE INDEX ip_index ON miner_stats (ip);