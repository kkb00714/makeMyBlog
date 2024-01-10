from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# 게시글 - 제목, 내용, 작성자, 작성일, 수정일, 이미지, 조회수, 카테고리 기능
class Post(models.Model):
    # 추가해야 할 것 : 카테고리 기능
    title = models.CharField(verbose_name='제목', null=False, max_length=60)
    content = models.TextField(verbose_name='내용', null=False, max_length=1000)
    writer = models.ForeignKey(verbose_name='작성자', to=User, on_delete=models.CASCADE, null=True, blank=True)
    # 작성자가 삭제되면 게시글도 삭제됨
    # 24/01/06 지금은 user 기능이 없어서 null, blank True로 해놓음
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True, null=False)
    modified_at = models.DateTimeField(verbose_name='마지막 수정일', auto_now=True, null=False)
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)
    view_count = models.PositiveIntegerField(verbose_name='조회수', default=0)

# 댓글 - 내용, 생성일
class Comment(models.Model):
    content = models.TextField(verbose_name='댓글 내용', max_length=500)
    created_at = models.DateTimeField(verbose_name='댓글 작성일', auto_now_add=True, null=False)
    post = models.ForeignKey(to='Post', on_delete=models.CASCADE)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    # 게시글 및 작성자가 삭제되면 댓글도 함께 삭제됨
    # 24/01/06 지금은 user 기능이 없어서 null, blank True로 해놓음
    


