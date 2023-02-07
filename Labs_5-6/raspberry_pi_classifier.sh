#!/bin/bash

while true; do
  sleep 2.0 &
  echo "##########################################"
  echo ""
  current_time=$(date "+%Y.%m.%d-%H.%M.%S")
  picture_filename=$current_time".jpg"
  echo "Taking picture..."
  raspistill -o "data/pix/"$picture_filename
  echo "Saved picture to: data/pix/"$picture_filename
  python3 elliott_train_test_model.py $picture_filename
  echo "##########################################"
  wait # for sleep
done