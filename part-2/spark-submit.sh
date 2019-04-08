#!/bin/bash

spark-submit \
    --master yarn \
    --deploy-mode cluster \
    --num-executors 3 \
    --py-files spark.py \
    -input $1 \
    -output $2