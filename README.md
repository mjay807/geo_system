# GEO 智能内容优化平台

基于 Streamlit 的 GEO（Generative Engine Optimization）内容优化工具。

## Docker 运行（推荐）

### 前置要求

- [Docker](https://docs.docker.com/get-docker/) 20.10+
- [Docker Compose](https://docs.docker.com/compose/install/) v2（Docker Desktop 已自带）

### 一键启动

```bash
# 进入项目目录
cd geo_system

# 构建并后台启动
docker compose up -d --build

# 查看日志
docker compose logs -f

# 停止
docker compose down
```

浏览器访问：**http://localhost:8501**

### 仅使用 docker run（不依赖 compose）

```bash
# 构建镜像
docker build -t geo_system:latest .

# 创建本地数据目录
mkdir -p data

# 启动容器
docker run -d \
  --name geo_system \
  -p 8501:8501 \
  -v "$(pwd)/data:/data" \
  geo_system:latest

# 查看日志
docker logs -f geo_system

# 停止并删除容器
docker stop geo_system && docker rm geo_system
```

### 配置 API Key（可选）

```bash
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
# 编辑 .streamlit/secrets.toml 填入 API Key
```

使用 Compose 时，取消 `docker-compose.yml` 里 `secrets.toml` 那一行 volume 的注释后重启：

```bash
docker compose up -d --build
```

或在 `docker run` 时增加挂载：

```bash
docker run -d \
  --name geo_system \
  -p 8501:8501 \
  -v "$(pwd)/data:/data" \
  -v "$(pwd)/.streamlit/secrets.toml:/app/.streamlit/secrets.toml:ro" \
  geo_system:latest
```

### 数据持久化

| 宿主机路径 | 容器路径 | 说明 |
|-----------|---------|------|
| `./data/geo_data.db` | `/data/geo_data.db` | SQLite 业务数据 |
| `./data/knowledge_base/` | `/data/knowledge_base/` | 品牌知识库文件 |

删除容器不会丢失 `./data` 目录中的数据。

---

## 本地运行（不用 Docker）

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -r requirements.txt
streamlit run geo_tool.py
```

访问：**http://localhost:8501**
