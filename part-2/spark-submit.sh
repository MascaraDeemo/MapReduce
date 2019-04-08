#!/bin/bash

spark-submit \
    --master yarn \
    --deploy-mode cluster \
    --num-executors 3 \
    --py-files spark.py \
    --input file:///home/hadoop/lab_commons/a1_data/ \
    --output file:///home/hadoop/MapReduce/part-2/spark_result/