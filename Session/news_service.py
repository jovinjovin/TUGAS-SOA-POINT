import dependencies

from nameko.rpc import rpc

class NewsService:

    name = 'news_service'

    database = dependencies.Database()

    @rpc
    def add_news(self, judul, isi, gambar):
        news = self.database.add_news(judul, isi, gambar)
        return news

    @rpc
    def edit_news(self, judul, isi, gambar):
        news = self.database.edit_news(judul, isi, gambar)
        return news
    
    @rpc
    def get_all_news(self):
        news = self.database.get_all_news()
        return news

    @rpc
    def get_news_by_id(self, id):
        news = self.database.get_news_by_id(id)
        return news

    @rpc
    def delete_news(self, id):
        news = self.database.delete_news(id)
        return news

    @rpc
    def download_file_by_id(self, id):
        news = self.database.download_file_by_id(id)
        return news