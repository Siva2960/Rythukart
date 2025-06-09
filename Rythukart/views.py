from django.shortcuts import render
from .models import Product, Register, Cart, CartItem, UserLocation, Order, OrderItem

# Create your views here.
def index(request):
    return render(request,'index.html')

import pymysql
from django.views.decorators.csrf import csrf_exempt

# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
def checkUser(number):
    try:
        con = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            database='RK',
            charset='utf8'
        )
        with con.cursor() as cur:
            cur.execute("SELECT number FROM rythukart_register WHERE number=%s", (number,))
            result = cur.fetchone()
            return result is not None
    except Exception as e:
        print("Check user error:", e)
        return False
    finally:
        con.close()

from django.shortcuts import render
from .models import Register

def Register_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        password = request.POST.get('password')

        # 1. Validate form fields
        if not all([name, number, password]):
            return render(request, 'index.html', {'data': 'All fields are required'})

        # 2. Check if number already exists
        if Register.objects.filter(number=number).exists():
            return render(request, 'index.html', {'data': 'You are already registered!'})

        # 3. Save new user
        try:
            Register.objects.create(name=name, number=number, password=password)
            return render(request, 'R_S.html', {'data': 'Signup successful!'})
        except Exception as e:
            print("Registration error:", e)
            return render(request, 'index.html', {'data': 'Something went wrong. Try again.'})

    # If GET request
    return render(request, 'index.html', {'data': 'Invalid request method'})

from django.shortcuts import render, redirect

from .models import Register

