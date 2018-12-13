import argparse
import datetime
import json
import logging
import os
import random
import time
import uuid

from kafka import KafkaProducer


EVENT_TEMPLATES = [
        { "eventCategory": "CC_BALANCE_PAYMENT", "eventValue": "LATE_PAYMENT", "eventSource": "CUSTOMERCARE"},
        { "eventCategory": "CC_BALANCE_PAYMENT", "eventValue": "MIN_DUE", "eventSource": "MOBLE"},
        { "eventCategory": "CC_BALANCE_PAYMENT", "eventValue": "MIN_DUE", "eventSource": "WEBSITE"},
        { "eventCategory": "CC_TRANSACTION", "eventValue": "AIRLINE_PURCHASE", "eventSource": "WEBSITE"},
        { "eventCategory": "CC_TRANSACTION", "eventValue": "MERCHANT_PURCHASE", "eventSource": "POS"},
        { "eventCategory": "CC_TRANSACTION", "eventValue": "HOTEL_PURCHASE", "eventSource": "POS"},
        { "eventCategory": "CC_TRANSACTION", "eventValue": "ONLINE_PURCHASE", "eventSource": "WEBSITE"},
        { "eventCategory": "DISPUTES", "eventValue": "CASE_CREATED", "eventSource": "IVR"},
        { "eventCategory": "DISPUTES", "eventValue": "CASE_CLOSED", "eventSource": "IVR"},
        { "eventCategory": "ONLINE_ACCOUNT", "eventValue": "PAYMENT_FAILURE", "eventSource": "CUSTOMERCARE"},
        { "eventCategory": "ONLINE_ACCOUNT", "eventValue": "PAYMENT_SUCCESS", "eventSource": "CUSTOMERCARE"},
]

def generate_event():
    #ret = {
    #    'customerAccountNumber': random.randint(1000000000000, 9000000000000),
    #    'customerGeo': 'EST',
    #    'eventId': str(uuid.uuid4()),
    #    'eventDate': datetime.datetime.now().isoformat(),
    #}
    #ret.update(EVENT_TEMPLATES[random.randint(0, 10)])
    ret = EVENT_TEMPLATES[random.randint(0, 10)]
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
        time.sleep(1.0 / int(args.rate))
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
