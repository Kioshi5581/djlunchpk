from django.urls import path
from django.urls.conf import include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'deals-list', DealViewSet, basename="deals-list"),
router.register(r'frozen-list', FrozenViewSet, basename="frozen-list"),
router.register(r'monthly-package', MonthlyViewSet, basename="monthly"),
router.register(r'users', UserAPI, basename="users"),

# router.register(r'signup', SignupView, basename="signup"),

urlpatterns = [
    path('', index, name="home"),
    path('food-deals/', deals, name="food-deals"),

    # deals api
    path('apioverview/', include(router.urls)),
    path('signup/', SignupView.as_view()),
    # path('deals-detail/<pk>/', DealsDetail.as_view()),
    # path('deals-create/', DealViewSet1.as_view()),
    # path('deals-update/<pk>/', DealsItemUpdate.as_view()),
    # path('deals-delete/<pk>/', DealsItemDelete.as_view()),


    # Frozen deals api
    # path('frozen-list/', frozenList.as_view()),
    # path('frozen-detail/<pk>/', frozenDetail.as_view()),
    # path('frozen-create/', FrozenItemCreate.as_view()),
    # path('frozen-update/<pk>/', FrozenItemUpdate.as_view()),
    # path('frozen-delete/<pk>/', FrozenItemDelete.as_view()),


    path('food-deals/<pk>/', deals_detail, name="deals-details"),
    path('place-an-order/', order_now, name="order-details"),
    path('place-an-order/thank-you/', order_success, name="order"),
    path('frozen/', frozens, name="Frozens"),
    path('frozen/<pk>/', frozens_detail, name="frozen-details"),
    path('make-money/become-a-foodlancer/', bcme_foodlancer, name="foodlancer"),
    path('make-money/apply-for-foodlancer/', apply_foodlancer, name="apply_foodlancer"),
    path('monthly-menu/<pk>/', monthly_menu),
    path('contact/', contact_us),
]



if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)