import scrapy


class SongsSpider(scrapy.Spider):
    name = 'songs'
    start_urls = [
        'https://www.letras.mus.br/estilos/axe/todosartistas.html',
        'https://www.letras.mus.br/estilos/bossa-nova/todosartistas.html',
        'https://www.letras.mus.br/estilos/brega/todosartistas.html',
        'https://www.letras.mus.br/estilos/forro/todosartistas.html',
        'https://www.letras.mus.br/estilos/funk/todosartistas.html',
        'https://www.letras.mus.br/estilos/gospelreligioso/todosartistas.html',
        'https://www.letras.mus.br/estilos/infantil/todosartistas.html',
        'https://www.letras.mus.br/estilos/jovem-guarda/todosartistas.html',
        'https://www.letras.mus.br/estilos/marchas-hinos/todosartistas.html',
        'https://www.letras.mus.br/estilos/mpb/todosartistas.html',
        'https://www.letras.mus.br/estilos/pagode/todosartistas.html',
        'https://www.letras.mus.br/estilos/samba/todosartistas.html',
        'https://www.letras.mus.br/estilos/samba-enredo/todosartistas.html',
        'https://www.letras.mus.br/estilos/sertanejo/todosartistas.html',
        'https://www.letras.mus.br/estilos/velha-guarda/todosartistas.html',
    ]

    def parse(self, response):
        artist_links = response.css('ul.cnt-list li a')
        yield from response.follow_all(artist_links, self.parse_artist)

    def parse_artist(self, response):
        song_links = response.css('.artista-todas a.song-name')
        yield from response.follow_all(song_links, self.parse_song)

    def parse_song(self, response):
        song_name = response.css('.cnt-head_title h1::text').get().strip()
        song_artist = response.css('.cnt-head_title span::text').get().strip()
        song_writer = (
            response
            .css('.letra-info_comp::text')
            .get()
            .split(':')[1]
            .strip()
        )
        song_lyrics = response.css('.cnt-letra p::text').getall()
        song_lyrics = '\n'.join(
            [self._remove_extra_spaces(verse) for verse in song_lyrics]
        )
        song_genre = (
            response
            .css('a[href*=estilos]')
            .attrib['href']
            .split('/')[-2]
        )
        return {
            'song_name': self._remove_extra_spaces(song_name),
            'song_artist': self._remove_extra_spaces(song_artist),
            'song_writer': self._remove_extra_spaces(song_writer),
            'song_lyrics': song_lyrics,
            'song_genre': song_genre,
        }

    def _remove_extra_spaces(self, s):
        return ' '.join(s.split())
