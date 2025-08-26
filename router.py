from fastapi import APIRouter

router = APIRouter(prefix='/faastapi_plugin_han_cock')

@router.get('/status')
async def root():
    return {'message': 'Hello from faastapi_plugin_han_cock!'}
