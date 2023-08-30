from fastapi import FastAPI

app = FastAPI(
    title='python-users',
)


@app.get('/')
async def root():

    return {'message': 'Hello, python-users'}
