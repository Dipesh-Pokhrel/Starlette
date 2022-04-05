from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from starlette.responses import JSONResponse
from starlette.templating import Jinja2Templates
import uvicorn

templates = Jinja2Templates(directory = 'templates')

app = Starlette (debug=True)
app.mount('/static',StaticFiles(directory='statics'), name='static')

@app.route('/')
async def homepage(request):
    template = 'index.html'
    context = {'request': request}
    return templates.TemplateResponse (template, context)

@app.route('/error')
async def homepage(request):
    return RuntimeError({'Oh no':'Error'})

@app.exception_handler(400)
async def not_found (request, exc):
    template = '404.html'
    context = {'request': request}
    return templates.TemplateResponse (template, context, status_code=404)

@app.exception_handler (500)
async def server_error (request, exc):
    template = '500.html'
    context = {'request': request}
    return templates.TemplateResponse (template, context,  status_code = 500)

if __name__ == "__main__":
    uvicorn.run(app,host='localhost', port=8000)