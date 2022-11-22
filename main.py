from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apis.api_base import api_router

# process requests from all origins
def include_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


# API generates a router
def include_router(app):
    app.include_router(api_router)


# start application
def start_application():
    app = FastAPI(title="Mailing Microservice", version="1.0")
    include_cors(app)
    include_router(app)
    return app


app = start_application()
