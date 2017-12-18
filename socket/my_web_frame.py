'''
这个程序我们来自定义一个web框架，使用的是wsgiref模块，这个模块为web应用提供了
一个接口,通过封装socket网络传输以及http协议来实现，运行服务使用此模块下的make_server类
'''

from wsgiref.simple_server import make_server  # 引用wsgiref模块


# 重写执行函数，函数里面写的是需求，里面有两个参数，缺一不可，一个是environ，一个是start_response
def application(environ, start_response):
    # environ是接收浏览器的请求信息，如果要处理浏览器发过来的请求，可以从这个里面提取
    print(environ)
    # environ以字典的形式封装了浏览器的请求信息，里面包括访问路径，取得访问路径
    path = environ.get('PATH_INFO')
    # 这一步是必须要写的，因为函数给响应的话，必须要按照响应解析的规则写响应头
    start_response('200 OK', [('content-Type', 'text/html')])

    # 可以根据路径的不同选择返回的页面
    if path == '/egon':
        return [b'<h1>hello egon<h1>']
    elif path == '/alex':
        return [b'<h1>hello alex<h1>']


'''实例化make_server类，他有三个参数，一个是域名，一个是端口，还有一个是执行函数的函数名
在这个类里面已经写好了socket传输对象
三者缺一不可，当监听开始后，一旦有浏览器访问绑定的域名和端口，就会执行这个函数'''
t = make_server('127.0.0.1', 8080, application)
if __name__ == '__main__':
    # 开始监听
    t.serve_forever()

"""
这样咱们就写好了一个简易的最小的web框架，我们来梳理一下里面的逻辑：
首先运行程序，会运行程序里面的make_server对象里面的serve_forever()方法，开始无限接听
一旦咱们根据绑定的域名和端口进行访问，就会被接听
接听到之后，就会收到浏览器发来的请求信息，访问页面也是一次请求
然后请求信息被保存到函数的environ里面，程序可以用environ.get()来读取里面的信息
读取信息后可以进行判断，然后根据判断返回响应的信息
如果是<form>表单要提交信息，必须要将域名、端口以及路径赋值给form表单的action属性，
然后给form下的input等标签的name属性赋值，他输入的内容会自动复制给value，
当点击commit按钮时，相当于浏览器重新向服务端发送了一次请求，地址为form表单里面action绑定的域名
同时name属性会和value属性一起打包在environ里面发送
这时处于监听状态的服务端会又接收一次请求，然后根据判断返回响应的数据
这样，服务端和浏览器会通过一次次的请求和响应不断传输数据
"""
