from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from controller.session_controller import SessionController
from typing import List
import uvicorn
from error.controller_runtime_error import ConfNotFoundError, SessionNotFoundError

app = FastAPI()
sc = SessionController()
api_router = APIRouter()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@api_router.post("/create_session")
def create_session(conf_name: str):
    try:
        return JSONResponse(
            content={
                "session_id": sc.create_session(conf_name)
            },
            status_code=200
        )
    except ConfNotFoundError as e:
        return JSONResponse(
            content={
                "message": e.message,
            },
            status_code=404
        )

@api_router.post("/get_output")
def get_output(session_id: int, input: List[str]):
    try:
        finish, output = sc.get_output(session_id, input)
    except SessionNotFoundError as e:
        return JSONResponse(
            content={
                "message": e.message,
            },
            status_code=404
        )
    if finish:
        sc.close_session(session_id)
    return JSONResponse(
        content={
            "finish": finish,
            "output": output
        },
        status_code=200
    )

app.include_router(api_router, prefix='/api')

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)