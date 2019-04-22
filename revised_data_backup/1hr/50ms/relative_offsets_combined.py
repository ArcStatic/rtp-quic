import sys
import numpy as np
from numpy import ma
import matplotlib.pyplot as plt


#filename = sys.argv[1].split("/")

client_files = ["/home/vivian/Documents/L5project/rtp-quic/revised_data/1hr/50ms/RELIABLE_3B_0L_18000F_2000D_60R_client.txt", "/home/vivian/Documents/L5project/rtp-quic/revised_data/1hr/50ms/RELIABLE_3B_001L_18000F_2000D_60R_client.txt", "/home/vivian/Documents/L5project/rtp-quic/revised_data/1hr/50ms/RELIABLE_3B_01L_18000F_2000D_60R_client.txt", "/home/vivian/Documents/L5project/rtp-quic/revised_data/1hr/50ms/RELIABLE_3B_1L_18000F_2000D_60R_client.txt", "/home/vivian/Documents/L5project/rtp-quic/revised_data/1hr/50ms/RELIABLE_3B_3L_18000F_2000D_60R_client.txt"]


server_files = ["/home/vivian/Documents/L5project/rtp-quic/revised_data/1hr/50ms/RELIABLE_3B_0L_18000F_2000D_60R_server.txt", "/home/vivian/Documents/L5project/rtp-quic/revised_data/1hr/50ms/RELIABLE_3B_001L_18000F_2000D_60R_server.txt", "/home/vivian/Documents/L5project/rtp-quic/revised_data/1hr/50ms/RELIABLE_3B_01L_18000F_2000D_60R_server.txt", "/home/vivian/Documents/L5project/rtp-quic/revised_data/1hr/50ms/RELIABLE_3B_1L_18000F_2000D_60R_server.txt", "/home/vivian/Documents/L5project/rtp-quic/revised_data/1hr/50ms/RELIABLE_3B_3L_18000F_2000D_60R_server.txt"]

start_data = []
end_app_data = []
end_stack_data = []

played_times_collected = []
playback_offsets_array_collected = []
time_axis_data_app_array_collected = []
sent_times_collected = []



