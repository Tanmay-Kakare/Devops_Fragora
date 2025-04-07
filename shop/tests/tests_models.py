import pytest
from shop.models import Perfume

@pytest.mark.django_db
def test_perfume_creation():
    perfume = Perfume.objects.create(
        name="Test Perfume",
        description="Test Desc",
        price=100.0,
        stock=10
    )
    assert perfume.name == "Test Perfume"
    assert perfume.price == 100.0
  