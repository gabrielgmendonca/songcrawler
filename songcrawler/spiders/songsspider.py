import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'songs'
    start_urls = [
        'https://www.letras.mus.br/mais-acessadas/mpb/',
    ]

    def parse(self, response):
        artist_links = response.css('.top-list_art a')
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
