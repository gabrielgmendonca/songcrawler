import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'songs'
    start_urls = [
        'https://www.letras.mus.br/chico-buarque/',
        'https://www.letras.mus.br/milton-nascimento/',
        'https://www.letras.mus.br/djavan/',
        'https://www.letras.mus.br/caetano-veloso/',
        'https://www.letras.mus.br/anavitoria/',
        'https://www.letras.mus.br/marisa-monte/',
        'https://www.letras.mus.br/nando-reis/',
        'https://www.letras.mus.br/ze-ramalho/',
        'https://www.letras.mus.br/gilberto-gil/',
        'https://www.letras.mus.br/maria-bethania/',
    ]

    def parse(self, response):
        song_links = response.css('.artista-todas a.song-name')
        yield from response.follow_all(song_links, self.parse_song)

    def parse_song(self, response):
        song_name = response.css('.cnt-head_title h1::text').get().strip()
        song_artist = response.css('.cnt-head_title span::text').get().strip()
        song_writer = (
            response
            .css('.letra-info_comp::text')
            .get()
            .strip()
        )
        song_lyrics = '\n'.join(
            response
            .css('.cnt-letra p::text')
            .getall()
        )

        return {
            'song_name': song_name,
            'song_artist': song_artist,
            'song_writer': song_writer,
            'song_lyrics': song_lyrics,
        }
