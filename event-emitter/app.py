import argparse
import json
import logging
import os
import random
import time
import uuid

from kafka import KafkaProducer


EVENTS = [
    'event_type_1',
    'event_type_2',
    'event_type_3',
    'event_type_4'
]


def generate_event():
    ret = {
        'user_id': random.randint(1000, 2000),
        'event_type': EVENTS[random.randint(0, 3)],
        'event_id': str(uuid.uuid4())
    }
    return ret


def main(args):
    logging.info('brokers={}'.format(args.brokers))
    logging.info('topic={}'.format(args.topic))
    logging.info('rate={}'.format(args.rate))

    logging.info('creating kafka producer')
    producer = KafkaProducer(bootstrap_servers=args.brokers)

    logging.info('begin sending events')
    while True:
        producer.send(args.topic, json.dumps(generate_event()).encode())
        time.sleep(1.0 / args.rate)
    logging.info('end sending events')


def get_arg(env, default):
    return os.getenv(env) if os.getenv(env, '') is not '' else default


def parse_args(parser):
    args = parser.parse_args()
    args.brokers = get_arg('KAFKA_BROKERS', args.brokers)
    args.topic = get_arg('KAFKA_TOPIC', args.topic)
    args.rate = get_arg('RATE', args.rate)
    return args


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info('starting kafka-openshift-python emitter')
    parser = argparse.ArgumentParser(description='emit some stuff on kafka')
    parser.add_argument(
            '--brokers',
            help='The bootstrap servers, env variable KAFKA_BROKERS',
            default='localhost:9092')
    parser.add_argument(
            '--topic',
            help='Topic to publish to, env variable KAFKA_TOPIC',
            default='bones-brigade')
    parser.add_argument(
            '--rate',
            type=int,
            help='Lines per second, env variable RATE',
            default=3)
    args = parse_args(parser)
    main(args)
    logging.info('exiting')
