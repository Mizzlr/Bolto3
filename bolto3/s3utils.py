import re
import logging

try:
    # Python 2.7
    from urlparse import urlparse
except ImportError:
    # Python 3.x
    from urllib.parse import urlparse

class S3UrlParserError(Exception): pass

class S3UrlParseResult(object):
    def __init__(self, scheme, region, bucket, key):
        self.scheme = scheme
        self.bucket = bucket
        self.region = region
        self.key = key

    def __repr__(self):
        if not self.region:
            self.region = ''

        return '{}(scheme="{}", region="{}", bucket="{}", key="{}")'\
            .format(self.__class__.__name__, self.scheme, self.region,
                    self.bucket, self.key)

class S3UrlParser(object):
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def parse_s3_url(self, s3_url):
        """Parses given `s3_url` and return an S3UrlParseResult object.
        """

        self.logger.debug('Parsing S3 URL: {}'.format(s3_url))

        parse_result = urlparse(s3_url)

        scheme = parse_result.scheme
        if parse_result.scheme == 's3':
            bucket = parse_result.netloc
            key = parse_result.path.lstrip('/')

        else:
            path = parse_result.path.lstrip('/')
            if not ('.s3' in parse_result.netloc and \
                    parse_result.netloc.endswith('.amazonaws.com')):
                bucket = parse_result.netloc.split('.', maxsplit=1)[0]
                key = path
            else:
                bucket, key = path.split('/', maxsplit=1)

        self.logger.info('Bucket: {}, Key: {}'.format(bucket, key))
        return S3UrlParseResult(scheme=scheme, region=None,
                                bucket=bucket, key=key)

    def format_s3_url(bucket, key, region=None, format=None):
        pass

if __name__ == '__main__':
    print(S3UrlParser().parse_s3_url('http://bucket.s3-us-east-1.amazonaws.com/prefix/key.zip'))
