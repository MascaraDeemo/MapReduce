#!/bin/bash

spark-submit \
    --master local[4] \
    spark.py \
    -input $1 \
    -output $2