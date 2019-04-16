#PARTIALLY RELIABLE DATA GENERATION

#playback buffer of 3 frames, 0.5% loss, 100 frames to send in total, 3000 RTP timestamp increment, quiet mode, send 60 frames per second, partial reliability
../examples/server -b 3 -t 0.005 -l 100 -i 3000 -q -f 60 127.0.0.1 5004 ../test-ca/rsa/ca.key test-ca/rsa/ca.cert > PARTIAL_3B_005L_100F_3000D_60R_server.txt &

../client -b 3 -e -a 3000 -q 127.0.0.1 5004 > PARTIAL_3B_005L_100F_3000D_60R_client.txt &

sleep 1m



#playback buffer of 3 frames, 1% loss, 100 frames to send in total, 3000 RTP timestamp increment, quiet mode, send 60 frames per second, partial reliability
../examples/server -b 3 -t 0.01 -l 100 -i 3000 -q -f 60 127.0.0.1 5004 ../test-ca/rsa/ca.key test-ca/rsa/ca.cert > PARTIAL_3B_01L_100F_3000D_60R_server.txt &

../client -b 3 -e -a 3000 -q 127.0.0.1 5004 > PARTIAL_3B_01L_100F_3000D_60R_client.txt &

sleep 1m



#playback buffer of 3 frames, 1.5% loss, 100 frames to send in total, 3000 RTP timestamp increment, quiet mode, send 60 frames per second, partial reliability
../examples/server -b 3 -t 0.015 -l 100 -i 3000 -q -f 60 127.0.0.1 5004 ../test-ca/rsa/ca.key test-ca/rsa/ca.cert > PARTIAL_3B_015L_100F_3000D_60R_server.txt &

../client -b 3 -e -a 3000 -q 127.0.0.1 5004 > PARTIAL_3B_015L_100F_3000D_60R_client.txt &

sleep 1m



#playback buffer of 3 frames, 2% loss, 100 frames to send in total, 3000 RTP timestamp increment, quiet mode, send 60 frames per second, partial reliability
../examples/server -b 3 -t 0.02 -l 100 -i 3000 -q -f 60 127.0.0.1 5004 ../test-ca/rsa/ca.key test-ca/rsa/ca.cert > PARTIAL_3B_02L_100F_3000D_60R_server.txt &

../client -b 3 -e -a 3000 -q 127.0.0.1 5004 > PARTIAL_3B_02L_100F_3000D_60R_client.txt &

sleep 1m



#playback buffer of 3 frames, 2% loss, 100 frames to send in total, 3000 RTP timestamp increment, quiet mode, send 60 frames per second, partial reliability
../examples/server -b 3 -t 0.02 -l 100 -i 3000 -q -f 60 127.0.0.1 5004 ../test-ca/rsa/ca.key test-ca/rsa/ca.cert > PARTIAL_3B_02L_100F_3000D_60R_server.txt &

../client -b 3 -e -a 3000 -q 127.0.0.1 5004 > PARTIAL_3B_02L_100F_3000D_60R_client.txt &

sleep 1m



#playback buffer of 3 frames, 2% loss, 100 frames to send in total, 3000 RTP timestamp increment, quiet mode, send 60 frames per second, partial reliability
../examples/server -b 3 -t 0.02 -l 100 -i 3000 -q -f 60 127.0.0.1 5004 ../test-ca/rsa/ca.key test-ca/rsa/ca.cert > PARTIAL_3B_02L_100F_3000D_60R_server.txt &

../client -b 3 -e -a 3000 -q 127.0.0.1 5004 > PARTIAL_3B_02L_100F_3000D_60R_client.txt &

sleep 1m



#playback buffer of 3 frames, 2.5% loss, 100 frames to send in total, 3000 RTP timestamp increment, quiet mode, send 60 frames per second, partial reliability
../examples/server -b 3 -t 0.025 -l 100 -i 3000 -q -f 60 127.0.0.1 5004 ../test-ca/rsa/ca.key test-ca/rsa/ca.cert > PARTIAL_3B_025L_100F_3000D_60R_server.txt &

../client -b 3 -e -a 3000 -q 127.0.0.1 5004 > PARTIAL_3B_025L_100F_3000D_60R_client.txt &

sleep 1m



#playback buffer of 3 frames, 3% loss, 100 frames to send in total, 3000 RTP timestamp increment, quiet mode, send 60 frames per second, partial reliability
../examples/server -b 3 -t 0.03 -l 100 -i 3000 -q -f 60 127.0.0.1 5004 ../test-ca/rsa/ca.key test-ca/rsa/ca.cert > PARTIAL_3B_03L_100F_3000D_60R_server.txt &

../client -b 3 -e -a 3000 -q 127.0.0.1 5004 > PARTIAL_3B_03L_100F_3000D_60R_client.txt &

sleep 1m



#playback buffer of 3 frames, 3.5% loss, 100 frames to send in total, 3000 RTP timestamp increment, quiet mode, send 60 frames per second, partial reliability
../examples/server -b 3 -t 0.035 -l 100 -i 3000 -q -f 60 127.0.0.1 5004 ../test-ca/rsa/ca.key test-ca/rsa/ca.cert > PARTIAL_3B_035L_100F_3000D_60R_server.txt &

../client -b 3 -e -a 3000 -q 127.0.0.1 5004 > PARTIAL_3B_035L_100F_3000D_60R_client.txt &

sleep 1m



#playback buffer of 3 frames, 4% loss, 100 frames to send in total, 3000 RTP timestamp increment, quiet mode, send 60 frames per second, partial reliability
../examples/server -b 3 -t 0.04 -l 100 -i 3000 -q -f 60 127.0.0.1 5004 ../test-ca/rsa/ca.key test-ca/rsa/ca.cert > PARTIAL_3B_04L_100F_3000D_60R_server.txt &

../client -b 3 -e -a 3000 -q 127.0.0.1 5004 > PARTIAL_3B_04L_100F_3000D_60R_client.txt &

sleep 1m



#playback buffer of 3 frames, 4.5% loss, 100 frames to send in total, 3000 RTP timestamp increment, quiet mode, send 60 frames per second, partial reliability
../examples/server -b 3 -t 0.045 -l 100 -i 3000 -q -f 60 127.0.0.1 5004 ../test-ca/rsa/ca.key test-ca/rsa/ca.cert > PARTIAL_3B_045L_100F_3000D_60R_server.txt &

../client -b 3 -e -a 3000 -q 127.0.0.1 5004 > PARTIAL_3B_045L_100F_3000D_60R_client.txt &

sleep 1m



#playback buffer of 3 frames, 5% loss, 100 frames to send in total, 3000 RTP timestamp increment, quiet mode, send 60 frames per second, partial reliability
../examples/server -b 3 -t 0.05 -l 100 -i 3000 -q -f 60 127.0.0.1 5004 ../test-ca/rsa/ca.key test-ca/rsa/ca.cert > PARTIAL_3B_05L_100F_3000D_60R_server.txt &

../client -b 3 -e -a 3000 -q 127.0.0.1 5004 > PARTIAL_3B_05L_100F_3000D_60R_client.txt &

sleep 1m
