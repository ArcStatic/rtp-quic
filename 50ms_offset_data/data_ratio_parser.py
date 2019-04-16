import sys
import numpy as np
from numpy import ma
import matplotlib.pyplot as plt

start_data = []
end_app_data = []
end_stack_data = []

with open(sys.argv[1]) as start:
  start_data = start.readlines()
  
with open(sys.argv[2]) as end:
  end_app_data = end.readlines()

first_ts = 0

app_seqnums = []
stack_seqnums = []
start_app_times = {}
start_stack_times = {}
end_app_times = {}
end_stack_times = {}
app_latencies = []
stack_latencies = []
time_axis_data_app = {}
time_axis_data_stack = {}
processed_seqnums = []
received_count = 0
questionable_entries = []
packets_sent = []


#timestamps seem to be in ns
for i in range(len(end_app_data)):
  if (("Final" not in end_app_data[i]) and ("Received" in end_app_data[i]) and ("length" not in end_app_data[i])):
    item = end_app_data[i].split(',')
    #ie. a latency will only exist if data was passed to the application
    if (int(item[0][15:]) not in app_seqnums):
      app_seqnums.append(int(item[0][15:]))
    
for i in range(len(end_app_data)):
  if (("Final" not in end_app_data[i]) and ("Stack" in end_app_data[i]) and ("length" not in end_app_data[i])):
    item = end_app_data[i].split(',')
    #ie. a latency will only exist if data was passed to the application
    if (int(item[0][13:]) not in stack_seqnums):
      stack_seqnums.append(int(item[0][13:]))
  

for i in range(len(start_data)):
  #if (("Final" not in start_data[i]) and ("pktlen" not in start_data[i])):
  if ("sent item" in start_data[i]):
    item = start_data[i].split(',')
    ssn = int(item[0][11:])
    packets_sent.append(int(item[0][11:]))
    sts = float(item[1][:-1])
    #ie. a latency will only exist if data was passed to the application
    #if (int(item[0][11:]) in app_seqnums):
    #if ((int(item[0][11:]) in app_seqnums) and (int(item[0][11:]) not in processed_seqnums)):
    if (not start_app_times):
      first_ts = (float(item[1][:-1]))
    #if (ssn not in start_app_times):
    if (start_app_times.get(ssn) == None):
      start_app_times[ssn] = sts
    else:
      pass
      #print("%d already in dictionary" % int(item[0][11:]))
    #time_axis_data_app[ssn] = ((float(item[1][:-1]) - first_ts)/1000000000.0)
    

for i in range(len(start_data)):
  #if (("Final" not in start_data[i]) and ("pktlen" not in start_data[i])):
  if ("sent item" in start_data[i]):
    item = start_data[i].split(',')
    ssn = int(item[0][11:])
    sts = float(item[1][:-1])
    #ie. a latency will only exist if data was passed to the application
    #if (int(item[0][11:]) in app_seqnums):
    #if ((int(item[0][11:]) in app_seqnums) and (int(item[0][11:]) not in processed_seqnums)):
    #if (not start_stack_times):
      #first_ts = (float(item[1][:-1]))
    #if (ssn not in start_stack_times):
    if (start_stack_times.get(ssn) == None):
      start_stack_times[ssn] = sts
    #time_axis_data_stack[ssn] = ((float(item[1][:-1]) - first_ts)/1000000000.0)
   


#print(sorted(stack_seqnums))
app_seqnums = sorted(app_seqnums)
stack_seqnums = sorted(stack_seqnums)
#print(start_stack_times)
print(len(start_stack_times))
#print(end_stack_times)
print(len(end_stack_times))

#print(start_app_times)
print(len(start_app_times))
#print(end_app_times)
print(len(end_app_times))

print("App: %d entries" % len(app_seqnums))
#print(app_seqnums)
print("Stack: %d entries" % len(stack_seqnums))
#print(stack_seqnums)

playback_times_actual = []
playback_times_rtp_ts = []

