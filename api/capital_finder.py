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

        if "country" in dic:
            country_name = dic["country"].strip()
            url = f"https://restcountries.com/v3.1/name/{country_name}?fields=name,capital"

        elif "capital" in dic:
            capital_name = dic["capital"].strip()
            url = f"https://restcountries.com/v3.1/capital/{capital_name}?fields=name,capital"
        else:
            # Default case if no recognized query parameter is found
            message = "Please provide a valid query parameter: country or capital."
            self.send_response(400) # Bad Request Code
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(message.encode())
            return

        r = requests.get(url)

        if r.status_code != 200:
            message = "Failed to fetch data from the API."
            self.send_response(500) # Server Error
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(message.encode())
            return

        data = r.json()
        if not data:
            message = "No results for the query provided."
        else:
            country_data = data[0]
            country_name = country_data["name"]["common"]
            capital = country_data["capital"][0] if "capital" in country_data else "No capital found"

            if "country" in dic:
                message = f'The capital of {country_name.title()} is {capital.title()}.'

            elif "capital" in dic:
                message = f'{capital.title()} is the capital of {country_name.title()}.'


        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return
