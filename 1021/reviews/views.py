from django.shortcuts import render, redirect
from .forms import ReviewForm, CommentForm, ReCommentForm
from .models import Review, Comment

def index(request):
    reviews = Review.objects.all()
    img_list = [
        {'num':1, 'img': 'https://an2-img.amz.wtchn.net/image/v2/KDbyppee1jp4Q0bwpzDclQ.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5Ea3dlRGN3TUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qUTFNVGs0TkRJMk5qRTVPRGMwTkRBaWZRLkNTdzJWU1lFUzFhaHBUUjRtb1YyWV9EWjJMcnlTczVWVmFjWmJ5S005YnM'},
        {'num':2, 'img': 'https://an2-img.amz.wtchn.net/image/v2/bwjtBMkCbVqCrDFC9XU9kg.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5Ea3dlRGN3TUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qUXlOREE0T0RNek56QTRPVEF5T1RNaWZRLldEd1hEN1FjTHpZb0tYbWVocTF1NmJuSEdEZTUwRHRGWUdwOUg4VE9QZGs'},
        {'num':3, 'img': 'https://an2-img.amz.wtchn.net/image/v2/bTp2M5Jfv1hWdv4QX1pcVQ.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5Ea3dlRGN3TUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qUTFNVGcxTURRMk16YzVORFk1TVRjaWZRLmNHSDRwX1htaDVYNjhPRWhURVQwTC1pRUpheTVRemIyaHMzcEFuN29SVlE'},
        {'num':4, 'img': 'https://an2-img.amz.wtchn.net/image/v2/chphdsVeY3rZbgV09N1kSw.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5Ea3dlRGN3TUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qSTFNekUyT0RBM016azRPVE00TlRRaWZRLjE0aGxoN2lkS3dZX1ZqVWd2MHlJeEpULXV3WlZRcjU1dllMNnVVaEVCc0U'},
        {'num':5, 'img': 'https://an2-img.amz.wtchn.net/image/v2/rPNP8grsFUglDPMS402V2g.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5Ea3dlRGN3TUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qTXpNVFl4TlRjME5EQXhPREF6T0RZaWZRLnd6RVZoaERDb1ZaOWt4SjJFUGg5c3QxQzM3emxlWHNXYnlwRDNRZzc4Ykk'},
        {'num':6, 'img': 'https://an2-img.amz.wtchn.net/image/v2/A3w93ZJKG1mmpfhnT4fviA.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5Ea3dlRGN3TUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qRTJPVFF4TWprMU1EVTROakkwTVRjaWZRLjhlVmVkcUhkQzVSa1E3R1VCc1lKSG92aW9KdlZRSDljTk00UmVyYk1ibnM'},
        {'num':7, 'img': 'https://an2-img.amz.wtchn.net/image/v2/4haai9-NA6ifdoWYapd1IA.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5Ea3dlRGN3TUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qUTFNak0wT1RjNE9EWTJOVFV4TVRJaWZRLnhOcmIxMVBVRm1CbEVya05ZLXNJXzVCeFdETzJjeU1QWERGeDNra2x3SDg'},
        {'num':8, 'img': 'https://an2-img.amz.wtchn.net/image/v2/b-HjLSBuEhkWB1VylnIeyA.jpg?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1SZk5Ea3dlRGN3TUhFNE1DSmRMQ0p3SWpvaUwzWXlMM04wYjNKbEwybHRZV2RsTHpFMk5qTXpNVE15TkRnME5UWTRNakEwT0RJaWZRLmp4Qk9lS3MtdnVrU093V1k0NFpfVjBoWUlUUE9WT3JiOFhKclM0UTJuVWc'},
    ]

    context = {
        'reviews': reviews,
        'img_list': img_list,
    }
    return render(request, 'reviews/index.html', context)
    
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews:index')
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'reviews/forms.html', context)

def detail(request, pk):
    comment_form = CommentForm()
    recomment_form = ReCommentForm()
    review = Review.objects.get(pk=pk)
    context = {
        'review': review,
        'comment_form': comment_form,
        'recomment_form': recomment_form,
    }
    return render(request, 'reviews/detail.html', context)

def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('reviews:detail', review.pk)
    else:
        form = ReviewForm(instance=review)
    context = {
        'form': form,
    }
    return render(request, 'reviews/forms.html', context)

def delete(request, pk):
    review = Review.objects.get(pk=pk)
    review.delete()
    return redirect('reviews:index')

def posts(request, pk):
    movies = [
        {'num': 1, 'title': "블랙 아담"},
        {'num': 2, 'title': "리멤버"},
        {'num': 3, 'title': "자백"},
        {'num': 4, 'title': "인생은 아름다워"},
        {'num': 5, 'title': "에브리씽 에브리웨어 올 앳 원스"},
        {'num': 6, 'title': "공조2: 인터내셔날"},
        {'num': 7, 'title': "귀못"},
        {'num': 8, 'title': "극장판 짱구는 못말려: 수수께끼! 꽃피는 천하떡잎학교"},
    ]
    reviews = Review.objects.filter(movie_title=pk)
    context = {
        'reviews': reviews,
        'movies': movies,
        'pk': pk,
    }
    return render(request, 'reviews/posts.html', context)

def comments(request, pk):
    review = Review.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.review = review
        comment.save()
    return redirect('reviews:detail', review.pk)

def comments_delete(request, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('reviews:detail', review_pk)

def recomments(request, pk):
    comment = request.POST.get('comment')
    comment_pk = Comment.objects.get(pk=comment)
    recomment_form = ReCommentForm(request.POST)
    if recomment_form.is_valid():
        recomment = recomment_form.save(commit=False)
        recomment.comment = comment_pk
        recomment.user = request.user
        recomment.save()
    return redirect('reviews:detail', pk)