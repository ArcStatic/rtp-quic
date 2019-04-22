###`pwd`/PARTIALly `pwd`/RELIABLE
python3 latency_parser_offsets_removed_buffer.py `pwd`/PARTIAL_3B_0L_18000F_2000D_60R_server.txt `pwd`/PARTIAL_3B_0L_18000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py `pwd`/PARTIAL_3B_001L_18000F_2000D_60R_server.txt `pwd`/PARTIAL_3B_001L_18000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py `pwd`/PARTIAL_3B_01L_18000F_2000D_60R_server.txt `pwd`/PARTIAL_3B_01L_18000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py `pwd`/PARTIAL_3B_1L_18000F_2000D_60R_server.txt `pwd`/PARTIAL_3B_1L_18000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py `pwd`/PARTIAL_3B_3L_18000F_2000D_60R_server.txt `pwd`/PARTIAL_3B_3L_18000F_2000D_60R_client.txt

sleep 1s



###fully `pwd`/RELIABLE
python3 latency_parser_offsets_removed_buffer.py `pwd`/RELIABLE_3B_0L_18000F_2000D_60R_server.txt `pwd`/RELIABLE_3B_0L_18000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py `pwd`/RELIABLE_3B_001L_18000F_2000D_60R_server.txt `pwd`/RELIABLE_3B_001L_18000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py `pwd`/RELIABLE_3B_01L_18000F_2000D_60R_server.txt `pwd`/RELIABLE_3B_01L_18000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py `pwd`/RELIABLE_3B_1L_18000F_2000D_60R_server.txt `pwd`/RELIABLE_3B_1L_18000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py `pwd`/RELIABLE_3B_1L_18000F_2000D_60R_server.txt `pwd`/RELIABLE_3B_1L_18000F_2000D_60R_client.txt

sleep 1s


###fully `pwd`/RELIABLE single offset example
python3 latency_parser_offsets_single.py `pwd`/RELIABLE_3B_1L_18000F_2000D_60R_server.txt `pwd`/RELIABLE_3B_1L_18000F_2000D_60R_client.txt

###fully `pwd`/RELIABLE combined offsets example
python3 relative_offsets_combined.py


###retransmissions
###`pwd`/PARTIALly `pwd`/RELIABLE
echo "\n`pwd`/PARTIAL, 0% loss" >> retransmission_data.txt
python3 retransmission_parser.py `pwd`/PARTIAL_3B_0L_18000F_2000D_60R_server.txt `pwd`/PARTIAL_3B_0L_18000F_2000D_60R_client.txt >> retransmission_data.txt

sleep 1s

echo "\n`pwd`/PARTIAL, 0.01% loss" >> retransmission_data.txt
python3 retransmission_parser.py`pwd`/PARTIAL_3B_001L_18000F_2000D_60R_server.txt `pwd`/PARTIAL_3B_001L_18000F_2000D_60R_client.txt >> retransmission_data.txt

sleep 1s

echo "\n`pwd`/PARTIAL, 0.1% loss" >> retransmission_data.txt
python3 retransmission_parser.py `pwd`/PARTIAL_3B_01L_18000F_2000D_60R_server.txt `pwd`/PARTIAL_3B_01L_18000F_2000D_60R_client.txt >> retransmission_data.txt

sleep 1s

echo "\n`pwd`/PARTIAL, 1% loss" >> retransmission_data.txt
python3 retransmission_parser.py `pwd`/PARTIAL_3B_1L_18000F_2000D_60R_server.txt `pwd`/PARTIAL_3B_1L_18000F_2000D_60R_client.txt >> retransmission_data.txt

sleep 1s

echo "\n`pwd`/PARTIAL, 3% loss" >> retransmission_data.txt
python3 retransmission_parser.py `pwd`/PARTIAL_3B_3L_18000F_2000D_60R_server.txt `pwd`/PARTIAL_3B_3L_18000F_2000D_60R_client.txt >> retransmission_data.txt

sleep 1s



###fully `pwd`/RELIABLE
echo "\n`pwd`/RELIABLE, 0% loss" >> retransmission_data.txt
python3 retransmission_parser.py `pwd`/RELIABLE_3B_0L_18000F_2000D_60R_server.txt `pwd`/RELIABLE_3B_0L_18000F_2000D_60R_client.txt >> retransmission_data.txt

sleep 1s

echo "\n`pwd`/RELIABLE, 0.01% loss" >> retransmission_data.txt
python3 retransmission_parser.py `pwd`/RELIABLE_3B_001L_18000F_2000D_60R_server.txt `pwd`/RELIABLE_3B_001L_18000F_2000D_60R_client.txt >> retransmission_data.txt

sleep 1s

echo "\n`pwd`/RELIABLE, 0.1% loss" >> retransmission_data.txt
python3 retransmission_parser.py `pwd`/RELIABLE_3B_01L_18000F_2000D_60R_server.txt `pwd`/RELIABLE_3B_01L_18000F_2000D_60R_client.txt >> retransmission_data.txt

sleep 1s

echo "\n`pwd`/RELIABLE, 1% loss" >> retransmission_data.txt
python3 retransmission_parser.py `pwd`/RELIABLE_3B_1L_18000F_2000D_60R_server.txt `pwd`/RELIABLE_3B_1L_18000F_2000D_60R_client.txt >> retransmission_data.txt

sleep 1s

echo "\n`pwd`/RELIABLE, 3% loss" >> retransmission_data.txt
python3 retransmission_parser.py `pwd`/RELIABLE_3B_1L_18000F_2000D_60R_server.txt `pwd`/RELIABLE_3B_1L_18000F_2000D_60R_client.txt >> retransmission_data.txt

sleep 1s






