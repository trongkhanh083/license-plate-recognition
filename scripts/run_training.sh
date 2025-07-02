#!/usr/bin/env bash
# scripts/run_training.sh
set -e
export PYTHONPATH="$(pwd)"

# Load defaults from configs/default.yaml
RAW_DIR=$(grep '^raw_dir:' configs/default.yaml    | awk '{print $2}')
PLATE_DIR=$(grep '^plate_dir:' configs/default.yaml    | awk '{print $2}')
DETECTED_PLATE_DIR=$(grep '^detected_plate_dir:' configs/default.yaml    | awk '{print $2}')
TEXT_DIR=$(grep '^text_dir:' configs/default.yaml    | awk '{print $2}')

# 1) Find license plate from image
python -m src.plate_detection \
  --raw_dir  "$RAW_DIR" \
  --plate_dir  "$PLATE_DIR" \
  --detected_plate_dir  "$DETECTED_PLATE_DIR" \


# 2) Recognize text from license plate 
python -m src.char_recognition \
  --plate_dir  "$PLATE_DIR" \
  --text_dir  "$TEXT_DIR" \

echo
echo "All done! You finished the License Plate Recognition project. Enjoy your result!"