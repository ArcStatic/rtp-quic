###150ms/PARTIALly 150ms/RELIABLE
python3 latency_parser_offsets_removed_buffer.py 150ms/PARTIAL_3B_0L_18000F_2000D_60R_server.txt 150ms/PARTIAL_3B_0L_18000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py 150ms/PARTIAL_3B_001L_18000F_2000D_60R_server.txt 150ms/PARTIAL_3B_001L_18000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py 150ms/PARTIAL_3B_01L_18000F_2000D_60R_server.txt 150ms/PARTIAL_3B_01L_18000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py 150ms/PARTIAL_3B_1L_18000F_2000D_60R_server.txt 150ms/PARTIAL_3B_1L_18000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py 150ms/PARTIAL_3B_3L_18000F_2000D_60R_server.txt 150ms/PARTIAL_3B_3L_18000F_2000D_60R_client.txt

sleep 1s



###fully 150ms/RELIABLE
python3 latency_parser_offsets_removed_buffer.py 150ms/RELIABLE_3B_0L_18000F_2000D_60R_server.txt 150ms/RELIABLE_3B_0L_18000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py 150ms/RELIABLE_3B_001L_18000F_2000D_60R_server.txt 150ms/RELIABLE_3B_001L_18000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py 150ms/RELIABLE_3B_01L_18000F_2000D_60R_server.txt 150ms/RELIABLE_3B_01L_18000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py 150ms/RELIABLE_3B_1L_18000F_2000D_60R_server.txt 150ms/RELIABLE_3B_1L_18000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py 150ms/RELIABLE_3B_3L_18000F_2000D_60R_server.txt 150ms/RELIABLE_3B_3L_18000F_2000D_60R_client.txt

sleep 1s


###fully 150ms/RELIABLE single offset example
python3 latency_parser_offsets_single.py 150ms/RELIABLE_3B_1L_18000F_2000D_60R_server.txt 150ms/RELIABLE_3B_1L_18000F_2000D_60R_client.txt

###fully 150ms/RELIABLE combined offsets example
python3 150ms/relative_offsets_combined.py


###retransmissions
###150ms/PARTIALly 150ms/RELIABLE
echo "\n150ms/PARTIAL, 0% loss" >> 150ms/retransmission_data.txt
echo `python3 150ms/retransmission_parser.py 150ms/PARTIAL_3B_0L_18000F_2000D_60R_server.txt 150ms/PARTIAL_3B_0L_18000F_2000D_60R_client.txt` >> 150ms/retransmission_data.txt

sleep 1s

echo "\n150ms/PARTIAL, 0.01% loss" >> 150ms/retransmission_data.txt
echo `python3 150ms/retransmission_parser.py150ms/PARTIAL_3B_001L_18000F_2000D_60R_server.txt 150ms/PARTIAL_3B_001L_18000F_2000D_60R_client.txt` >> 150ms/retransmission_data.txt

sleep 1s

echo "\n150ms/PARTIAL, 0.1% loss" >> 150ms/retransmission_data.txt
echo `python3 150ms/retransmission_parser.py 150ms/PARTIAL_3B_01L_18000F_2000D_60R_server.txt 150ms/PARTIAL_3B_01L_18000F_2000D_60R_client.txt` >> 150ms/retransmission_data.txt

sleep 1s

echo "\n150ms/PARTIAL, 1% loss" >> 150ms/retransmission_data.txt
echo `python3 150ms/retransmission_parser.py 150ms/PARTIAL_3B_1L_18000F_2000D_60R_server.txt 150ms/PARTIAL_3B_1L_18000F_2000D_60R_client.txt` >> 150ms/retransmission_data.txt

sleep 1s

echo "\n150ms/PARTIAL, 3% loss" >> 150ms/retransmission_data.txt
echo `python3 150ms/retransmission_parser.py 150ms/PARTIAL_3B_3L_18000F_2000D_60R_server.txt 150ms/PARTIAL_3B_3L_18000F_2000D_60R_client.txt` >> 150ms/retransmission_data.txt

sleep 1s



###fully 150ms/RELIABLE
echo "\n150ms/RELIABLE, 0% loss" >> 150ms/retransmission_data.txt
echo `python3 150ms/retransmission_parser.py 150ms/RELIABLE_3B_0L_18000F_2000D_60R_server.txt 150ms/RELIABLE_3B_0L_18000F_2000D_60R_client.txt` >> 150ms/retransmission_data.txt

sleep 1s

echo "\n150ms/RELIABLE, 0.01% loss" >> 150ms/retransmission_data.txt
echo `python3 150ms/retransmission_parser.py 150ms/RELIABLE_3B_001L_18000F_2000D_60R_server.txt 150ms/RELIABLE_3B_001L_18000F_2000D_60R_client.txt` >> 150ms/retransmission_data.txt

sleep 1s

echo "\n150ms/RELIABLE, 0.1% loss" >> 150ms/retransmission_data.txt
echo `python3 150ms/retransmission_parser.py 150ms/RELIABLE_3B_01L_18000F_2000D_60R_server.txt 150ms/RELIABLE_3B_01L_18000F_2000D_60R_client.txt` >> 150ms/retransmission_data.txt

sleep 1s

echo "\n150ms/RELIABLE, 1% loss" >> 150ms/retransmission_data.txt
echo `python3 150ms/retransmission_parser.py 150ms/RELIABLE_3B_1L_18000F_2000D_60R_server.txt 150ms/RELIABLE_3B_1L_18000F_2000D_60R_client.txt` >> 150ms/retransmission_data.txt

sleep 1s

echo "\n150ms/RELIABLE, 3% loss" >> 150ms/retransmission_data.txt
echo `python3 150ms/retransmission_parser.py 150ms/RELIABLE_3B_1L_18000F_2000D_60R_server.txt 150ms/RELIABLE_3B_1L_18000F_2000D_60R_client.txt` >> 150ms/retransmission_data.txt

sleep 1s






