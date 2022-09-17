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
        'https://www.letras.mus.br/carlos-drummond-de-andrade/',
        'https://www.letras.mus.br/gonzaguinha/',
        'https://www.letras.mus.br/belchior/',
        'https://www.letras.mus.br/elis-regina/',
        'https://www.letras.mus.br/fagner/',
        'https://www.letras.mus.br/toquinho/',
        'https://www.letras.mus.br/gilsons/',
        'https://www.letras.mus.br/ana-vilela/',
        'https://www.letras.mus.br/seu-jorge/',
        'https://www.letras.mus.br/vanessa-da-mata/',
        'https://www.letras.mus.br/maria-rita/',
        'https://www.letras.mus.br/jorge-vercillo/',
        'https://www.letras.mus.br/maria-gadu/',
        'https://www.letras.mus.br/adriana-calcanhotto/',
        'https://www.letras.mus.br/jorge-ben-jor/',
        'https://www.letras.mus.br/nelson-goncalves/',
        'https://www.letras.mus.br/chico-cesar/',
        'https://www.letras.mus.br/beto-guedes/',
        'https://www.letras.mus.br/zeca-baleiro/',
        'https://www.letras.mus.br/ana-carolina/',
        'https://www.letras.mus.br/lenine/',
        'https://www.letras.mus.br/oswaldo-montenegro/',
        'https://www.letras.mus.br/ney-matogrosso/',
        'https://www.letras.mus.br/tribalistas/',
        'https://www.letras.mus.br/joanna/',
        'https://www.letras.mus.br/roberta-campos/',
        'https://www.letras.mus.br/tie/',
        'https://www.letras.mus.br/geraldo-azevedo/',
        'https://www.letras.mus.br/ivan-lins/',
        'https://www.letras.mus.br/elba-ramalho/',
        'https://www.letras.mus.br/nelsinho-correa/',
        'https://www.letras.mus.br/gal-costa/',
        'https://www.letras.mus.br/geraldo-vandre/',
        'https://www.letras.mus.br/vander-lee/',
        'https://www.letras.mus.br/marcelo-jeneci/',
        'https://www.letras.mus.br/joao-bosco/',
        'https://www.letras.mus.br/flavio-venturini/',
        'https://www.letras.mus.br/marina-lima/',
        'https://www.letras.mus.br/fafa-de-belem/',
        'https://www.letras.mus.br/emilio-santiago/',
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
            .split(':')[1]
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
