# 使用官方FastAPI的基礎映像
FROM python:3.9-slim

# 設置工作目錄
WORKDIR /app

# 複製當前目錄的內容到工作目錄
COPY . /app

# 安裝依賴
RUN pip install --no-cache-dir -r requirements.txt

# 暴露端口
EXPOSE 8000

# 啟動命令
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
