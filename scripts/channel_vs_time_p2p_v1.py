'''
Get the time to fullfill and invoice vs the number of channels used.
'''

from pyln.client import LightningRpc
import time

fund_amount = 11275
invoice_amount = 1000000

l1 = LightningRpc('/home/sammy/lightning1/testnet/lightning-rpc')
l2 = LightningRpc('/home/sammy/lightning2/testnet/lightning-rpc')

# Get info about the otherlighting daemon
getinfo1 = l1.getinfo()
id = getinfo1['id']
host = getinfo1['binding'][0]['address']
port = getinfo1['binding'][0]['port']

for i in range(0, 1):
   channel_info = l2.fundchannel(id, amount = fund_amount)

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

   invoice_info1 = l1.invoice(invoice_amount*(i+1), "Payment {}".format(invoice_amount), i+1)
   payments = []
   
   start_time = time.time()
   # Divide payment into n numbers of parts, one for each channel
   # with an equal share of the payment
   print("Time to Pay: {}".format(time.time()-start_time))

l2.close(id)
