# coding:utf-8
# @Time    : 2021/7/15 5:44 下午
# @Author  : liangxinxin
# @Email  : liangxinxina@enn.cn
import json
from sanic import Sanic
from sanic import Blueprint
from sanic.log import logger as LOG
from sanic.response import json, text,file_stream

app = Sanic("hello_sanic")
blueprint = Blueprint('foo',strict_slashes=True)


@app.route("/")
async def test(request):
    LOG.info("hello this is sanic log!")
    print("endpoint", request.endpoint)  # hello_sanic.test
    return json({"hello": "hello sanic!", "url": request.url, "query_string": request.query_string,
                 "args": request.args, "query_args": request.query_args})


@blueprint.get('/index')
async def bar(request): # 声明异步函数，可以中途挂起
    return text(request.endpoint)  # hello_sanic.foo.bar

@app.route('/big_file.png')
async def handle_request(request):
    return await file_stream('/Users/liangxinxin/Desktop/疾病.png/未命名/Canvas 1.png')
@blueprint.get("/r3", strict_slashes=True)
def r3(request):
    return text("strict_slashes applicable from blueprint route level")

@blueprint.get("/r4")
def r3(request):
    return text("strict_slashes applicable from blueprint  level")

if __name__ == "__main__":
    # access_log =True 开启日志
    app.blueprint(blueprint)
    app.run(host="0.0.0.0", port=8000, debug=True, access_log=True)
