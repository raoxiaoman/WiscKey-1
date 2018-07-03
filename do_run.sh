#!/bin/bash
vsizes=(16 32 64 128 256 512 1024 2048 4096 8192 16384)
#vsizes=(16 32 64 128 256 512 1024 2048 4096 8192)
#vsizes=(16384) 
for vsize in ${vsizes[@]}; do
   #echo ${VALUE_SIZE}
   #sudo VALUE_SIZE=${vsize} ./run_bench.sh | tee ./test_result/wskey_value${vsize} 
   sudo VALUE_SIZE=${vsize} ./run_bench.sh | tee ./test_result/wskey_value${vsize} 
done
