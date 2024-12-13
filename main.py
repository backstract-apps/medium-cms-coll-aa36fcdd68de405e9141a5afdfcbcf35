from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - medium-cms-coll-aa36fcdd68de405e9141a5afdfcbcf35',debug=False,docs_url='/admiring-spence-af93e3f2b94511ef9a0c0242ac1200054/docs',openapi_url='/admiring-spence-af93e3f2b94511ef9a0c0242ac1200054/openapi.json')

app.include_router(router, prefix='/admiring-spence-af93e3f2b94511ef9a0c0242ac1200054/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()