for f in range(len(server_files)):
  with open(server_files[f]) as start:
    start_data = start.readlines()
    
  with open(client_files[f]) as end:
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

  #timestamps seem to be in ns
  for i in range(len(end_app_data)):
    if ("stream frame received" in end_app_data[i]):
      received_count += 1
      
  print("received stream frames: %d" % received_count)


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
  pb_offsets_array = []

  sent_times = []
  played_times = []
  played_times_ns = []

  #print("start_app_times_keys:")
  #print(start_app_times.keys())
  #print("end_app_times_keys:")
  #print(end_app_times.keys())
  #print("app_seqnums:")
  #print(app_seqnums)
  playback_diff_prev = 0

  diff_per_frame = 1/60.0
  print("diff_per_frame: %f" % diff_per_frame)

  diff_per_frame_ns = 1000000000.0/60.0
  print("diff_per_frame_ns: %f" % diff_per_frame_ns)
  fragment = 0


  for i in range(len(app_seqnums)):
    if ((start_app_times.get(app_seqnums[i]) != None) and (end_app_times.get(app_seqnums[i]) != None)):
      #plot send -> receive at app latencies
      start_app_times_array.append(start_app_times.get(app_seqnums[i]))
      end_app_times_array.append(end_app_times.get(app_seqnums[i]))
      time_axis_data_app_array.append((start_app_times.get(app_seqnums[i]) - first_ts)/1000000000.0)
    if ((end_stack_times.get(stack_seqnums[i]) != None) and (end_app_times.get(app_seqnums[i]) != None)):
      #plot receive at app -> playback latencies
      #calculate playback offsets as if application resumes playback on lost packet
      #(ie. playback deadline doesn't increment while stalled)
      #playback_offsets_array.append((playback_times_actual[i] - playback_times_rtp_ts[i]))
      
      playback_diff = playback_times_actual[i] - playback_times_rtp_ts[i]
      if (i != 0):
        playback_diff_prev = playback_times_actual[i-1] - playback_times_rtp_ts[i-1]
      #if ((playback_offsets_array[i] != 0) and (playback_offsets_array[i-1] < 0) and (playback_offsets_array[i] > 0)):
      if ((playback_diff_prev <= 0) and (playback_diff > 0)):
        #pb_delay_counter += playback_diff
        pb_delay_counter += (12000 + playback_diff)
      
      
      
      delay_encountered = (playback_diff > playback_diff_prev)
      
      #print("i: %d" % i)
      sent_time = (start_app_times.get(app_seqnums[i]))
      #played_time = (end_app_times.get(app_seqnums[i]))
      #add playback delay and diff per frame
      #played_time = (end_app_times.get(app_seqnums[i]) + (((pb_delay_counter)/3000) * diff_per_frame_ns) + diff_per_frame_ns)
      if(i == 0):
        played_time = (end_app_times.get(app_seqnums[i]) + (((pb_delay_counter)/3000) * diff_per_frame_ns) + diff_per_frame_ns)
        fragment = 1
      else:
        #played_time = (played_times[i-1] + (((pb_delay_counter)/3000) * diff_per_frame_ns) + diff_per_frame_ns)
        #ie. if it's a subsequent section of an I-frame
        if ((fragment != 0) and (((playback_times_rtp_ts[i] - 3000) % 30000 == 0))):
          played_time = (played_times_ns[i-1])
        #if it's the first section of an I-frame
        elif (((playback_times_rtp_ts[i] - 3000) % 30000 == 0)):
          frame_gap = (playback_times_rtp_ts[i] - playback_times_rtp_ts[i-1]) / 3000
          #print("frame gap at item %d: %d" % (i, frame_gap))
          if (playback_diff > playback_diff_prev):
            #played_time = (played_times_ns[i-1] + (((pb_delay_counter)/3000) * diff_per_frame_ns) + diff_per_frame_ns)
            played_time = (played_times_ns[i-1] + ((((pb_delay_counter)/3000) * diff_per_frame_ns) + (diff_per_frame_ns * frame_gap)))
          else:
            #played_time = (played_times_ns[i-1] + diff_per_frame_ns)
            played_time = (played_times_ns[i-1] + (diff_per_frame_ns * frame_gap))
          fragment += 1
        #otherwise, it's a P-frame
        #constantly adds pb_delay counter, should only be added once
        else:
          frame_gap = (playback_times_rtp_ts[i] - playback_times_rtp_ts[i-1]) / 3000
          if (playback_diff > playback_diff_prev):
            #played_time = (played_times_ns[i-1] + (((pb_delay_counter)/3000) * diff_per_frame_ns) + diff_per_frame_ns)
            played_time = (played_times_ns[i-1] + (((pb_delay_counter)/3000) * diff_per_frame_ns) + (diff_per_frame_ns * frame_gap))
          else:
            #played_time = (played_times_ns[i-1] + diff_per_frame_ns)
            played_time = (played_times_ns[i-1] + (diff_per_frame_ns * frame_gap))
          fragment = 0
      #print("pb_delay_counter: %d " % pb_delay_counter)
      #print("pb_delay_counter ns: %d " % (((pb_delay_counter)/3000) * diff_per_frame_ns))
      #print("played_time: %d (%f)" % (played_time, (played_time - first_ts)/1000000000.0))
      #playback time calculated in s
      #playback_offsets_array.append((played_time - sent_time)/1000000000.0)
      #playback_offsets_array.append(((played_time - sent_time) + (((pb_delay_counter)/3000) * diff_per_frame_ns))/1000000000.0)
      #print("played_time - sent_time = playback_offset_time")
      #print("%f - %f = %f" % ((played_time - first_ts)/1000000000.0, (sent_time - first_ts)/1000000000.0, (played_time - sent_time)/1000000000.0))
      #sent_times.append(sent_time/1000000000.0)
      sent_times.append((sent_time - first_ts)/1000000000.0)
      #print("sent_times appended val: %f" % ((sent_time - first_ts)/1000000000.0))
      
      #act as if client freezes when there's no content, buffers, then resumes from missing frame
      #if (playback_times_actual[i] > playback_times_rtp_ts[i]):
        #playback_times_actual[i] = playback_times_rtp_ts[i]
      
      pb_offset_seconds = ((pb_delay_counter)/3000) * diff_per_frame;
      #print("pb_offset_seconds: %f " % pb_offset_seconds)
      
      
     
      
      played_times.append((played_time - first_ts)/1000000000.0)
      played_times_ns.append((played_time))
      playback_offsets_array.append(played_times[i] - sent_times[i])
      #print(played_times[i])
      #print(played_times_ns[i])
      #print("#####")
        #print("played_times appended val: %f" % ((played_time - first_ts)/1000000000.0))
      #playback_offsets_array.append((played_times[i] - (sent_time/1000000000.0)))
      pb_offsets_array.append(pb_offset_seconds)
      
  for i in range(len(stack_seqnums)):
    if ((start_stack_times.get(stack_seqnums[i]) != None) and (end_stack_times.get(stack_seqnums[i]) != None)):
      start_stack_times_array.append(start_stack_times.get(stack_seqnums[i]))
      end_stack_times_array.append(end_stack_times.get(stack_seqnums[i]))
      time_axis_data_stack_array.append((start_stack_times.get(stack_seqnums[i]) - first_ts)/1000000000.0)
      
  print("App start: %d len" % len(start_app_times_array))
  #print(app_seqnums)
  print("Stack start: %d len" % len(start_stack_times_array))
  #print(app_seqnums)
  print("App end: %d len" % len(end_app_times_array))
  #print(stack_seqnums)
  print("Stack end: %d len" % len(end_stack_times_array))
  #print(stack_seqnums)

  #time_axis_data_app_array = list(time_axis_data_app.values())
  #start_app_times_array = list(start_app_times.values())
  #end_app_times_array = list(end_app_times.values())

  #time_axis_data_stack_array = list(time_axis_data_stack.values())
  #start_stack_times_array = list(start_stack_times.values())
  #end_stack_times_array = list(end_stack_times.values())


  #time_axis_data_stack_array = sorted(time_axis_data_app.values())
  #start_stack_times_array = sorted(start_app_times.values())
  #end_stack_times_array = sorted(end_app_times.values())
      
  #for i in range(len(start_app_times)):
    #app_latencies.append((float(end_app_times[i]) - float(start_app_times[i]))/1000000.0)
    #print("%d - %d =  %f" % (end_app_times[i], start_app_times[i], app_latencies[i]))
    #print("time axis data: %f" % time_axis_data_app[i])
    
  last_num = 0

  for i in range(min(len(start_app_times_array), (len(end_app_times_array)))):
    #app latencies seem too high by a factor of 10 in some cases
    app_latencies.append((float(end_app_times_array[i]) - float(start_app_times_array[i]))/1000000.0)
    #if(app_latencies[i] > 100):
      #print("app, sn %d: %d - %d =  %f" % (app_seqnums[i], end_app_times_array[i], start_app_times_array[i], app_latencies[i]))
    '''
    if app_seqnums[i] != (last_num + 1):
      #print("Missing seqnum: %d" % (last_num + 1))
      last_num = app_seqnums[i]
    else:
      last_num = app_seqnums[i]
    #print("time axis data: %f" % time_axis_data_app_array[i])
    '''

  last_num = 0  
  #for i in range(len(start_stack_times)):
    #stack_latencies.append((float(end_stack_times[i]) - float(start_stack_times[i]))/1000000.0)
    
  for i in range(min(len(start_stack_times_array), (len(end_stack_times_array)))):
    stack_latencies.append((float(end_stack_times_array[i]) - float(start_stack_times_array[i]))/1000000.0)
    #if(stack_latencies[i] > 100):
    #print("stack, sn %d: %d - %d =  %f" % (stack_seqnums[i], end_stack_times_array[i], start_stack_times_array[i], stack_latencies[i]))
    '''
    if stack_seqnums[i] != (last_num + 1):
      #print("Missing seqnum: %d" % (last_num + 1))
      last_num = last_num = stack_seqnums[i] 
    else:
      last_num = stack_seqnums[i]
    #print("app: %d - %d =  %f" % (end_app_times_array[i], start_app_times_array[i], app_latencies[i]))
    #print("time axis data: %f" % time_axis_data_stack_array[i])
    '''

  #print start_times
  #print end_times
  #print(app_latencies)
  #print(stack_latencies)
  #print(time_axis_data_app[0:60])
  #print(time_axis_data_stack)

