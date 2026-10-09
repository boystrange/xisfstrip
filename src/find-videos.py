import argparse
from html.parser import HTMLParser
from pathlib import Path
import sys


class VideoSourceParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.video_depth = 0
        self.urls = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)

        if tag == 'video':
            self.video_depth += 1
            self._add_source(attributes.get('src'))
        elif tag == 'source' and self.video_depth:
            self._add_source(attributes.get('src'))

    def handle_endtag(self, tag):
        if tag == 'video' and self.video_depth:
            self.video_depth -= 1

    def _add_source(self, source):
        if source:
            if source.startswith('//'):
                source = source[2:]
            self.urls.append(source)


def find_video_urls(html_file):
    html = Path(html_file).read_text(encoding='utf-8', errors='replace')
    parser = VideoSourceParser()
    parser.feed(html)
    return parser.urls


def main():
    parser = argparse.ArgumentParser(
        description='Read an HTML file and print URLs from its video elements.'
    )
    parser.add_argument('html_file', help='path to the HTML file to read')
    args = parser.parse_args()

    try:
        video_urls = find_video_urls(args.html_file)
    except OSError as error:
        print(f'Error: {error}', file=sys.stderr)
        return 2

    if not video_urls:
        print('No video URLs found.')
        return 0

    for video_url in video_urls:
        print(video_url)
    return 0


if __name__ == '__main__':
    sys.exit(main())
