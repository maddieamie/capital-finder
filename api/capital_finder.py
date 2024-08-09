from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        # query capital, name
        # /capital-finder?country=Chile -> https://restcountries.com/v3.1/name/{name}
        # /capital-finder?capital=Santiago -> https://restcountries.com/v3.1/capital/{capital}
        # filter response https://restcountries.com/v3.1/all?fields=name,capital

        if "query" in dic:
            query_value = dic["query"].strip()

            if "country" in query_value.lower():
                country_name = query_value.split('=')[1]
                url = f"https://restcountries.com/v3.1/name/{country_name}?fields=name,capital"

            elif "capital=" in query_value.lower():
                capital_name = query_value.split('=')[1]
                url = f"https://restcountries.com/v3.1/capital/{capital_name}?fields=name,capital"
            else:
                # api just tries whatever as a country
                url = f"https://restcountries.com/v3.1/name/{query_value}?fields=name,capital"

            r = requests.get(url)

            if r.status_code != 200:
                # tries for capital if unspecified query fails as a country
                url = f"https://restcountries.com/v3.1/capital/{query_value}?fields=name,capital"

                r = requests.get(url)

            if r.status_code == 200:

                data = r.json()

                for country_data in data:
                    country_name = country_data["name"][0]
                    capital = country_data["capital"][0]

                    if dic["query"] == country_name:
                        message = f'The capital of {country_name.title()} is {capital.title()}.'
                        break
                    elif dic["query"] == capital:
                        message = f'{capital.title()} is the capital of {country_name.title()}.'
                        break
                    else:
                        message = "No results found for the query provided."
        else:
            message = """Query did not produce results, please enter either a country name 
            or the name of a capital of a country."""

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return
