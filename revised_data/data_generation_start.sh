./50ms/data_generation.sh
sleep 1s

echo "50ms processing complete"

./100ms/data_generation.sh
sleep 1s

echo "100ms processing complete"

./150ms/data_generation.sh
sleep 1s

echo "150ms processing complete"

./1hr/50ms/data_generation_1hr.sh
sleep 1s

echo "50ms 1hr processing complete"

./1hr/100ms/data_generation_1hr.sh
sleep 1s

echo "100ms 1hr processing complete"

