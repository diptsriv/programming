from confluent_kafka import Producer


p = Producer({'bootstrap.servers' : 'ns3080240.ip-145-239-0.eu:9092'})


try:
    for val in xrange(1,1000):
        p.produce('dip_topic', 'myvalue #{0}' .format(val))

        p.poll(0.5)

except KeyboardInterrupt:
    pass


p.flush(30)
