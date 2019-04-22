###50ms/PARTIALly 50ms/RELIABLE
python3 latency_parser_offsets_removed_buffer.py 50ms/PARTIAL_3B_0L_18000F_2000D_60R_server.txt 50ms/PARTIAL_3B_0L_18000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py 50ms/PARTIAL_3B_001L_18000F_2000D_60R_server.txt 50ms/PARTIAL_3B_001L_18000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py 50ms/PARTIAL_3B_01L_18000F_2000D_60R_server.txt 50ms/PARTIAL_3B_01L_18000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py 50ms/PARTIAL_3B_1L_18000F_2000D_60R_server.txt 50ms/PARTIAL_3B_1L_18000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py 50ms/PARTIAL_3B_3L_18000F_2000D_60R_server.txt 50ms/PARTIAL_3B_3L_18000F_2000D_60R_client.txt

sleep 1s



###fully 50ms/RELIABLE
python3 latency_parser_offsets_removed_buffer.py 50ms/RELIABLE_3B_0L_18000F_2000D_60R_server.txt 50ms/RELIABLE_3B_0L_18000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py 50ms/RELIABLE_3B_001L_18000F_2000D_60R_server.txt 50ms/RELIABLE_3B_001L_18000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py 50ms/RELIABLE_3B_01L_18000F_2000D_60R_server.txt 50ms/RELIABLE_3B_01L_18000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py 50ms/RELIABLE_3B_1L_18000F_2000D_60R_server.txt 50ms/RELIABLE_3B_1L_18000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py 50ms/RELIABLE_3B_3L_18000F_2000D_60R_server.txt 50ms/RELIABLE_3B_3L_18000F_2000D_60R_client.txt

sleep 1s


###fully 50ms/RELIABLE single offset example
python3 latency_parser_offsets_single.py 50ms/RELIABLE_3B_1L_18000F_2000D_60R_server.txt 50ms/RELIABLE_3B_1L_18000F_2000D_60R_client.txt

###fully 50ms/RELIABLE combined offsets example
python3 50ms/relative_offsets_combined.py


###retransmissions
###50ms/PARTIALly 50ms/RELIABLE
echo "\n50ms/PARTIAL, 0% loss" >> 50ms/retransmission_data.txt
echo `python3 50ms/retransmission_parser.py 50ms/PARTIAL_3B_0L_18000F_2000D_60R_server.txt 50ms/PARTIAL_3B_0L_18000F_2000D_60R_client.txt` >> 50ms/retransmission_data.txt

sleep 1s

echo "\n50ms/PARTIAL, 0.01% loss" >> 50ms/retransmission_data.txt
echo `python3 50ms/retransmission_parser.py 50ms/PARTIAL_3B_001L_18000F_2000D_60R_server.txt 50ms/PARTIAL_3B_001L_18000F_2000D_60R_client.txt` >> 50ms/retransmission_data.txt

sleep 1s

echo "\n50ms/PARTIAL, 0.1% loss" >> 50ms/retransmission_data.txt
echo `python3 50ms/retransmission_parser.py 50ms/PARTIAL_3B_01L_18000F_2000D_60R_server.txt 50ms/PARTIAL_3B_01L_18000F_2000D_60R_client.txt` >> 50ms/retransmission_data.txt

sleep 1s

echo "\n50ms/PARTIAL, 1% loss" >> 50ms/retransmission_data.txt
echo `python3 50ms/retransmission_parser.py 50ms/PARTIAL_3B_1L_18000F_2000D_60R_server.txt 50ms/PARTIAL_3B_1L_18000F_2000D_60R_client.txt` >> 50ms/retransmission_data.txt

sleep 1s

echo "\n50ms/PARTIAL, 3% loss" >> 50ms/retransmission_data.txt
echo `python3 50ms/retransmission_parser.py 50ms/PARTIAL_3B_3L_18000F_2000D_60R_server.txt 50ms/PARTIAL_3B_3L_18000F_2000D_60R_client.txt` >> 50ms/retransmission_data.txt

sleep 1s



###fully 50ms/RELIABLE
echo "\n50ms/RELIABLE, 0% loss" >> 50ms/retransmission_data.txt
echo `python3 50ms/retransmission_parser.py 50ms/RELIABLE_3B_0L_18000F_2000D_60R_server.txt 50ms/RELIABLE_3B_0L_18000F_2000D_60R_client.txt` >> 50ms/retransmission_data.txt

sleep 1s

echo "\n50ms/RELIABLE, 0.01% loss" >> 50ms/retransmission_data.txt
echo `python3 50ms/retransmission_parser.py 50ms/RELIABLE_3B_001L_18000F_2000D_60R_server.txt 50ms/RELIABLE_3B_001L_18000F_2000D_60R_client.txt` >> 50ms/retransmission_data.txt

sleep 1s

echo "\n50ms/RELIABLE, 0.1% loss" >> 50ms/retransmission_data.txt
echo `python3 50ms/retransmission_parser.py 50ms/RELIABLE_3B_01L_18000F_2000D_60R_server.txt 50ms/RELIABLE_3B_01L_18000F_2000D_60R_client.txt` >> 50ms/retransmission_data.txt

sleep 1s

echo "\n50ms/RELIABLE, 1% loss" >> 50ms/retransmission_data.txt
echo `python3 50ms/retransmission_parser.py 50ms/RELIABLE_3B_1L_18000F_2000D_60R_server.txt 50ms/RELIABLE_3B_1L_18000F_2000D_60R_client.txt` >> 50ms/retransmission_data.txt

sleep 1s

echo "\n50ms/RELIABLE, 3% loss" >> 50ms/retransmission_data.txt
echo `python3 50ms/retransmission_parser.py 50ms/RELIABLE_3B_1L_18000F_2000D_60R_server.txt 50ms/RELIABLE_3B_1L_18000F_2000D_60R_client.txt` >> 50ms/retransmission_data.txt

sleep 1s






