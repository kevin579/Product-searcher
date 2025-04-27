class UrlManager:
    """
    A class to manage URLs during a web crawling process.

    Attributes:
        new_urls (set): 
            A set of URLs yet to be processed.
        old_urls (set): 
            A set of URLs that have already been processed.
    """

    def __init__(self):
        """
        Initialize the UrlManager with empty sets for new and old URLs.
        """
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        """
        Add a single new URL to the new_urls set if it has not been seen before.

        Args:
            url (str): 
                The URL to add.

        Returns:
            None
        """
        if url is None or len(url) == 0:
            return
        if url in self.new_urls or url in self.old_urls:
            return
        self.new_urls.add(url)

    def add_new_urls(self, urls):
        """
        Add multiple new URLs to the new_urls set.

        Args:
            urls (iterable): 
                An iterable (such as a list or set) of URLs to add.

        Returns:
            None
        """
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def get_url(self):
        """
        Retrieve and remove one URL from the new_urls set, 
        adding it to old_urls to mark it as processed.

        Returns:
            str or None: 
                A URL if available; otherwise, None.
        """
        if self.has_new_url():
            url = self.new_urls.pop()
            self.old_urls.add(url)
            return url
        else:
            return None

    def has_new_url(self):
        """
        Check if there are any new URLs available to process.

        Returns:
            bool: 
                True if there are new URLs; False otherwise.
        """
        return len(self.new_urls) > 0
