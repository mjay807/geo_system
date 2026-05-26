#!/bin/sh
set -e

DATA_DIR="${GEO_DATA_DIR:-/data}"
mkdir -p "$DATA_DIR/knowledge_base"

# 将数据目录链接到应用工作目录，便于持久化挂载
if [ ! -e /app/geo_data.db ]; then
  ln -sf "$DATA_DIR/geo_data.db" /app/geo_data.db
fi
if [ ! -e /app/knowledge_base ]; then
  ln -sf "$DATA_DIR/knowledge_base" /app/knowledge_base
fi

exec streamlit run geo_tool.py \
  --server.address=0.0.0.0 \
  --server.port=8501 \
  --server.headless=true \
  --browser.gatherUsageStats=false
