import uvicorn

if __name__=='__main__':
    uvicorn.run("server:create_app", port=5001, reload=True)