"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView, ListView
from appe.models import Add_newproduct, Vendor_Addresses
from appe import views
from ecommerce import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
    path('login/', TemplateView.as_view(template_name="logins.html")),
    path('newcustomersignup/', TemplateView.as_view(template_name="customer/customerregister.html")),
    path('customersignup/', views.customersignup),
    path('check_customerotp/', views.check_customerotp),
    path('newcustomerlogin/', TemplateView.as_view(template_name="customer/customerlogin.html"), name='clogin'),
    path('customerindex/', TemplateView.as_view(template_name="customer/customerindex.html")),
    path('customerlogin/', views.customerlogin),
    path('newvendorsignup/', TemplateView.as_view(template_name="registered_Vendor.html")),
    path('vendorsignup/', views.vendorsignup),
    path('check_vendorotp/', views.check_vendorotp),
    path('newvendorlogin/', TemplateView.as_view(template_name="login_Vendor.html"), name='vlogin'),
    path('vendorlogin/', views.vendorlogin),
    # path('index/', TemplateView.as_view(template_name="index.html")),
    # path('products/', TemplateView.as_view(template_name="products.html")),
    path('products/', ListView.as_view(template_name="customer/womens.html", model=Add_newproduct,
                                       queryset=Add_newproduct.objects.filter(TYPE="women"))),
    path('womenclothes_shirts/', ListView.as_view(template_name="customer/womens.html", model=Add_newproduct,
                                                  queryset=Add_newproduct.objects.filter(CATEGORIETYPE='Shirts',
                                                                                         TYPE='women'))),
    path('womenclothes_pants/', ListView.as_view(template_name="customer/womens.html", model=Add_newproduct,
                                                 queryset=Add_newproduct.objects.filter(CATEGORIETYPE='Pants',
                                                                                        TYPE='women'))),
    path('womenaccessories/', ListView.as_view(template_name="customer/womens.html", model=Add_newproduct,
                                               queryset=Add_newproduct.objects.filter(CATEGORIETYPE='Accessories',
                                                                                      TYPE='women'))),
    path('products1/', ListView.as_view(template_name="customer/mens.html", model=Add_newproduct,
                                        queryset=Add_newproduct.objects.filter(TYPE="men"))),
    path('menclothes_shirts/', ListView.as_view(template_name="customer/mens.html", model=Add_newproduct,
                                                queryset=Add_newproduct.objects.filter(CATEGORIETYPE='Shirts',
                                                                                       TYPE='men'))),
    path('menclothes_pants/', ListView.as_view(template_name="customer/mens.html", model=Add_newproduct,
                                               queryset=Add_newproduct.objects.filter(CATEGORIETYPE='Pants',
                                                                                      TYPE='men'))),
    path('menaccessories/', ListView.as_view(template_name="customer/mens.html", model=Add_newproduct,
                                             queryset=Add_newproduct.objects.filter(CATEGORIETYPE='Accessories',
                                                                                    TYPE='men'))),
    path('products2/', ListView.as_view(template_name="customer/kids.html", model=Add_newproduct,
                                        queryset=Add_newproduct.objects.filter(TYPE="kid"))),
    path('kidclothes_shirts/', ListView.as_view(template_name="customer/kids.html", model=Add_newproduct,
                                                queryset=Add_newproduct.objects.filter(CATEGORIETYPE='Shirts',
                                                                                       TYPE='kid'))),
    path('kidclothes_pants/', ListView.as_view(template_name="customer/kids.html", model=Add_newproduct,
                                               queryset=Add_newproduct.objects.filter(CATEGORIETYPE='Pants',
                                                                                      TYPE='kid'))),
    path('kidaccessories/', ListView.as_view(template_name="customer/kids.html", model=Add_newproduct,
                                             queryset=Add_newproduct.objects.filter(CATEGORIETYPE='Accessories',
                                                                                    TYPE='kid'))),
    path('vproducts/', ListView.as_view(template_name="products.html", model=Add_newproduct,
                                       queryset=Add_newproduct.objects.filter(TYPE="women"))),
    path('vwomenclothes_shirts/', ListView.as_view(template_name="products.html", model=Add_newproduct,
                                                  queryset=Add_newproduct.objects.filter(CATEGORIETYPE='Shirts',
                                                                                         TYPE='women'))),
    path('vwomenclothes_pants/', ListView.as_view(template_name="products.html", model=Add_newproduct,
                                                 queryset=Add_newproduct.objects.filter(CATEGORIETYPE='Pants',
                                                                                        TYPE='women'))),
    path('vwomenaccessories/', ListView.as_view(template_name="products.html", model=Add_newproduct,
                                               queryset=Add_newproduct.objects.filter(CATEGORIETYPE='Accessories',
                                                                                      TYPE='women'))),
    path('vproducts1/', ListView.as_view(template_name="products1.html", model=Add_newproduct,
                                       queryset=Add_newproduct.objects.filter(TYPE="women"))),
    path('vmenclothes_shirts/', ListView.as_view(template_name="products1.html", model=Add_newproduct,
                                                queryset=Add_newproduct.objects.filter(CATEGORIETYPE='Shirts',
                                                                                       TYPE='men'))),
    path('vmenclothes_pants/', ListView.as_view(template_name="products1.html", model=Add_newproduct,
                                               queryset=Add_newproduct.objects.filter(CATEGORIETYPE='Pants',
                                                                                      TYPE='men'))),
    path('vmenaccessories/', ListView.as_view(template_name="products1.html", model=Add_newproduct,
                                             queryset=Add_newproduct.objects.filter(CATEGORIETYPE='Accessories',
                                                                                    TYPE='men'))),
    path('vproducts2/', ListView.as_view(template_name="products2.html", model=Add_newproduct,
                                         queryset=Add_newproduct.objects.filter(TYPE="kid"))),
    path('vkidclothes_shirts/', ListView.as_view(template_name="products2.html", model=Add_newproduct,
                                                queryset=Add_newproduct.objects.filter(CATEGORIETYPE='Shirts',
                                                                                       TYPE='kid'))),
    path('vkidclothes_pants/', ListView.as_view(template_name="products2.html", model=Add_newproduct,
                                               queryset=Add_newproduct.objects.filter(CATEGORIETYPE='Pants',
                                                                                      TYPE='kid'))),
    path('vkidaccessories/', ListView.as_view(template_name="products2.html", model=Add_newproduct,
                                             queryset=Add_newproduct.objects.filter(CATEGORIETYPE='Accessories',
                                                                                    TYPE='kid'))),

    # path('products1/', TemplateView.as_view(template_name="products1.html")),
    # path('products2/', TemplateView.as_view(template_name="products2.html")),
    path('mail/', TemplateView.as_view(template_name="customer/contact.html")),
    path('vmail/', TemplateView.as_view(template_name="mail.html")),
    path('dashboard/', TemplateView.as_view(template_name="dashboard.html")),
    path('customerdashboard/', TemplateView.as_view(template_name="customer/customer_dashboard.html")),
    path('yourproducts/', TemplateView.as_view(template_name="your_Products.html")),
    path('previousproducts/', TemplateView.as_view(template_name="previous_Products.html")),
    path('addnewproducts/', TemplateView.as_view(template_name="addnew_Product.html")),
    path('addnewproduct/', views.addnewproduct),
    path('inventory/', TemplateView.as_view(template_name="inventory.html")),
    path('soldproducts/', TemplateView.as_view(template_name="sold_Product.html")),
    path('returnproducts/', TemplateView.as_view(template_name="return_Product.html")),
    path('youraddresses/', ListView.as_view(template_name="your_Address.html", model=Vendor_Addresses)),
    path('addnewaddress/', TemplateView.as_view(template_name="addnew_Address.html")),
    path('saveaddress/', views.saveaddress),
    path('manageaddress/', ListView.as_view(template_name="manage_Address.html", model=Vendor_Addresses)),
    path('updateaddress/', views.update_address, name='updateaddress'),
    path('update_Address/', views.address_Update, name='update_Address'),
    path('del_address/', views.delete_ADDress, name='del_address'),
    path('loginsecurity/', TemplateView.as_view(template_name="login_Security.html")),
    path('vendorchangepassword/', views.vendor_changepassword),
    path('vendorupdatepassword/', views.vendor_updatepassword),
    path('vendorchangemobilenumber/', views.vendorchange_mobilenumber),
    path('vendorupdatemobileno/', views.vendorupdate_mobileno),
    path('add_cart/', views.add_to_cart, name='add_cart'),
    path('single/', views.single, name='single'),
    # path('checkout/', TemplateView.as_view(template_name="checkout.html"),name='checkout'),
    path('del_product/', views.delete_product, name='delete_product'),

    path('paymentoptions/', TemplateView.as_view(template_name="paymentoptions.html")),

    path('clogout/', views.clogout),
    path('vlogout/', views.vlogout),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)