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
)

app.mount("/assets", StaticFiles(directory="dist/assets"), name="assets")

app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return FileResponse("dist/index.html")

# 捕获其他所有路由
@app.get("/{path:path}")
async def catch_all(path: str):
    return FileResponse("dist/index.html")

if __name__ == '__main__':
    print("正在进行运行前测试")
    import pytest as ptt
    try:
        run_test()
    except ptt.ExitCode:
        print("运行前测试失败")
        exit(1)
        
    print("运行前测试通过")
    
    uvicorn.run(app, host="127.0.0.1", port=8000)
    
    