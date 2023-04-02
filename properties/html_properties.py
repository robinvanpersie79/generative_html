class HTMLProperties:

    SPECIAL_TOKENS = [
        '[UNK]', '[CLS]', '[SEP]', '[PAD]', '[MASK]',
        ' ---scss-start--- ',
        ' ---scss-end--- ',
        ' ---css-start--- ',
        ' ---css-end--- ',
        ' ---webpage-start--- ',
        ' ---webpage-end--- ',
        ' ---html-start--- ',
        ' ---html-end--- ',
        ' ---js-start--- ',
        ' ---js-end--- ',
    ]

    @property
    def special_tokens(self):
        return self.SPECIAL_TOKENS

    @property
    def html_tags(self):

        from urllib.request import urlopen

        # import json
        import json
        # store the URL in url as
        # parameter for urlopen
        url = 'https://raw.githubusercontent.com/sindresorhus/html-tags/main/html-tags.json'

        # store the response of URL
        response = urlopen(url)

        # storing the JSON response
        # from url in data
        return json.loads(response.read())
