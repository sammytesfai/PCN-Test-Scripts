"""
Get time to open a channel. Must be in NORMAL state for channel to be
operational.
"""

from pyln.client import LightningRpc
import random, time


l1 = LightningRpc("/home/sammy/lightning1/testnet/lightning-rpc")
l2 = LightningRpc("/home/sammy/lightning2/testnet/lightning-rpc")

# Get info about the otherlighting daemon
getinfo1 = l1.getinfo()
id = getinfo1['id']
host = getinfo1['binding'][0]['address']
port = getinfo1['binding'][0]['port']


for i in range(0,10):
   # Establish connection, start timer, open channel
   l2.connect(id, host = host, port = port)
   start_time = time.time()
   channel_info = l2.fundchannel(id, amount = 'all', minconf = 0)

   # Identify which peer within nodes list of peers we are currently look at
   peers = l2.listpeers()['peers']
   peer_index = 0
   for i in range(0, len(peers)):
      if peers[i]['id'] == id:
         peer_index = i

   # Identify which channel between peer we are currently looking at
   channels = peers[peer_index]['channels']
   channel_index = 0
   for i in range(0, len(channels)):
      if channels[i]['channel_id'] == channel_info['channel_id']:
         channel_index = i

   # Loop until the states goes from Locked to Normal (Fully operational)
   state = l2.listpeers()['peers'][peer_index]['channels'][channel_index]['state']
   while(state != 'CHANNELD_NORMAL'):
      state = l2.listpeers()['peers'][peer_index]['channels'][channel_index]['state']

   file = open('open_close.txt', 'a')
   file.write('{} '.format(time.time()-start_time))
   file.close()

   start_time = time.time()
   l2.close(id)

   state = l2.listpeers()['peers'][peer_index]['channels'][channel_index]['state']
   while(state != 'ONCHAIN'):
      state = l2.listpeers()['peers'][peer_index]['channels'][channel_index]['state']

   file = open('open_close.txt', 'a')
   file.write('{}\n'.format(time.time()-start_time))
   file.close()
