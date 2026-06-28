# FastAPI Template

這是一個使用 FastAPI + Poetry 建立的基本 API 專案模板，已包含：

- FastAPI app 入口
- Health check API
- Poetry 依賴管理
- Pytest 測試
- Ruff 程式碼檢查
- Dockerfile

## 專案結構

```text
fastapi-template/
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_main.py
├── Dockerfile
├── poetry.lock
├── pyproject.toml
└── README.md
```

## 環境需求

- Python 3.9 以上
- Poetry

確認 Python 版本：

```bash
python3 --version
```

如果尚未安裝 Poetry，可以先安裝：

```bash
python3 -m pip install --user poetry
```

確認 Poetry 是否可用：

```bash
poetry --version
```

## 安裝依賴

進入專案資料夾：

```bash
cd /Users/linyusheng/Documents/Project/fastapi-template
```

安裝專案依賴：

```bash
poetry install
```

## 啟動開發伺服器

```bash
poetry run uvicorn app.main:app --reload
```

啟動後可以打開：

- API 首頁：http://127.0.0.1:8000
- API 文件：http://127.0.0.1:8000/docs
- ReDoc 文件：http://127.0.0.1:8000/redoc
- Health check：http://127.0.0.1:8000/health

## 目前 API

### `GET /`

回傳基本訊息。

```json
{
  "message": "Hello, FastAPI!"
}
```

### `GET /health`

回傳服務健康狀態。

```json
{
  "status": "ok"
}
```

## 執行測試

```bash
poetry run pytest
```

## 程式碼檢查

```bash
poetry run ruff check .
```

如果要自動修正 Ruff 可修的問題：

```bash
poetry run ruff check . --fix
```

## 使用 Docker

建立映像檔：

```bash
docker build -t fastapi-template .
```

啟動容器：

```bash
docker run --rm -p 8000:8000 fastapi-template
```

啟動後打開：

```text
http://127.0.0.1:8000/docs
```

## 新增 API 範例

可以在 `app/main.py` 新增 route：

```python
@app.get("/hello/{name}")
def say_hello(name: str) -> dict[str, str]:
    return {"message": f"Hello, {name}!"}
```

啟動伺服器後打開：

```text
http://127.0.0.1:8000/hello/linyusheng
```

## 常用指令

```bash
# 安裝依賴
poetry install

# 啟動開發伺服器
poetry run uvicorn app.main:app --reload

# 執行測試
poetry run pytest

# 程式碼檢查
poetry run ruff check .

# 進入 Poetry shell
poetry shell
```
