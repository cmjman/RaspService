import sys
sys.path.append('..')
from sensors.dht11 import DHT11

if __name__ == '__main__':
    dht11 = DHT11()   
    dht11.getOutput()
