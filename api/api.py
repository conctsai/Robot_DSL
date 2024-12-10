from fastapi import APIRouter
from fastapi.responses import JSONResponse
from controller.session_controller import SessionController
from typing import List
from error.controller_runtime_error import ConfNotFoundError, SessionNotFoundError
from error.dsl_runtime_error import DSLRuntimeError
from error.parse_error import ParseError

sc = SessionController() # 会话控制器
api_router = APIRouter() # API路由

@api_router.post("/create_session")
def create_session(conf_name: str):
    '''
    创建会话
    :param conf_name: 配置文件名
    '''
    try:
        return JSONResponse(
            content={
                "session_id": sc.create_session(conf_name)
            },
            status_code=200
        )
    except ConfNotFoundError as e: # 配置文件不存在
        return JSONResponse(
            content={
                "message": e.message,
            },
            status_code=404
        )
    except ParseError as e: # 解析错误
        return JSONResponse(
            content={
                "message": e.message,
            },
            status_code=500
        )
    except DSLRuntimeError as e: # DSL运行时错误
        return JSONResponse(
            content={
                "message": e.message,
            },
            status_code=500
        )
    except Exception as e: # 未知错误
        return JSONResponse(
            content={
                "message": str(e),
            },
            status_code=500
        )

@api_router.post("/get_output")
def get_output(session_id: int, input: List[str]):
    '''
    获取输出
    :param session_id: 会话ID
    :param input: 输入
    '''
    try:
        finish, output = sc.get_output(session_id, input)
    except SessionNotFoundError as e: # 会话不存在
        return JSONResponse(
            content={
                "message": e.message,
            },
            status_code=404
        )
    except DSLRuntimeError as e: # DSL运行时错误
        return JSONResponse(
            content={
                "message": e.message,
            },
            status_code=500
        )
    except Exception as e: # 未知错误
        return JSONResponse(
            content={
                "message": str("Unknown error:") + str(e),
            },
            status_code=500
        )
    if finish:
        sc.close_session(session_id) # 如果运行结束，关闭会话
    return JSONResponse(
        content={
            "finish": finish,
            "output": output
        },
        status_code=200
    )
    
@api_router.get("/get_all_conf_name")
def get_all_conf_name():
    '''
    获取所有配置文件名
    '''
    return JSONResponse(
        content={
            "conf_name": sc.conf_controller.get_all_conf_name()
        },
        status_code=200
    )
