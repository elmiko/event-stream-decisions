# event emitter
A Python source-to-image application for emitting to an Apache Kafka topic

## Launching on OpenShift

```
oc new-app centos/python-36-centos7~https://github.com/elmiko/event-stream-decisions \
  --context-dir event-emitter \
  -e KAFKA_BROKERS=kafka:9092 \
  -e KAFKA_TOPIC=events \
  -e RATE=1 \
  --name=emitter
```

You will need to adjust the `KAFKA_BROKERS` and `KAFKA_TOPICS` variables to
match your configured Kafka deployment and desired topic. The `RATE` variable
controls how many messages per second the emitter will send, by default this
is set to 3.