#'''
  played_times_collected.append(played_times)
  playback_offsets_array_collected.append(playback_offsets_array)
  time_axis_data_app_array_collected.append(time_axis_data_app_array)
  sent_times_collected.append(sent_times)

################################


#################

plt.ylabel("Actual playback time (s)")
#y0 = latencies
#y = y0.copy() + 2.5
#y = pb_delay_counter_array

plt.xlabel("Time sent (s)")

#lines = plt.step(x, y, label='Actual time each packet is played when reaching application')
lines = []
for a in range(len(server_files)):
  x = sent_times_collected[a]
  y = played_times_collected[a]
  if (a == 0):
    lines.append(plt.step(x, y, label = "0% loss"))
  elif (a == 1):
    lines.append(plt.step(x, y, label = "1% loss"))
  elif (a == len(server_files)-1):
    lines.append(plt.step(x, y, label = "3% loss"))
  #else:
    #lines.append(plt.step(x, y))

#y -= 0.5
#plt.step(x, y, where='post', label='post')

plt.legend()

plt.xlim(0, 300)
plt.ylim(0, 300)

#y = ma.masked_where((y0 > -0.15) & (y0 < 0.15), y - 0.5)
#plt.step(x, y, label='masked (pre)')


#plt.show()
#plt.savefig('app_latency/%s.pdf' % sys.argv[1][:-4])
plt.savefig('offsets-relative-combined.png')

#for a in range(len(server_files)):
#  l = lines.pop(a)
#  l.remove()
#  del l

#################

plt.xlabel("Time elapsed (s)")
#y0 = latencies
#y = y0.copy() + 2.5
#y = pb_delay_counter_array
#y = playback_offsets_array

plt.ylabel("Cumulative playback delay (s)")

#lines = plt.step(x, y, label='Actual time each packet is played when reaching application')
lines = []
for a in range(len(server_files)):
  x = time_axis_data_app_array_collected[a]
  y = playback_offsets_array_collected[a]
  lines.append(plt.step(x, y))

#y -= 0.5
#plt.step(x, y, where='post', label='post')

#plt.legend()

plt.xlim(0, 300)
plt.ylim(0, 1.5)

#y = ma.masked_where((y0 > -0.15) & (y0 < 0.15), y - 0.5)
#plt.step(x, y, label='masked (pre)')


#plt.show()
#plt.savefig('app_latency/%s.pdf' % sys.argv[1][:-4])
#plt.savefig('offsets-combined.png')
plt.savefig('%s/offsets-combined.png' % ("/".join(str(s) for s in filename[:-1])))





