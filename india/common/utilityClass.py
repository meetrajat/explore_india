class UtilityClass:
    @staticmethod
    def get_wikipedia_baseurl():
        """
        Returns the base URL for the Wikipedia REST API.
        """
        return "https://en.wikipedia.org/api/rest_v1/page/summary/"