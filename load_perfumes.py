from shop.models import Perfume

products = [
    {
        'name': 'Amber Horizon',
        'description': 'Amber Horizon is a unique blend of sophistication and allure.',
        'price': 50.08,
        'stock': 12,
        'image': 'perfumes/single-product-website-template.jpg'
    },
    {
        'name': 'Black Thorn',
        'description': 'Black Thorn is a unique blend of sophistication and allure.',
        'price': 101.45,
        'stock': 16,
        'image': 'perfumes/bg.png'
    },
    {
        'name': 'Tidal Drift',
        'description': 'Tidal Drift is a unique blend of sophistication and allure.',
        'price': 101.71,
        'stock': 16,
        'image': 'perfumes/Black thorn bottle.png'
    },
    {
        'name': 'Iris Glow',
        'description': 'Iris Glow is a unique blend of sophistication and allure.',
        'price': 112.33,
        'stock': 17,
        'image': 'perfumes/Fragora [ A3 ] Print.jpg'
    },
    {
        'name': 'Misty Grove',
        'description': 'Misty Grove is a unique blend of sophistication and allure.',
        'price': 97.94,
        'stock': 7,
        'image': 'perfumes/FRAGORA [ LOGO ] Png.png'
    },
    {
        'name': 'Velvet Bloom',
        'description': 'Velvet Bloom is a unique blend of sophistication and allure.',
        'price': 53.16,
        'stock': 7,
        'image': 'perfumes/Amber Horizon [ Bottle ].png'
    },
    {
        'name': 'Sapphire Rain',
        'description': 'Sapphire Rain is a unique blend of sophistication and allure.',
        'price': 68.88,
        'stock': 9,
        'image': 'perfumes/Black Thorn 00 [ Bottle ].png'
    },
    {
        'name': 'Crimson Silk',
        'description': 'Crimson Silk is a unique blend of sophistication and allure.',
        'price': 87.24,
        'stock': 6,
        'image': 'perfumes/Black Thorn [ Bottle ].png'
    },
    {
        'name': 'Golden Dusk',
        'description': 'Golden Dusk is a unique blend of sophistication and allure.',
        'price': 51.84,
        'stock': 10,
        'image': 'perfumes/Citrine Sky [ Bottle ].png'
    },
    {
        'name': 'Midnight Ember',
        'description': 'Midnight Ember is a unique blend of sophistication and allure.',
        'price': 82.12,
        'stock': 20,
        'image': 'perfumes/Coastal Charm [ Bottle ].png'
    },
]

for p in products:
    Perfume.objects.get_or_create(
        name=p['name'],
        defaults={
            'description': p['description'],
            'price': p['price'],
            'stock': p['stock'],
            'image': p['image']
        }
    )

print("✅ Sample perfumes loaded.")