#there will be more data in start_data than end_data due to retransmissions
for i in range(len(end_app_data)):
  if (("Final" not in end_app_data[i]) and ("Received" in end_app_data[i]) and ("length" not in end_app_data[i])):
    item = end_app_data[i].split(',')
    #print("end time: %d" % int(item[0][15:]))
    end_app_times[int(item[0][15:])] = float(item[1][:-1])
    if (start_app_times.get(int(item[0][15:]))):
      #print("accepted: %d" % int(item[0][15:]))
      time_axis_data_app[int(item[0][15:])] = ((start_app_times.get(int(item[0][15:])) - first_ts)/1000000000.0)
    #time_axis_data_app[int(item[0][15:])] = ((float(item[1][:-1]) - first_ts)/1000000000.0)
    #end_times.append(float(item[1][:-1])/1000000000)
    #end_app_times.append(float(item[1][:-1])/1000000000)
    #end_app_times.append(float(item[1][:-1]))
    #else:
      #end_times.append(0)
    playback_item = end_app_data[i+1].split(',')
    playback_times_actual.append(int(playback_item[0][21:]))
    playback_times_rtp_ts.append(int(playback_item[1][14:-1]))
      
#print(start_app_times)
print("")
print("")
#print(time_axis_data_app)


#there will be more data in start_data than end_data due to retransmissions
for i in range(len(end_app_data)):
  if (("Final" not in end_app_data[i]) and ("Stack" in end_app_data[i]) and ("length" not in end_app_data[i])):
    item = end_app_data[i].split(',')
    end_stack_times[int(item[0][13:])] = float(item[1][:-1])
    if (start_stack_times.get(int(item[0][13:]))):
      time_axis_data_stack[int(item[0][13:])] = ((start_stack_times.get(int(item[0][13:])) - first_ts)/1000000000.0)
    #time_axis_data_stack[int(item[0][13:])] = ((float(item[1][:-1]) - first_ts)/1000000000.0)
    #end_times.append(float(item[1][:-1])/1000000000)
    #end_app_times.append(float(item[1][:-1])/1000000000)
    #end_app_times.append(float(item[1][:-1]))
    #else:
      #end_times.append(0)

#print(len(start_stack_times))
#print(end_stack_times)
#print(len(end_stack_times))

#print(start_app_times)
#print(len(start_app_times))
#print(end_app_times)
#print(len(end_app_times))
    
#time_axis_data_app_array = sorted(time_axis_data_app.values())
#start_app_times_array = sorted(start_app_times.values())
#end_app_times_array = sorted(end_app_times.values())

##!!ERRORS CAUSED BY MISALIGNED VALUES!!

time_axis_data_app_array = []
start_app_times_array = []
end_app_times_array = []

time_axis_data_stack_array = []
start_stack_times_array = []
end_stack_times_array = []

playback_offsets_array = []
pb_delay_counter_array = []
pb_delay_counter = 0

total_packets = 0
useful_packets = 0
stale_packets = 0

#print("start_app_times_keys:")
#print(start_app_times.keys())
#print("end_app_times_keys:")
#print(end_app_times.keys())
#print("app_seqnums:")
#print(app_seqnums)

for i in range(len(app_seqnums)):
  if ((start_app_times.get(app_seqnums[i]) != None) and (end_app_times.get(app_seqnums[i]) != None)):
    #plot send -> receive at app latencies
    start_app_times_array.append(start_app_times.get(app_seqnums[i]))
    end_app_times_array.append(end_app_times.get(app_seqnums[i]))
    time_axis_data_app_array.append((start_app_times.get(app_seqnums[i]) - first_ts)/1000000000.0)
  if ((end_stack_times.get(stack_seqnums[i]) != None) and (end_app_times.get(app_seqnums[i]) != None)):
    #plot receive at app -> playback latencies
    #playback_offsets_array.append((playback_times_actual[i] - playback_times_rtp_ts[i]) * (3000 * (1000/60)))
    playback_offsets_array.append((playback_times_actual[i] - playback_times_rtp_ts[i]))
    if ((playback_offsets_array[i] != 0) and (playback_offsets_array[i-1] < 0) and (playback_offsets_array[i] > 0)):
      pb_delay_counter += playback_offsets_array[i]
    #pb_delay_counter_array.append(pb_delay_counter)
    pb_delay_counter_array.append(((pb_delay_counter)/3000) * (1000/60))
    #print(playback_offsets_array[i])
    #print("%d, %d" % (i, pb_delay_counter))
    #print(pb_delay_counter/3000)
    #print(((pb_delay_counter)/3000) * (1000/60))
    if (playback_offsets_array[i] > 0):
      stale_packets += 1
    else:
      useful_packets += 1

#print("Total packets received: %d" % (stale_packets + useful_packets))
print("Total packets sent: %d" % len(packets_sent))
print("Useful packets: %d" % (useful_packets))
print("Stale packets: %d" % (stale_packets))
#print("percentage of useful packets: %d" % ((useful_packets/(stale_packets + useful_packets)) * 100))
print("percentage of useful packets: %d" % ((useful_packets/len(packets_sent)) * 100))



