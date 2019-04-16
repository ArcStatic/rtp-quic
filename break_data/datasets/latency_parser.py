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
start_app_times = []
start_stack_times = []
end_app_times = []
end_stack_times = []
app_latencies = []
stack_latencies = []
time_axis_data_app = []
time_axis_data_stack = []
processed_seqnums = []
received_count = 0

#timestamps seem to be in ns
for i in range(len(end_app_data)):
  if ("stream frame received" in end_app_data[i]):
    received_count += 1
    
print("received stream frames: %d" % received_count)


#timestamps seem to be in ns
for i in range(len(end_app_data)):
  if (("Final" not in end_app_data[i]) and ("Stack" not in end_app_data[i])):
    item = end_app_data[i].split(',')
    #ie. a latency will only exist if data was passed to the application
    app_seqnums.append(int(item[0][15:]))
    
for i in range(len(end_app_data)):
  if (("Final" not in end_app_data[i]) and ("Received" not in end_app_data[i])):
    item = end_app_data[i].split(',')
    #ie. a latency will only exist if data was passed to the application
    stack_seqnums.append(int(item[0][13:]))
  

for i in range(len(start_data)):
  if ("Final" not in start_data[i]):
    item = start_data[i].split(',')
    #ie. a latency will only exist if data was passed to the application
    #if (int(item[0][11:]) in app_seqnums):
    if ((int(item[0][11:]) in app_seqnums) and (int(item[0][11:]) not in processed_seqnums)):
      #print("app match found: %s" % item[0][11:])
      if (start_app_times == []):
        #first_ts = (float(item[1][:-1])/1000000000)
      #start_times.append(float(item[1][:-1])/1000000000)
      #time_axis_data.append((float(item[1][:-1])/1000000000) - first_ts)
        first_ts = (float(item[1][:-1])/1000000000)
      start_app_times.append(float(item[1][:-1])/1000000000)
      processed_seqnums.append(int(item[0][11:]))
      #print("start app times len: %d" % len(start_app_times))
      time_axis_data_app.append((float(item[1][:-1])/1000000000) - first_ts)

processed_seqnums = []
      
for i in range(len(start_data)):
  if ("Final" not in start_data[i]):
    item = start_data[i].split(',')
    #ie. a latency will only exist if data was passed to the application
    if ((int(item[0][11:]) in stack_seqnums) and (int(item[0][11:]) not in processed_seqnums)):
      print("stack match found: %s" % item[0][11:])
      if (start_stack_times == []):
        #first_ts = (float(item[1][:-1])/1000000000)
      #start_times.append(float(item[1][:-1])/1000000000)
      #time_axis_data.append((float(item[1][:-1])/1000000000) - first_ts)
        first_ts = (float(item[1][:-1])/1000000000)
      start_stack_times.append(float(item[1][:-1])/1000000000)
      processed_seqnums.append(int(item[0][11:]))
      print("start stack times len: %d" % len(start_stack_times))
      time_axis_data_stack.append((float(item[1][:-1])/1000000000) - first_ts)


#print(sorted(stack_seqnums))
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
print(app_seqnums)
print("Stack: %d entries" % len(stack_seqnums))
print(stack_seqnums)

#there will be more data in start_data than end_data due to retransmissions
for i in range(len(end_app_data)):
  if (("Final" not in end_app_data[i]) and ("Received" in end_app_data[i])):
    item = end_app_data[i].split(',')
    #end_times.append(float(item[1][:-1])/1000000000)
    end_app_times.append(float(item[1][:-1])/1000000000)
    #else:
      #end_times.append(0)

for i in range(len(end_app_data)):
  if (("Final" not in end_app_data[i]) and ("rx" in end_app_data[i])):
    item = end_app_data[i].split(',')
    #end_times.append(float(item[1][:-1])/1000000000)
    end_stack_times.append(float(item[1][:-1])/1000000000)
    #else:
      #end_times.append(0)


print(len(start_stack_times))
#print(end_stack_times)
print(len(end_stack_times))

#print(start_app_times)
print(len(start_app_times))
#print(end_app_times)
print(len(end_app_times))
    
for i in range(len(start_app_times)):
  app_latencies.append(end_app_times[i] - start_app_times[i])
    
for i in range(len(start_stack_times)):
  stack_latencies.append(end_stack_times[i] - start_stack_times[i])

#print start_times
#print end_times
#print(app_latencies)
#print(stack_latencies)
#print(time_axis_data_app)
#print(time_axis_data_stack)






x = time_axis_data_app
#y0 = latencies
#y = y0.copy() + 2.5
y = app_latencies

plt.step(x, y, label='Latency between sending data and receiving application data (reliable)s')

#y -= 0.5
#plt.step(x, y, where='post', label='post')

#y = ma.masked_where((y0 > -0.15) & (y0 < 0.15), y - 0.5)
#plt.step(x, y, label='masked (pre)')

plt.legend()

plt.xlim(0, 30000)
plt.ylim(0, 10)

#plt.show()
plt.savefig('app_latency/%s.pdf' % sys.argv[1][:-4])










