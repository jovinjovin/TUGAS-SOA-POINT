from nameko.web.handlers import http
from werkzeug.wrappers import Response
import uuid
import json
from nameko.rpc import RpcProxy

from session import SessionProvider

class Service:
    name = "gateway_service"

    session_provider = SessionProvider()
    news_rpc = RpcProxy('news_service')

    @http('POST', '/register')
    def register(self, request):
        user_data = []
        user_data.append(request.json['username'])
        response = Response('Register Berhasil')
        return response
    
    @http('POST', '/login')
    def login(self, request):
        user_data = {
            'id': request.json['id'],
            'username': request.json['username']
        }
        session_id = self.session_provider.set_session(user_data)
        response = Response(str(user_data))
        response.set_cookie('SESSID', session_id)
        return response

    @http('POST', '/logout')
    def logout(self, request):
        cookies = request.cookies
        if cookies:
            session_data = self.session_provider.delete_session(cookies['SESSID'])
            response = Response('Logout Berhasil')
            return response
        else:
            response = Response('Login Dulu!')
            return response

    @http('POST', '/add')
    def add_news(self, request):
        cookies = request.cookies
        if cookies:
            data = request.json
            result = self.news_rpc.add_news(data['judul'], data['isi'], data['gambar'])
            return result
        else:
            response = Response('Login Dulu!')
            return response

    @http('POST', '/edit')
    def edit_news(self, request):
        cookies = request.cookies
        if cookies:
            data = request.json
            result = self.news_rpc.edit_news(data['judul'], data['isi'], data['gambar'])
            return result
        else:
            response = Response('Login Dulu!')
            return response

    @http('POST', '/getall')
    def get_all_news(self, request):
        data = request.json
        result = self.news_rpc.get_all_news()
        return json.dumps(result)

    @http('POST', '/getbyid')
    def get_news_by_id(self, request):
        data = request.json
        result = self.news_rpc.get_news_by_id(data['id'])
        return json.dumps(result)

    @http('POST', '/delete')
    def delete_news(self, request):
        cookies = request.cookies
        if cookies:
            data = request.json
            result = self.news_rpc.delete_news(data['id'])
            return json.dumps(result)
        else:
            response = Response('Login Dulu!')
            return response
            
    @http('POST', '/download')
    def download_file_by_id(self, request):
        data = request.json
        result = self.news_rpc.download_file_by_id(data['id'])
        return json.dumps(result)