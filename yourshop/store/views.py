from django.shortcuts import render
from django.views.generic import View
from .models import Banners, Products, ProductImage, Sizes, Comments
from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from django.db.models import Prefetch, OuterRef, Subquery


class HomePageView(View):
    template_name = 'shop/home.html'

    def get(self, request, *args, **kwargs):
        banners = Banners.objects.filter(active=True)  # Получаем активные баннеры

        # Получаем URL первого изображения для каждого продукта
        product_images = ProductImage.objects.filter(main_image=True)
        context = {
            'banners': banners,
            'product_images': product_images,
        }

        return render(request, self.template_name, context)

class SingleProductView(DetailView):
    model = Products
    template_name = 'shop/03-Single_product_v3.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        sizes = product.sizes.all()
        comments = Comments.objects.filter(product=product)
        comment_form = CommentForm()
        comment_count = comments.count()
        comment_rate = comments.aggregate(Avg('rate'))['rate__avg']
        images = ProductImage.objects.filter(product=product)

        context['sizes'] = sizes
        context['comment_form'] = comment_form
        context['comments'] = comments
        context['comment_count'] = comment_count
        context['comment_rate'] = comment_rate
        context['images'] = images
        return context

    def post(self, request, *args, **kwargs):
        product = self.get_object()
        form = CommentForm(request.POST, product=product)  # передаем продукт в форму
        if form.is_valid():
            form.save()
            return redirect('store:product', pk=product.pk)
        else:
            # Если форма недействительна, возвращаем контекст с формой и другими данными
            context = self.get_context_data(**kwargs)
            context['comment_form'] = form
            return self.render_to_response(context)
