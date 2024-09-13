# Order API (Python 3.9 + FastAPI)

## 使用的設計模式與SOLID原則

- **單一職責原則 (SRP)**: 每個class只負責一項功能，如 OrderService 僅處理訂單檢查和轉換邏輯。
- **開放/封閉原則 (OCP)**: 該系統允許擴展，但不修改現有功能。例如可以新增其他貨幣類型或價格邏輯，而不修改現有的檢查邏輯。
- **里氏替換原則 (LSP)**: 各個模型類的實現符合預期行為。例如，Order 模型可以被其他符合要求的訂單擴展繼承。
- **依賴倒置原則 (DIP)**: 控制器不依賴具體的實現，而是依賴抽象。
- **接口隔離原則 (ISP)**: 每個模塊的接口只暴露必要的方法。OrderService 只提供處理訂單的邏輯，而不包含其他不相關的方法。

## 使用技術

- **FastAPI**: 用於構建 API，提供高效且快速的路由處理及內建的 Swagger 文件生成。
- **Python 3.9**: 編寫應用的主要語言。
- **Pydantic**: 用於數據驗證，確保輸入數據格式正確。
- **Docker**: 用於應用容器化，確保環境一致性和便於部署。
- **Docker Compose**: 用於輕鬆啟動和管理 Docker 容器。

## 功能概述

- **POST /api/orders**: 接收並處理訂單數據，進行格式檢查和轉換。
  - 檢查是否為有效貨幣（支持 TWD, USD）。
  - 檢查價格是否大於0。
  - 返回經過處理的訂單數據。
    
    
## 啟動應用

使用Docker運行應用：

```bash
docker-compose up
