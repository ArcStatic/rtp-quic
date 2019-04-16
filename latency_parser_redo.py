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

#timestamps seem to be in ns
for i in range(len(end_app_data)):
  if ("stream frame received" in end_app_data[i]):
    received_count += 1
    
print("received stream frames: %d" % received_count)


#timestamps seem to be in ns
for i in range(len(end_app_data)):
  if (("Final" not in end_app_data[i]) and ("Stack" not in end_app_data[i]) and ("length" not in end_app_data[i])):
    item = end_app_data[i].split(',')
    #ie. a latency will only exist if data was passed to the application
    if (int(item[0][15:]) not in app_seqnums):
      app_seqnums.append(int(item[0][15:]))
    
for i in range(len(end_app_data)):
  if (("Final" not in end_app_data[i]) and ("Received" not in end_app_data[i]) and ("length" not in end_app_data[i])):
    item = end_app_data[i].split(',')
    #ie. a latency will only exist if data was passed to the application
    if (int(item[0][13:]) not in stack_seqnums):
      stack_seqnums.append(int(item[0][13:]))
  

for i in range(len(start_data)):
  if (("Final" not in start_data[i]) and ("pktlen" not in start_data[i])):
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
  if (("Final" not in start_data[i]) and ("pktlen" not in start_data[i])):
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

#print("start_app_times_keys:")
#print(start_app_times.keys())
#print("end_app_times_keys:")
#print(end_app_times.keys())
#print("app_seqnums:")
#print(app_seqnums)

for i in range(len(app_seqnums)):
  if ((start_app_times.get(app_seqnums[i]) != None) and (end_app_times.get(app_seqnums[i]) != None)):
    start_app_times_array.append(start_app_times.get(app_seqnums[i]))
    end_app_times_array.append(end_app_times.get(app_seqnums[i]))
    time_axis_data_app_array.append((start_app_times.get(app_seqnums[i]) - first_ts)/1000000000.0)
    
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
  print("app, sn %d: %d - %d =  %f" % (app_seqnums[i], end_app_times_array[i], start_app_times_array[i], app_latencies[i]))
  if app_seqnums[i] != (last_num + 1):
    print("Missing seqnum: %d" % (last_num + 1))
    last_num = app_seqnums[i]
  else:
    last_num = app_seqnums[i]
  #print("time axis data: %f" % time_axis_data_app_array[i])

last_num = 0  
#for i in range(len(start_stack_times)):
  #stack_latencies.append((float(end_stack_times[i]) - float(start_stack_times[i]))/1000000.0)
  
for i in range(min(len(start_stack_times_array), (len(end_stack_times_array)))):
  stack_latencies.append((float(end_stack_times_array[i]) - float(start_stack_times_array[i]))/1000000.0)
  if(stack_latencies[i] < 50):
    print("stack, sn %d: %d - %d =  %f" % (stack_seqnums[i], end_stack_times_array[i], start_stack_times_array[i], stack_latencies[i]))
  if stack_seqnums[i] != (last_num + 1):
    print("Missing seqnum: %d" % (last_num + 1))
    last_num = last_num = stack_seqnums[i] 
  else:
    last_num = stack_seqnums[i]
  #print("app: %d - %d =  %f" % (end_app_times_array[i], start_app_times_array[i], app_latencies[i]))
  #print("time axis data: %f" % time_axis_data_stack_array[i])

#print start_times
#print end_times
#print(app_latencies)
#print(stack_latencies)
#print(time_axis_data_app[0:60])
#print(time_axis_data_stack)

x = time_axis_data_app_array
plt.xlabel("Time elapsed (s)")
#y0 = latencies
#y = y0.copy() + 2.5
y = app_latencies
plt.ylabel("Latency (ms)")

plt.step(x, y, label='Delay between sending data and receiving application data')

#y -= 0.5
#plt.step(x, y, where='post', label='post')

#y = ma.masked_where((y0 > -0.15) & (y0 < 0.15), y - 0.5)
#plt.step(x, y, label='masked (pre)')

plt.legend()

plt.xlim(0, 300)
plt.ylim(0, 300)

#plt.show()
#plt.savefig('app_latency/%s.pdf' % sys.argv[1][:-4])
plt.savefig('app-%s.pdf' % sys.argv[1][:-4])



#######

x = time_axis_data_stack_array
plt.xlabel("Time elapsed (s)")
#y0 = latencies
#y = y0.copy() + 2.5
y = stack_latencies
plt.ylabel("Latency (ms)")

plt.step(x, y, label='Delay between sending data and receiving data at the stack')

#y -= 0.5
#plt.step(x, y, where='post', label='post')

#y = ma.masked_where((y0 > -0.15) & (y0 < 0.15), y - 0.5)
#plt.step(x, y, label='masked (pre)')

plt.legend()

plt.xlim(0, 300)
plt.ylim(0, 300)

plt.savefig('stack-%s.pdf' % sys.argv[1][:-4])













