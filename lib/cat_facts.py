import requests

class CatFacts:
    def __init__(self, requester):
        self.requester = requester

    def provide(self):
        return f"Cat fact: {self._get_cat_fact()['fact']}"

    # Again, don't stub this method.
    def _get_cat_fact(self):
        #response = requests.get("https://catfact.ninja/fact")
        response = self.requester.get()
        return response.json()
