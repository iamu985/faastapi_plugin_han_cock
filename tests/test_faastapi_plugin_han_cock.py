# from fastapi import FastAPI
# from fastapi.testclient import TestClient
# from faastapi_plugin_han_cock.router import router

# app = FastAPI()
# app.include_router(router)
# client = TestClient(app)

# def test_root():
#     resp = client.get('/faastapi_plugin_han_cock/')
#     assert resp.status_code == 200
#     assert resp.json() == {'message': 'Hello from faastapi_plugin_han_cock!'}
