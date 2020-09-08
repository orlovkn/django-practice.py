from django.urls import path

from products.views import (
    ProductListView,
    ProductDetailSlugView,
    # product_list_view,
    # ProductDetailView,
    # product_detail_view,
    # ProductFeaturedListView,
    # ProductFeaturedDetailView
)

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<slug:slug>/', ProductDetailSlugView.as_view(), name='detail'),
    # path('products/<int:pk>/', ProductDetailView.as_view()),
    # path('featured/', ProductFeaturedListView.as_view()),
    # path('featured/<int:pk>/', ProductFeaturedDetailView.as_view()),
]