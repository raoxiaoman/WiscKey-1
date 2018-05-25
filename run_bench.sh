#!/bin/bash
KB=1024
NUM=1000000
#NUM=10000
#NUM=10000000
LBENCH_BIN=./out-static/db_bench
#BENCHMARKS="fillseq,fillrandom,overwrite,readrandom,readseq,seekrandom,compact,readrandom,readseq"
#BENCHMARKS="fillseq,seekrandom,compact,seekrandom"
BENCHMARKS="fillseq,fillrandom,overwrite,readrandom,readseq,seekrandom,compact,readrandom,readseq,seekrandom"
#BENCHMARKS="fillseq,readrandom"
USE_EXISTING_DB=0
#VALUE_SIZE=4096
DB=../wiskkey_db_test


if [ -n "$BENCHMARKS" ]; then
    ARGS="$ARGS --benchmarks=$BENCHMARKS"
fi
if [ -n "$USE_EXISTING_DB" ]; then
    ARGS="$ARGS --use_existing_db=$USE_EXISTING_DB"
fi
if [ -n "$NUM" ]; then
    ARGS="$ARGS --num=$NUM"
fi
if [ -n "$READ" ]; then
    ARGS="$ARGS --reads=$READ"
fi
if [ -n "$THREADS" ]; then
    ARGS="$ARGS --threads=$THREADS"
fi
if [ -n "$VALUE_SIZE" ]; then
    ARGS="$ARGS --value_size=$VALUE_SIZE"
fi
if [ -n "$WRITE_BUFFER_SIZE" ]; then
    ARGS="$ARGS --write_buffer_size=$WRITE_BUFFER_SIZE"  
fi
if [ -n "$BLOCK_SIZE" ]; then
    ARGS="$ARGS --block_size=$BLOCK_SIZE"
fi
if [ -n "$CACHE_SIZE" ]; then
    ARGS="$ARGS --cache_size=$CACHE_SIZE"        
fi
if [ -n "$BLOOM_BIT" ]; then
    ARGS="$ARGS --bloom_bits=$BLOOM_BIT"
fi
if [ -n "$OPEN_FILES" ]; then
    ARGS="$ARGS -open_files=$OPEN_FILES"
fi
if [ -n "$DB" ]; then
    ARGS="$ARGS --db=$DB"
fi

LBENCH_CMD="$LBENCH_BIN $ARGS"

rm -rf ../wiskkey_db_test/*
echo "$LBENCH_CMD"
eval "$LBENCH_CMD"
