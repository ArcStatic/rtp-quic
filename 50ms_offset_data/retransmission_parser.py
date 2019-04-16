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
retransmissions = 0

for i in range(len(start_data)):
  #if (("Final" not in start_data[i]) and ("pktlen" not in start_data[i])):
  if ("sent item" in start_data[i]):
    item = start_data[i].split(',')
    ssn = int(item[0][11:])
    if (ssn not in stack_seqnums):
      stack_seqnums.append(ssn)
    else:
      retransmissions += 1


print("Retransmissions: %d" % retransmissions)

playback_times_actual = []
playback_times_rtp_ts = []


