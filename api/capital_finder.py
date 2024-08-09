from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class Handler(BaseHTTPRequestHandler):
    def get_the_thing(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        # query capital, name
        # /capital-finder?country=Chile -> https://restcountries.com/v3.1/name/{name}
        # /capital-finder?capital=Santiago -> https://restcountries.com/v3.1/capital/{capital}
        # filter response https://restcountries.com/v3.1/all?fields=name,capital

        if "query" in dic:
            url = "https://restcountries.com/v3.1/all?fields=name,capital"
            r = requests.get(url + dic["query"])
            data = r.json()
            # message_thing = []
            for country_data in data:
                country_name = country_data["name"][0]
                capital = country_data["capital"][0]
                # message_thing.append(country_name, capital)

                if dic["query"] == country_name:
                    message = f'The capital of {country_name} is {capital}.'
                elif dic["query"] == capital:
                    message = f'{capital} is the capital of {country_name}'
        else:
            message = """Query did not produce results, please enter either a country name 
            or the name of a capital of a country."""

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return
