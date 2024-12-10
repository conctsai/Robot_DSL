from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from api.api import api_router
from test import run_test
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) # 添加CORS中间件

app.mount("/assets", StaticFiles(directory="dist/assets"), name="assets") # 静态文件

app.include_router(api_router, prefix="/api") # API路由

@app.get("/")
async def root():
    '''
    根路由
    '''
    return FileResponse("dist/index.html")

# 捕获其他所有路由
@app.get("/{path:path}")
async def catch_all(path: str):
    return FileResponse("dist/index.html")

if __name__ == '__main__':
    print("正在进行运行前测试")
    import pytest as ptt

    code = run_test()
    
    if code != 0:
        print("运行前测试失败")
        exit(code)
    
    print("运行前测试通过")
    # 启动服务器
    uvicorn.run(app, host="127.0.0.1", port=8000)