# Order API (Python 3.9 + FastAPI)

## 使用的設計模式與SOLID原則

### 設計模式
- **MVC 架構: 將應用劃分為三個層次：**: 
  - Model: 負責數據結構和數據驗證（order_model.py）。
  - View: 負責將數據格式化並返回給客戶端（TBD）。  
  - Controller: 處理 API 請求並調用服務層進行業務邏輯處理（order_controller.py）。
  
- **單例模式 (Singleton): 對於某些服務或資源，當擴展時可以考慮單例模式，以確保只有一個實例負責處理某一部分功能。**

### SOLID原則
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
  - 檢查訂單金額是否大於0。
  - 檢查訂單金額是否小於上限金額(預設2000)。
  - 檢查名字是否包含非英文字母。
  - 檢查名字字首是否非大寫。
  - 將USD貨幣自動轉換成TWD貨幣。
    
    
## 啟動應用
### 先決條件
- **Docker已安裝完成在系統上。**

### 執行步驟

```bash
git clone https://github.com/106318102Ernie/order_system.git
cd order_system
docker-compose up
```

- **應用將運行在http://localhost:8000**
- **你可以通過 http://localhost:8000/docs 查看自動生成的 Swagger 文檔。**

## 測試
該項目包含單元測試來檢查 API 的正確性。測試文件位於 app/tests 目錄中。

### 測試步驟
```bash
docker-compose run app pytest
```
測試包含以下情境：
  - 檢查是否為有效貨幣（支持 TWD, USD）。
  - 檢查訂單金額是否大於0。
  - 檢查訂單金額是否小於上限金額(預設2000)。
  - 檢查名字是否包含非英文字母。
  - 檢查名字字首是否非大寫。
  - 將USD貨幣自動轉換成TWD貨幣。

## Future Work
  - 支持更多貨幣類型: 可以添加更多支持的貨幣類型，並擴展其他種類匯率轉換。
  - 添加訂單狀態: 可以將訂單狀態管理功能納入系統，允許訂單進行不同階段的處理。
  - 身份驗證與授權: 可以增加身份驗證系統來限制對API的訪問，確保只有授權用戶可以創建或查看訂單。

## github連結
https://github.com/106318102Ernie/order_system.git

## 結論
這個 API 示例展示了如何使用 Python 3.9 和 FastAPI 構建一個基於 MVC 架構的訂單檢查與轉換系統。透過 Docker 進行容器化管理，遵循Clean Code 和 SOLID 設計原則，並且使用單元測試保證代碼質量。