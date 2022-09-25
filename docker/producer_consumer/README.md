## Producer and Consumer as Containers
The app has 3 images:
* Rabbitmq
* Producer
* Consumer


## How to run
Build images for producer and consumer
```shell
docker build -t simple_consumer consumer
docker build -t simple_producer producer
```
and then run the docker compose
```shell
docker-compose up
```

the messages can be seen in the logs of the simple_consumer container.