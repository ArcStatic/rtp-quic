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
        delay = "50ms"
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
    #appServer.cmd('./ngtcp2/examples/server -b 3 -t 0.1 -l 100 -i 3000 -q -f 60 ' + appServer.IP() + ' 5004 ngtcp2/test-ca/rsa/ca.key ngtcp2/test-ca/rsa/ca.cert > ngtcp2/datasets/PARTIAL_3B_10L_100F_2000D_60R_server.txt &')
    #pid = int( appServer.cmd('./ngtcp2/examples/server -b 3 -t 0.1 -l 100 -i 3000 -q -f 60 ' + appServer.IP() + ' 5004 ngtcp2/test-ca/rsa/ca.key ngtcp2/test-ca/rsa/ca.cert > ngtcp2/datasets/PARTIAL_3B_10L_18000F_2000D_60R_server.txt') )
    #appServer.cmd('wait', pid)
    
    
    #appServer.cmd('./home/mininet/quic_data/mininet/ngtcp2/examples/server -b 3 -t 0.1 -l 100 -i 3000 -q -f 60 ', appServer.IP(), ' 5004 ../test-ca/rsa/ca.key test-ca/rsa/ca.cert')
    #appServer.cmd('echo "hi" >> foo.txt')
    #appServer.cmd('sudo ./ngtcp2/datasets/generate_data_server.sh ' + appServer.IP() + ' &')
    #print("server command run")
    #print('sudo ./ngtcp2/datasets/generate_data_server.sh ' + appServer.IP() + ' &')
    
    #appServer.cmd('./ngtcp2/examples/server -b 3 -l 18000 -i 3000 -q -f 60 ', appServer.IP(), ' 5004 ngtcp2/test-ca/rsa/ca.key ngtcp2/test-ca/rsa/ca.cert > ngtcp2/datasets/PARTIAL_3B_0L_18000F_2000D_60R_server.txt &')
    
    
    
    #for i in range(5):
    #appClient.cmd('./ngtcp2/examples/client -b 3 -e -a 3000 -q ' + appServer.IP() + ' 5004 > ngtcp2/datasets/PARTIAL_3B_0L_100F_2000D_60R_client.txt')
    #pid = int( appClient.cmd('./ngtcp2/examples/client -b 3 -e -a 3000 -q ' + appServer.IP() + ' 5004 > ngtcp2/datasets/PARTIAL_3B_10L_18000F_2000D_60R_client.txt') )
    #appClient.cmd('wait', pid)
    
    #appClient.cmd('./home/mininet/quic_data/mininet/ngtcp2/examples/client -b 3 -e -a 3000 -q', appServer.IP(), ' 5004')
    #print('sudo ./ngtcp2/datasets/generate_data_client.sh ' + appServer.IP() + ' &')
    #appClient.cmd('sudo ./ngtcp2/datasets/generate_data_client.sh ' + appServer.IP() + ' &')
    #print("client command run")
    
    #appClient.cmd('./ngtcp2/examples/client -b 3 -e -a 3000 -q ', appServer.IP(), ' 5004 > ngtcp2/datasets/PARTIAL_3B_0L_18000F_2000D_60R_client.txt')
    
    

    
    #3% loss, partial
    #################################
    appServer.cmd('./ngtcp2/examples/server -b 3 -t 0.03 -l 18000 -i 3000 -q -f 60 ', appServer.IP(), ' 5004 ngtcp2/test-ca/rsa/ca.key ngtcp2/test-ca/rsa/ca.cert > ngtcp2/datasets/PARTIAL_3B_03L_18000F_2000D_60R_server.txt &')
    
    appClient.cmd('./ngtcp2/examples/client -b 3 -e -a 3000 -q ', appServer.IP(), ' 5004 > ngtcp2/datasets/PARTIAL_3B_03L_18000F_2000D_60R_client.txt')
    
    time.sleep(20)
    ################################

    
    #3% loss, reliable
    #################################
    appServer.cmd('./ngtcp2-reliable/examples/server -b 3 -t 0.03 -l 18000 -i 3000 -q -f 60 ', appServer.IP(), ' 5004 ngtcp2-reliable/test-ca/rsa/ca.key ngtcp2-reliable/test-ca/rsa/ca.cert > ngtcp2/datasets/RELIABLE_3B_03L_18000F_2000D_60R_server.txt &')
    
    appClient.cmd('./ngtcp2-reliable/examples/client -b 3 -e -a 3000 -q ', appServer.IP(), ' 5004 > ngtcp2/datasets/RELIABLE_3B_03L_18000F_2000D_60R_client.txt')
    
    time.sleep(20)
    ################################
    
    
    
    
    
    network.stop()
    time.sleep(5)

if __name__ == '__main__':
    quic_exchange()