def Login(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        password = request.POST.get('password')

        try:
            user = Register.objects.get(number=number, password=password)
            request.session['number'] = number  # Store user number in session
            return render(request, 'home.html', {
                'name': user.name,
                'data': f"Welcome {user.name}"
            })
        except Register.DoesNotExist:
            return render(request, 'login.html', {'data': 'Invalid login details'})
    return render(request, 'login.html')

def logout_view(request):
    request.session.flush()  # ✅ Clears the session safely
    return redirect('index')

from django.shortcuts import render, redirect
from .models import Register

def home(request):
    number = request.session.get("number")
    name = None
    if number:
        try:
            user = Register.objects.get(number=number)
            name = user.name
        except Register.DoesNotExist:
            pass

    return render(request, 'home.html', {"name": name})

def home1(request):
    return render(request,'home1.html')
def veg(request):
    user_number = request.session.get('number')

    if user_number:
        user = get_object_or_404(Register, number=user_number)
        cart = get_cart_for_user(user)
        cart_items = CartItem.objects.filter(cart=cart).select_related('product')
        cart_map = {item.product.id: item for item in cart_items}
    else:
        cart_items = []
        cart_map = {}

    products = Product.objects.filter(product_type='veg', stock__gt=0)

    context = {
        'products': products,
        'cart_items': cart_items,
        'cart_map': cart_map,
        'user_authenticated': bool(user_number),
    }
    return render(request, 'veg.html', context)



def pappu(request):
    user_number = request.session.get('number')
    if user_number:
        user = get_object_or_404(Register, number=user_number)
        cart = get_cart_for_user(user)
        cart_items = CartItem.objects.filter(cart=cart).select_related('product')
        cart_map = {item.product.id: item for item in cart_items}
    else:
        cart_items = []
        cart_map = {}

    products = Product.objects.filter(product_type='pappu', stock__gt=0)

    context = {
        'products': products,
        'cart_items': cart_items,
        'cart_map': cart_map,
        'user_authenticated': bool(user_number),
    }
    return render(request, 'pappu.html', context)


def rice(request):
    user_number = request.session.get('number')
    if user_number:
        user = get_object_or_404(Register, number=user_number)
        cart = get_cart_for_user(user)
        cart_items = CartItem.objects.filter(cart=cart).select_related('product')
        cart_map = {item.product.id: item for item in cart_items}
    else:
        cart_items = []
        cart_map = {}

    products = Product.objects.filter(product_type='rice', stock__gt=0)

    context = {
        'products': products,
        'cart_items': cart_items,
        'cart_map': cart_map,
        'user_authenticated': bool(user_number),
    }
    return render(request, 'rice.html', context)


from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

def admin_upload(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_upload')
    else:
        form = ProductForm()
    return render(request, 'admin_upload.html', {'form': form})


def checkout(request):
    cart = request.session.get('cart', {})  # Example: { 'product_id': quantity }

    for product_id, qty in cart.items():
        product = Product.objects.get(id=product_id)
        if product.stock >= qty:
            product.stock -= qty
            product.save()
        else:
            return HttpResponse("Not enough stock for " + product.name)

    request.session['cart'] = {}  # clear cart
    return HttpResponse("Purchase successful!")

from .models import UserLocation  # import your model


def add_address(request):
    return render(request, 'add_address.html')

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import UserLocation

def location_page(request):
    return render(request, 'location_page.html')  # Template you'll create next

from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from .models import UserLocation
from django.shortcuts import redirect

@csrf_protect
def save_location(request):
    if request.method == 'POST':
        data = request.POST
        UserLocation.objects.create(
            name=data.get('name'),
            number=data.get('number'),
            address_line=data.get('address_line'),
            near_by=data.get('near_by'),
            area=data.get('area'),
            district=data.get('district', ''),
            pincode=data.get('pincode', ''),
            latitude=data.get('latitude') or 0,
            longitude=data.get('longitude') or 0
        )
        return JsonResponse({'message': 'Saved successfully'})
    return JsonResponse({'error': 'Invalid request'}, status=400)



def select_address(request, address_id):
    try:
        address = UserLocation.objects.get(id=address_id)
        # Save selected address in session
        request.session['user_address'] = {
            'name': address.name,
            'number': address.number,
            'address_line': address.address_line,
            'area': address.area,
            'near_by': address.near_by,
            'pincode': address.pincode,
        }
        return redirect('cart')  # Redirect back to cart page after selection
    except UserLocation.DoesNotExist:
        return redirect('cart')  # If address doesn't exist, redirect to cart page


from django.shortcuts import redirect, render, get_object_or_404
from .models import Register, Cart, CartItem, Order, OrderItem, Product


def payment(request):
    user_number = request.session.get('number')
    if not user_number:
        return redirect('Login')

    user = get_object_or_404(Register, number=user_number)
    cart = get_cart_for_user(user)
    cart_items = CartItem.objects.filter(cart=cart).select_related('product')

    if not cart_items.exists():
        return redirect('view_cart')

    address = request.session.get('user_address', {})  # previously selected
    address_str = f"{address.get('address_line', '')}, {address.get('area', '')}, {address.get('pincode', '')}"

    total = sum(item.subtotal() for item in cart_items)

    # ✅ Save order
    order = Order.objects.create(user=user, total=total, address=address_str)

    for item in cart_items:
        # ✅ Reduce product stock
        product = item.product
        if product.stock >= item.quantity:
            product.stock -= item.quantity
            product.save()
        else:
            # Optional: handle insufficient stock (currently assumes always enough)
            pass

        # ✅ Save order item
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=item.quantity,
            price=product.price
        )

    cart_items.delete()  # ✅ clear cart after ordering

    return render(request, 'payment.html', {'message': 'Payment successful!'})

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Product, Register, Cart, CartItem, UserLocation
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

def get_cart_for_user(user):
    cart, _ = Cart.objects.get_or_create(user=user)
    return cart
def cart_view(request):
    print("🛒 cart_view triggered")  # Confirm view is being used
    user_number = request.session.get('number')
    print("📱 Logged in as:", user_number)

    if not user_number:
        return redirect('Login')

    try:
        user = Register.objects.get(number=user_number)
    except Register.DoesNotExist:
        return redirect('Login')

    cart = get_cart_for_user(user)
    cart_items = CartItem.objects.filter(cart=cart).select_related('product')
    total = sum(item.subtotal() for item in cart_items)
    user_addresses = UserLocation.objects.filter(number=user_number)

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'cart_total': total,
        'user_addresses': user_addresses,
    })


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.db.models import Sum

