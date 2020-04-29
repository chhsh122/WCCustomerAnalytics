from django.db import models

# Create your models here.
from django.urls import reverse


class Department(models.Model):
    name = models.CharField(max_length=128, verbose_name='评论分类', help_text='一个评论分类的名字应该唯一', unique=True, db_index=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = "评论分类"

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=128, verbose_name='描述', null=True, blank=True)

    class Meta:
        verbose_name = '描述'
        verbose_name_plural = '客户描述'

    def get_absolute_url(self):
        return reverse('title-detail-view', args=(self.name,))

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(verbose_name='图片')
    title = models.ForeignKey(Title, on_delete=models.SET_NULL, blank=False, null=True, )

    class Meta:
        verbose_name = '图片'
        verbose_name_plural = '客户资料'

    def __str__(self):
        return self.image.path


class Employe(models.Model):
    name = models.CharField(max_length=128, verbose_name='客户名字', help_text='名字', null=False, blank=False,
                            db_index=True)

    gender_choices = (
        (0, '男'),
        (1, '女'),
        # (2, '中评'),
    )

    gender = models.IntegerField(choices=gender_choices, verbose_name='性别', default=0)

    idCard = models.CharField(max_length=18, verbose_name='SEO描述', help_text='SEO描述', blank=True, null=True)
    phone = models.CharField(max_length=11, verbose_name='客户地址')

    birthday = models.CharField(max_length=18,verbose_name='评论')
    time = models.TimeField(verbose_name='时间', auto_now=True)

    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='顺序',
                                   db_index=True)

    title = models.ForeignKey(Title, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='业务模式',
                              db_index=True)

    enable = models.BooleanField(verbose_name='是否是VIP', default=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)

    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        verbose_name = "客户分析"
        verbose_name_plural = "客户分析"

    def __str__(self):
        return self.name
