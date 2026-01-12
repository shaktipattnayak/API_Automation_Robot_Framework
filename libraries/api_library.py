# import json
# import requests
# import yaml
# from jsonschema import validate, ValidationError


# class PostsLibrary:
#     """Robot Framework library providing simple API keywords for Posts endpoints."""

#     def __init__(self, config_path="config/config.yaml"):
#         with open(config_path, "r", encoding="utf-8") as f:
#             cfg = yaml.safe_load(f)
#         self.base_url = cfg.get("base_url")
#         self.timeout = cfg.get("timeout", 10)
#         self.session = requests.Session()

#     def get_all_posts(self):
#         """Returns status code and parsed JSON for GET /posts"""
#         resp = self.session.get(f"{self.base_url}/posts", timeout=self.timeout)
#         return int(resp.status_code), resp.json()

#     # alias kept for backwards compatibility with test naming
#     def get_posts(self):
#         return self.get_all_posts()

#     def get_post_by_id(self, post_id):
#         """Returns status code and parsed JSON for GET /posts/{id}"""
#         resp = self.session.get(f"{self.base_url}/posts/{post_id}", timeout=self.timeout)
#         return int(resp.status_code), resp.json()

#     def validate_schema(self, data, schema_file="schema/schema_posts.json"):
#         """Validates a dict `data` against a local JSON schema file.

#         Raises jsonschema.ValidationError if invalid, which will fail the Robot test.
#         """
#         with open(schema_file, "r", encoding="utf-8") as f:
#             schema = json.load(f)
#         validate(instance=data, schema=schema)
#         return True


import os
import json
from requests import Session

class ApiLibrary:
    def __init__(self):
        self.base_url = os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")
        self.session = Session()

    def get_posts(self):
        return self.session.get(f"{self.base_url}/posts")

    def get_post(self, post_id):
        return self.session.get(f"{self.base_url}/posts/{post_id}")

    def get_posts_json(self):
        """Return the JSON-decoded body for GET /posts"""
        return self.get_posts().json()

    def validate_json_schema(self, response_or_obj, schema_file):
        from jsonschema import validate
        # Accept either a requests.Response or a plain Python object (dict/list)
        if hasattr(response_or_obj, "json"):
            body = response_or_obj.json()
        else:
            body = response_or_obj
        schema = json.load(open(schema_file))
        validate(instance=body, schema=schema)


# Module-level convenience functions so this module can be imported as a Robot library
_api = ApiLibrary()

def get_posts():
    return _api.get_posts()


def get_post(post_id):
    return _api.get_post(post_id)


def get_posts_json():
    return _api.get_posts_json()


def validate_json_schema(response_or_obj, schema_file):
    return _api.validate_json_schema(response_or_obj, schema_file)
