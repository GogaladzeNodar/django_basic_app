from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Product, Category
from django.db.models import Max, Min, Avg, Sum, F


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


def category_list(request):
    categories = Category.objects.filter(parent__isnull=True)

    for category in categories:
        category.product_count = Product.objects.filter(
            categories__in=category.get_descendants(include_self=True)
        ).count()

    context = {
        "categories": categories,
    }

    return render(request, "store/category_list.html", context)


def category_products(request, category_id):

    category = get_object_or_404(Category, id=category_id)
    descendant_categories = category.get_descendants(include_self=True)

    products = Product.objects.filter(categories__in=descendant_categories).distinct()

    for product in products:
        product.total_value = product.price * product.stock

    paginator = Paginator(products, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    stats = products.aggregate(
        max_price=Max("price"),
        min_price=Min("price"),
        avg_price=Avg("price"),
        total_value=Sum(F("price") * F("stock")),
    )

    context = {
        "category": category,
        "products": page_obj,
        "stats": stats,
    }
    return render(request, "store/category_products.html", context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    context = {
        "product": product,
    }

    return render(request, "store/products_detail.html", context)
