from fastapi import FastAPI

users_app = FastAPI(
    title='python-users',
)


@users_app.get('/')
async def root():

    return {'message': 'Hello, python-users'}
