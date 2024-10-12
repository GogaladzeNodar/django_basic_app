from django.shortcuts import render, get_list_or_404
from django.http import JsonResponse
from .models import Product, Category

"""შექმენით 2 ვიუ და შესაბამისად განუსაზღვრეთ მისამართებიც(urls),
 ერთი view პასუხისმგებელი უნდა იყოს ყველა კატეგორიის ინფორმაციის დაბრუნებაზე, (კატეგორიას წამოყვეს თავისი მშობელი კატეგორიები, 
 [პირველი დონე]), მეორე ვიუმ უნდა დააბრუნოს პროდუქტების სია თავისი კატეგორიებით[უშუალოდ მშობელი კატეგორიები],
  დაბრუნებული პასუხების ფორმატი უნდა იყოს JSON"""


def AllCategoryView(request):

    categories = {}
    # for category in Category.objects.all():    ---  ase wamogheba N+1 problemastan migviyvans.
    for category in Category.objects.select_related("parent").all():
        categories[category.id] = {
            "name": category.name,
            "description": category.description,
            "parent": category.parent.name if category.parent else None,
            "is_active": category.is_active,
            "created_at": category.created_at,
            "updated_at": category.updated_at,
        }

    return JsonResponse(categories)


def AllProductsView(request):

    products = {}

    for product in Product.objects.prefetch_related("categories").all():
        products[product.id] = {
            "name": product.name,
            "categories": [category.name for category in product.categories.all()],
            "description": product.description,
            "price": product.price,
            "image": product.image.url if product.image else None,
            "stock": product.stock,
            "created_at": product.created_at,
            "updated_at": product.updated_at,
        }

    return JsonResponse(products)
