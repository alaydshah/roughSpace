from typing import Optional, List

import requests
from requests.exceptions import HTTPError, Timeout
from requests.auth import HTTPBasicAuth

URLs = ["https://api.github.com/invalid", "https://api.github.com"]
URL = "https://httpbin.org"
DATA = {"key": "value"}


def urls_basics():
    for url in URLs:
        try:
            response = requests.get(url)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        else:
            print("Success!")
            print(type(response.content), response.content)
            print(type(response.text), response.text)
            print(type(response.json()), response.json())
            print(response.json()["emojis_url"])
            print(type(response.headers), response.headers)
            print(response.headers['content-type'])


def query_popular_python_repositories() -> Optional[List]:
    try:
        # Pass params as dict
        response = requests.get("https://api.github.com/search/repositories",
                                params={"q": "language:python", "sort": "stars", "order": "desc"})
        # Pass params as list of tuples
        # response = requests.get("https://api.github.com/search/repositories",
        #                         params=[("q", "language:python"), ("sort", "stars"), ("order", "desc")])
        # Pass params as bytes:
        # response = requests.get("https://api.github.com/search/repositories",
        #                         params=b"q=language:python&sort=stars&order=desc")
        response.raise_for_status()
    except Exception as e:
        print(f"Exception occurred: {e}")
        return []
    return response.json()["items"]


def query_text_match():
    try:
        response = requests.get("https://api.github.com/search/repositories",
                                params={"q": "real python"},
                                headers={"Accept": "application/vnd.github.text-match+json"})
        response.raise_for_status()
    except Exception as e:
        print(f"Execption: {e}")
        return None
    if response:
        return response.json()["items"][0]["text_matches"][0]["matches"]


def get_popular_python_projects():
    repositories = query_popular_python_repositories()
    for repo in repositories[:3]:
        print(f"Name: {repo['name']}")
        print(f"Description: {repo['description']}")
        print(f"Stars: {repo['stargazers_count']}")


def http_methods():
    print(f'GET -- requests.get(url): {requests.get(URL + "/get")}')
    print(f'POST -- requests.post(url, data): {requests.post(URL + "/post", data=DATA)}')
    print(f'PUT -- requests.put(url,data): {requests.put(URL + "/put", data=DATA)}')
    print(f'DELETE -- requests.delete(url): {requests.delete(URL + "/delete", data=DATA)}')
    print(f'HEAD -- requests.head(url): {requests.head(URL + "/get")}')
    print(f'PATCH -- requests.patch(url, data): {requests.patch(URL + "/patch", data=DATA)}')
    print(f'OPTIONS -- requests.options(url): {requests.options(URL + "/get")}')


def inspect_post():
    data_dictionary = {"key": "value"}
    data_tuple = [("key", "value")]
    data_json = {"key": "value"}
    # Send Data as Dictionary
    response = requests.post(URL + "/post", data=data_dictionary)
    json_response = response.json()
    print(json_response["data"], json_response["headers"]["Content-Type"])

    # Send Data as Tuple
    response = requests.post(URL + "/post", data=data_tuple)
    json_response = response.json()
    print(json_response["data"], json_response["headers"]["Content-Type"])

    # Send Data as Json
    response = requests.post(URL + "/post", json=data_json)
    json_response = response.json()
    print(json_response["data"], json_response["headers"]["Content-Type"])
    print(type(response.request), response.request.url, response.request.headers, response.request.body)


def authenticated_requests():
    try:
        # Passing ("user", "passwd") as auth
        response = requests.get(URL + "/basic-auth/user/passwd",
                                auth=("user", "passwd"))

        # Explicitly Basic Authentication
        # response = requests.get(URL + "/basic-auth/user/passwd",
        #                         auth=HTTPBasicAuth("user", "passwd"))
        response.raise_for_status()
    except Exception as e:
        print(f"Exception: {e}")
        return None
    print(response.status_code)
    print(response.request.headers)


def request_with_timeout():
    response = requests.get(URL + "/get", timeout=1)
    print(response)

    connection_timeout, read_timeout = 3, 5
    try:
        response = requests.get(URL + "/get", timeout=(connection_timeout, read_timeout))
    except Timeout:
        print("The request timed out")
    else:
        print("The request did not time out")


if __name__ == "__main__":
    # Get Popular Repositories
    # get_popular_python_projects()

    # Query Match
    # match = query_text_match()
    # if match:
    #     print(match)

    # Common HTTP Methods
    # http_methods()

    # Inspect different ways to pass data in post
    # inspect_post()

    # Authenticated Requests
    # authenticated_requests()

    # Timeout
    request_with_timeout()
