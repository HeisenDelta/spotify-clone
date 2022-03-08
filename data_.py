import requests
from selectolax.lexbor import LexborHTMLParser
import json

HEADERS = ({
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Accept-language': 'en-us, en;q=0.5'
})

class Video:
    def __init__(self, string):
        self.title_ = string['title']['runs'][0]['text']
        self.channel_ = string['longBylineText']['runs'][0]['text']
        self.thumbnail_ = string['thumbnail']['thumbnails'][0]['url']
        self.id_ = string['videoId']
        self.url_ = 'https://www.youtube.com/watch?v=' + self.id_


def get_results_from_keyword(keyword):
    base_url = 'https://www.youtube.com/results?search_query='
    URL = base_url + keyword.lower().replace(' ', '+')

    page = requests.get(URL, headers = HEADERS)
    parser = LexborHTMLParser(page.content)
    scripts = parser.root.css('body script')

    data = max((script.text() for script in scripts), key = len)
    json_text = json.loads(data[data.index('{'): -1])
    
    videos = json_text['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents']

    # formatted = json.dumps(videos, indent = 4)
    # with open('text3.json', 'w') as handle: handle.write(formatted)

    video_objs = []
    for video in videos:
        try: video_objs.append(Video(video['videoRenderer']))
        except KeyError: continue

    for video_obj in video_objs:
        print(video_obj.title_, video_obj.channel_, video_obj.thumbnail_, video_obj.id_, video_obj.url_, sep = '\n')
    print('Number of results:', len(video_objs))

if __name__ == '__main__':
    get_results_from_keyword(keyword = 'best nightcore 2022')