@csrf_exempt
def add_to_cart_ajax(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            product_id = data.get("product_id")

            user_number = request.session.get("number")
            if not user_number:
                return JsonResponse({"error": "Not logged in"}, status=401)

            user = get_object_or_404(Register, number=user_number)
            cart = get_cart_for_user(user)
            product = get_object_or_404(Product, id=product_id)

            item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            item.quantity += 1 if not created else 0
            item.save()

            cart_count = cart.items.aggregate(total=Sum("quantity"))["total"] or 0

            return JsonResponse({
                "success": True,
                "cart_count": cart_count,
                "item_id": item.id,
                "quantity": item.quantity,
                "product_id": product.id
            })
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request"}, status=400)

@require_POST
def increase_cart_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.quantity += 1
    item.save()
    return redirect('view_cart')

@require_POST
def decrease_cart_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect('view_cart')

@csrf_exempt
def change_cart_quantity_ajax(request):
    if request.method == "POST":
        data = json.loads(request.body)
        item_id = data.get("item_id")
        action = data.get("action")  # 'increase' or 'decrease'

        try:
            item = CartItem.objects.get(id=item_id)
            if action == "increase":
                item.quantity += 1
                item.save()
            elif action == "decrease":
                if item.quantity > 1:
                    item.quantity -= 1
                    item.save()
                else:
                    item.delete()

            cart = item.cart
            cart_count = cart.items.aggregate(total=Sum("quantity"))["total"] or 0

            return JsonResponse({
                "success": True,
                "item_id": item.id,
                "quantity": item.quantity if item.id else 0,
                "cart_count": cart_count
            })
        except CartItem.DoesNotExist:
            return JsonResponse({"success": False, "deleted": True})
    return JsonResponse({"error": "Invalid request"}, status=400)

from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect
from .models import CartItem

@require_POST
def remove_cart_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('view_cart')

# views.py

def order_history(request):
    user_number = request.session.get('number')
    if not user_number:
        return redirect('Login')

    user = get_object_or_404(Register, number=user_number)
    orders = Order.objects.filter(user=user).order_by('-created_at')
    return render(request, 'orders.html', {'orders': orders})
import tempfile
import os
from django.template.loader import get_template
from weasyprint import HTML
from django.http import HttpResponse
from .models import Order
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
from io import BytesIO
from .models import Order
from django.shortcuts import get_object_or_404

def generate_invoice(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    template = get_template("invoice.html")
    html_content = template.render({"order": order})

    # 🧠 Create PDF in memory (no file writing!)
    pdf_file = BytesIO()
    HTML(string=html_content).write_pdf(pdf_file)
    pdf_file.seek(0)

    # 📄 Return as downloadable PDF response
    response = HttpResponse(pdf_file, content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="invoice_{order_id}.pdf"'
    return response

from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import Product, Register, Cart, CartItem

@require_POST
@csrf_protect
def voice_add_to_cart(request):
    if request.method == "POST":
        product_name = request.POST.get("product_name", "").strip().lower()
        quantity = int(request.POST.get("quantity", 1))
        user_number = request.session.get("number")

        if not user_number:
            return JsonResponse({"success": False, "error": "Login required."})

        try:
            user = Register.objects.get(number=user_number)
            cart = get_cart_for_user(user)
            product = Product.objects.filter(name__icontains=product_name, stock__gte=1).first()

            if not product:
                return JsonResponse({"success": False, "error": "Product not found."})

            item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            item.quantity += quantity
            item.save()

            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})
    return JsonResponse({"success": False, "error": "Invalid request"})
