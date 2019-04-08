#!/bin/bash

spark-submit \
    --master local[4] \
    spark.py \
    --input file:///home/hadoop/lab_commons/a1_data/ \
    --output file:///home/hadoop/MapReduce/part-2/spark_result/