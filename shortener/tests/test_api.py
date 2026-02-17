import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from shortener.models import Short


@pytest.mark.django_db
class TestCreateShortURL:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = APIClient()
        self.url = reverse("shortener:short-create")

    @pytest.mark.parametrize(
        "payload, expected_status",
        [
            ({"url": "https://example.com"}, 201),  # valid-https
            ({"url": "http://google.com"}, 201),  # valid-http
            ({}, 400),  # missing-field
            ({"url": ""}, 400),  # empty-string
            ({"url": "   "}, 400),  # only-spaces
            ({"url": "not-a-url"}, 400),  # not-url
            ({"url": "www.google.com"}, 400),  # no-scheme
            ({"url": "ftp://example.com"}, 400),  # wrong-scheme
            ({"url": "https://example.com/" + "a" * 5000}, 400),  # very-long-url
            ({"url": "https://exa<>mple.com"}, 400),  # invalid-chars
            ({"url": "https://żółć.pl"}, 201),  # unicode-domain
            ({"url": "<script>alert(1)</script>"}, 400),  # xss-attempt
        ],
        ids=[
            "valid-https",
            "valid-http",
            "missing-field",
            "empty-string",
            "only-spaces",
            "not-url",
            "no-scheme",
            "wrong-scheme",
            "very-long-url",
            "invalid-chars",
            "unicode-domain",
            "xss-attempt",
        ],
    )
    def test_create_short_url(self, payload, expected_status):
        response = self.client.post(self.url, payload, format="json")
        assert response.status_code == expected_status

    def test_create_short_url_and_no_duplicate(self):
        payload = {"url": "https://example.com"}
        response_first = self.client.post(self.url, payload, format="json")

        response_sec = self.client.post(self.url, payload, format="json")

        assert response_first.status_code == 201
        assert response_sec.status_code == 201
        assert response_first.data["code"] == response_sec.data["code"]
        assert len(Short.objects.all()) == 1


@pytest.mark.django_db
class TestGetShortURL:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = APIClient()
        self.url = reverse("shortener:short-create")

    @pytest.mark.parametrize(
        "url, code, expected_status",
        [
            ("https://example.com", "code123", 302),  # valid-https
            ("http://google.com", "code123", 302),  # valid-http
            ("www.google.com", "code123", 302),  # no-scheme
            ("ftp://example.com", "code123", 302),  # wrong-scheme
            ("https://example.com/" + "a" * 5000, "code123", 302),  # very-long-url
        ],
        ids=[
            "valid-https",
            "valid-http",
            "no-scheme",
            "wrong-scheme",
            "very-long-url",
        ],
    )
    def test_redirect_short_link(self, url, code, expected_status):
        obj = Short.objects.create(url=url, code=code)

        redirect_url = reverse("shortener:short-redirect", kwargs={"code": code})

        response = self.client.get(redirect_url)

        assert response.status_code == expected_status

        if expected_status == 302:
            assert response.url == url
