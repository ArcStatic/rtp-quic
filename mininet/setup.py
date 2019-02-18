from mininet.topo import Topo
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.net import Mininet
from mininet.log import lg, info
from mininet.util import dumpNodeConnections
from mininet.cli import CLI
import sys
import os.path
from subprocess import call
import time

#mininet setup script based on original script written by Stephen McQuistin:
#https://github.com/lumisota/ifip-otcs-hollywood/blob/master/evaluations/perf-voip-adsl.py

class DumbbellTopo(Topo):
    def build(self, bw=8, delay="0ms"):
        #delay = ""
        #queue_size = 0
        #if sys.argv[1].split('-')[2] == "uk":
        delay = "10ms"
        queue_size = 14
        #elif sys.argv[1].split('-')[2] == "us":
            #delay = "35ms"
            #queue_size = 48
        print delay, queue_size
        switch1 = self.addSwitch('switch1')
        switch2 = self.addSwitch('switch2')
        appClient = self.addHost('aClient')
        appServer = self.addHost('aServer')
        #crossClient = self.addHost('cClient')
        #crossServer = self.addHost('cServer')
        self.addLink(appClient, switch1)
        #self.addLink(crossClient, switch1)
        self.addLink(appServer, switch2)
        #self.addLink(crossServer, switch2)
        self.addLink(switch1, switch2, bw=bw, delay=delay, max_queue_size=queue_size)

def quic_exchange():
    dumbbell = DumbbellTopo()
    network = Mininet(topo=dumbbell, host=CPULimitedHost, link=TCLink, autoPinCpus=True)
    network.start()
    dumpNodeConnections(network.hosts)
    network.pingAll()
    
    #crossClient = network.get('cClient')
    #crossServer = network.get('cServer')
    appClient = network.get('aClient')
    appServer = network.get('aServer')

    # disable offloading - when enabled, permits segments larger than 1500 bytes
    #crossClient.cmd('ethtool -K ' + str(crossClient.intf()) + ' gso off')
    #crossServer.cmd('ethtool -K ' + str(crossServer.intf()) + ' gso off')
    appClient.cmd('ethtool -K ' + str(appClient.intf()) + ' gso off')
    appServer.cmd('ethtool -K ' + str(appServer.intf()) + ' gso off')

    #appClient.cmd('echo `ping', appServer.IP(), ' > vagrant_data/client-sent-ping`')
    #appServer.cmd('echo `ping', appClient.IP(), ' > vagrant_data/server-sent-ping`')
    
    #appServer.cmd('./vagrant/quiche/examples/server ', appServer.IP(), ' 5006 >> vagrant_data/quic-server')
    #for i in range(5):
        #appClient.cmd('./vagrant/quiche/examples/client ', appServer.IP(), ' 5006 >> vagrant_data/quic-client')
        #time.sleep(1)
    appServer.cmd('./home/vagrant/ngtcp2/examples/server ', appServer.IP(), ' 5006')
    #for i in range(5):
    appClient.cmd('./home/vagrant/ngtcp2/examples/client ', appServer.IP(), ' 5006')
    time.sleep(1)
    
    network.stop()
    time.sleep(5)

if __name__ == '__main__':
    quic_exchange()
