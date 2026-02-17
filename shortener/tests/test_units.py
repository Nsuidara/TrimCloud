# tests/test_models.py
import pytest
from shortener.models import Short
from shortener.utils import generate_code


@pytest.mark.django_db
def test_create_short_url():
    obj = Short.objects.create(url="https://example.com", code="abc123")
    assert obj.code == "abc123"
    assert obj.url == "https://example.com"


def test_generate_code_default_length():
    code = generate_code("https://example.com")
    assert len(code) == 6


@pytest.mark.django_db
def test_create_short_url_no_code():
    obj = Short.objects.create(url="https://example.com", code="")
    assert obj.code == ""
    assert obj.url == "https://example.com"


def test_generate_code_custom_length():
    code = generate_code("https://example.com", length=10)
    assert len(code) == 10
    

def test_generate_code_returns_string():
    code = generate_code("test")
    assert isinstance(code, str)
    
    
def test_generate_code_is_not_deterministic():
    code1 = generate_code("same-value")
    code2 = generate_code("same-value")
    assert code1 != code2
    
@pytest.mark.parametrize("bad_value", [
    123,
    None,
    [],
    {},
    5.5,
])
def test_generate_code_invalid_value_type(bad_value):
    with pytest.raises(TypeError, match="value must be str"):
        generate_code(bad_value)