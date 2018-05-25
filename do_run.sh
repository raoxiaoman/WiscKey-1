#!/bin/bash
#vsizes=(16 32 64 128 256 1024 4096)
vsizes=(256)
for vsize in ${vsizes[@]}; do
   #echo ${VALUE_SIZE}
   #sudo VALUE_SIZE=${vsize} ./run_bench.sh | tee ./test_result/wskey_value${vsize} 
   sudo VALUE_SIZE=${vsize} ./run_bench.sh | tee ./test_result/wskey_value${vsize} 
done
