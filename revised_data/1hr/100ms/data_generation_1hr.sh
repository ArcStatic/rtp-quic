###1hr/100ms/PARTIALly 1hr/100ms/RELIABLE
python3 latency_parser_offsets_removed_buffer.py 1hr/100ms/PARTIAL_3B_0L_216000F_2000D_60R_server.txt 1hr/100ms/PARTIAL_3B_0L_216000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py 1hr/100ms/PARTIAL_3B_001L_216000F_2000D_60R_server.txt 1hr/100ms/PARTIAL_3B_001L_216000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py 1hr/100ms/PARTIAL_3B_01L_216000F_2000D_60R_server.txt 1hr/100ms/PARTIAL_3B_01L_216000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py 1hr/100ms/PARTIAL_3B_1L_216000F_2000D_60R_server.txt 1hr/100ms/PARTIAL_3B_1L_216000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py 1hr/100ms/PARTIAL_3B_3L_216000F_2000D_60R_server.txt 1hr/100ms/PARTIAL_3B_3L_216000F_2000D_60R_client.txt

sleep 1s



###fully 1hr/100ms/RELIABLE
python3 latency_parser_offsets_removed_buffer.py 1hr/100ms/RELIABLE_3B_0L_216000F_2000D_60R_server.txt 1hr/100ms/RELIABLE_3B_0L_216000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py 1hr/100ms/RELIABLE_3B_001L_216000F_2000D_60R_server.txt 1hr/100ms/RELIABLE_3B_001L_216000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py 1hr/100ms/RELIABLE_3B_01L_216000F_2000D_60R_server.txt 1hr/100ms/RELIABLE_3B_01L_216000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py 1hr/100ms/RELIABLE_3B_1L_216000F_2000D_60R_server.txt 1hr/100ms/RELIABLE_3B_1L_216000F_2000D_60R_client.txt

sleep 1s

python3 latency_parser_offsets_removed_buffer.py 1hr/100ms/RELIABLE_3B_1L_216000F_2000D_60R_server.txt 1hr/100ms/RELIABLE_3B_1L_216000F_2000D_60R_client.txt

sleep 1s


###fully 1hr/100ms/RELIABLE single offset example
python3 latency_parser_offsets_single.py 1hr/100ms/RELIABLE_3B_3L_216000F_2000D_60R_server.txt 1hr/100ms/RELIABLE_3B_3L_216000F_2000D_60R_client.txt

###fully 1hr/100ms/RELIABLE combined offsets example
python3 1hr/100ms/relative_offsets_combined.py


###retransmissions
###1hr/100ms/PARTIALly 1hr/100ms/RELIABLE
echo "\n1hr/100ms/PARTIAL, 0% loss" >> 1hr/100ms/retransmission_data.txt
echo `python3 1hr/100ms/retransmission_parser.py 1hr/100ms/PARTIAL_3B_0L_216000F_2000D_60R_server.txt 1hr/100ms/PARTIAL_3B_0L_216000F_2000D_60R_client.txt` >> 1hr/100ms/retransmission_data.txt

sleep 1s

echo "\n1hr/100ms/PARTIAL, 0.01% loss" >> 1hr/100ms/retransmission_data.txt
echo `python3 1hr/100ms/retransmission_parser.py1hr/100ms/PARTIAL_3B_001L_216000F_2000D_60R_server.txt 1hr/100ms/PARTIAL_3B_001L_216000F_2000D_60R_client.txt` >> 1hr/100ms/retransmission_data.txt

sleep 1s

echo "\n1hr/100ms/PARTIAL, 0.1% loss" >> 1hr/100ms/retransmission_data.txt
echo `python3 1hr/100ms/retransmission_parser.py 1hr/100ms/PARTIAL_3B_01L_216000F_2000D_60R_server.txt 1hr/100ms/PARTIAL_3B_01L_216000F_2000D_60R_client.txt` >> 1hr/100ms/retransmission_data.txt

sleep 1s

echo "\n1hr/100ms/PARTIAL, 1% loss" >> 1hr/100ms/retransmission_data.txt
echo `python3 1hr/100ms/retransmission_parser.py 1hr/100ms/PARTIAL_3B_1L_216000F_2000D_60R_server.txt 1hr/100ms/PARTIAL_3B_1L_216000F_2000D_60R_client.txt` >> 1hr/100ms/retransmission_data.txt

sleep 1s

echo "\n1hr/100ms/PARTIAL, 3% loss" >> 1hr/100ms/retransmission_data.txt
echo `python3 1hr/100ms/retransmission_parser.py 1hr/100ms/PARTIAL_3B_3L_216000F_2000D_60R_server.txt 1hr/100ms/PARTIAL_3B_3L_216000F_2000D_60R_client.txt` >> 1hr/100ms/retransmission_data.txt

sleep 1s



###fully 1hr/100ms/RELIABLE
echo "\n1hr/100ms/RELIABLE, 0% loss" >> 1hr/100ms/retransmission_data.txt
echo `python3 1hr/100ms/retransmission_parser.py 1hr/100ms/RELIABLE_3B_0L_216000F_2000D_60R_server.txt 1hr/100ms/RELIABLE_3B_0L_216000F_2000D_60R_client.txt` >> 1hr/100ms/retransmission_data.txt

sleep 1s

echo "\n1hr/100ms/RELIABLE, 0.01% loss" >> 1hr/100ms/retransmission_data.txt
echo `python3 1hr/100ms/retransmission_parser.py 1hr/100ms/RELIABLE_3B_001L_216000F_2000D_60R_server.txt 1hr/100ms/RELIABLE_3B_001L_216000F_2000D_60R_client.txt` >> 1hr/100ms/retransmission_data.txt

sleep 1s

echo "\n1hr/100ms/RELIABLE, 0.1% loss" >> 1hr/100ms/retransmission_data.txt
echo `python3 1hr/100ms/retransmission_parser.py 1hr/100ms/RELIABLE_3B_01L_216000F_2000D_60R_server.txt 1hr/100ms/RELIABLE_3B_01L_216000F_2000D_60R_client.txt` >> 1hr/100ms/retransmission_data.txt

sleep 1s

echo "\n1hr/100ms/RELIABLE, 1% loss" >> 1hr/100ms/retransmission_data.txt
echo `python3 1hr/100ms/retransmission_parser.py 1hr/100ms/RELIABLE_3B_1L_216000F_2000D_60R_server.txt 1hr/100ms/RELIABLE_3B_1L_216000F_2000D_60R_client.txt` >> 1hr/100ms/retransmission_data.txt

sleep 1s

echo "\n1hr/100ms/RELIABLE, 3% loss" >> 1hr/100ms/retransmission_data.txt
echo `python3 1hr/100ms/retransmission_parser.py 1hr/100ms/RELIABLE_3B_1L_216000F_2000D_60R_server.txt 1hr/100ms/RELIABLE_3B_1L_216000F_2000D_60R_client.txt` >> 1hr/100ms/retransmission_data.txt

sleep 1s






