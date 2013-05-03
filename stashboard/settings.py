import os

DEBUG = False

SITE_NAME = "Rainforest QA Status"
SITE_AUTHOR = "Russell Smith"
SITE_URL = "http://status.rainforestqa.com"
REPORT_URL = "mailto:team@rainforestqa.com"

# Twitter update settings
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
TWITTER_ACCESS_TOKEN = ''
TWITTER_ACCESS_TOKEN_SECRET = ''
TWITTER_HANDLE = 'rainforestqa'

# RSS Feed settings
RSS_NUM_EVENTS_TO_FETCH = 50

# OAuth Consumer Credentials
CONSUMER_KEY = '4dba98dcc2b271291ff337c7c655a679'
CONSUMER_SECRET = '979e48e67ef0c406bc1762beb9935103962dec8a'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "templates"),
    )
