# Date
Before 24-10-2023
# What's going on
I have free trial Google Cloud. Using GC I've created 4 VMs. 2 of them have low CPU and storage. Other 2 are much stronger.
The first couple (miners) is for sending JSON data to the 3rd VM (Pooler or Surveyor). The Surveyor has a simple socket connector with the miners. Through socket connector it sends word 'stat' and gets JSON data as a response.
Then the Surveyor sends data from POST method to the 4th VM (main server) which has Flask API and gets POST request from the Surveyor. The main server puts the JSON data in Postgres. The whole process happens every 2 mins and scheduled in Airflow.
There is an analytical table on top of JSON data table. This table is updated every 5 mins through Airflow as well.
On top of Postgres there is Grafana which visualize this analytical table.


# Date:
24-10-2023
# What's going on
Started implementing the idea of testing the program using thousands of docker containers. Using free trial Google Cloud VMs I'm going to create 50000 docker containers for 2 strong VMs (25k each). Both VMs will be Kafka Producers. Apart from them there is another VM which will be Kafka brocker and Kafka consumer at the same time.

Today I installed Kafka and tested it without Docker. Started doing it with Docker there are some issues which I will fix tomorrow.


# Date:		
25-10-2023
# What's going on
I decided to keep non docker way for now to test kafka

This is local non Docker way how kafka was installed and works:
749  sudo apt-get update
750  sudo apt-get upgrade
751  sudo apt-get install openjdk-11-jdk
768  wget https://downloads.apache.org/kafka/3.6.0/kafka_2.13-3.6.0.tgz
769  tar -xzf kafka_2.13-3.6.0.tgz 
771  cd kafka_2.13-3.6.0/
773  nohup bin/zookeeper-server-start.sh config/zookeeper.properties > zookeper_output.log 2>&1 &
775  nohup bin/kafka-server-start.sh config/server.properties > kafka_output.log 2>&1 &
776  bin/kafka-topics.sh --create --topic test --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

777  ./bin/kafka-topics.sh --list --bootstrap-server=localhost:9092

778  bin/kafka-console-producer.sh --topic test --bootstrap-server localhost:9092
788  bin/kafka-console-consumer.sh --topic test --bootstrap-server localhost:9092 --from-beginning

Also I create kafka_producer for miner servers and I make create_response function separate because it's used now in 2 different scripts.


# Date:		
26-10-2023
# What's going on
Started thinking about time series DB like InfluxDB, Prometheus etc. (examples https://www.reddit.com/r/MoneroMining/comments/d684pi/xmrig_mining_monitoring_with_prometheus_grafana/
https://github.com/jouir/mining-dashboards
https://github.com/MrClappy/MinerDashboards
)

Also instead of creating thousands of dockers I can use multithreading for python Kafka consumer for testing purposes.


# Date:		
28-10-2023
# What's going on
Started implementing the next idea: kafka gets data from miners -> Python through Kafka API (confluent_kafka) process this data and checks alert event -> Python writes this data into analytical DB. Another approch is Flink which is much simpler scalable.
