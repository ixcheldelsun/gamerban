import pytest
from rest_framework.test import APIRequestFactory


@pytest.fixture
def request_factory(request):
    """API request factory"""
    request_factory = APIRequestFactory()
    if request.cls:
        request.cls.request_factory = request_factory
    return request_factory