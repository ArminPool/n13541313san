from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.db.models import CharField, DateField, TimeField
from django import forms
from django.core.urlresolvers import reverse
from django_mysql.models import ListTextField
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.
from users.models import Author


class Post(models.Model):
    header = models.CharField(max_length=500)

    img = ProcessedImageField(upload_to='uploaded/posts/img',
                              processors=[ResizeToFill(700, 450)],

                              format='JPEG',
                              options={'quality': 60}, null=True, blank=False)

    description = RichTextField(config_name='awesome_ckeditor')

    text = RichTextField(config_name='awesome_ckeditor')

    date_published = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    Main_Tag = models.CharField(max_length=500)

    author = models.ForeignKey(Author, null=False)

    is_article = models.BooleanField(default=False)

    is_vip = models.BooleanField(default=False)

    is_universal_ons = models.BooleanField(default=False)

    is_pairs_of_currencies = models.BooleanField(default=False)

    is_domestic_dollar = models.BooleanField(default=False)

    public = models.BooleanField(default=False)

    Tags = ListTextField(
        base_field=models.CharField(max_length=20),
        size=3,
    )
    seen = models.IntegerField(default=0)

    class Meta:
        ordering = ['-date_published']

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return '/' + str(self.header).replace(' ', '-') + '/'

    def get_Main_Tag(self):
        return str(self.Main_Tag).replace(' ', '-')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')

    user = models.ForeignKey(User, null=True)

    body = models.TextField(max_length=250, null=True)

    created = models.DateTimeField(auto_now_add=True)

    approved = models.BooleanField(default=False)

    parent = models.ForeignKey("self", null=True, blank=True)

    public = models.BooleanField(default=False)

    def approved(self):
        self.approved = True
        self.save()

    def __str__(self):

        return self.user.username

    def is_parent(self):
        if self.parent is not None:
            return False
        return True

    # is_public for moderation
    def is_public(self):

        if self.public:
            return True
        return False

    def children(self):
        return Comment.objects.filter(parent=self)


class Calender(models.Model):
    date = DateField()

    time = TimeField()

    stock = CharField(max_length=60)

    event = CharField(max_length=60)

    importance = CharField(max_length=60)

    actual = CharField(max_length=60)

    predict = CharField(max_length=60)

    previous = CharField(max_length=60)

    def __str__(self):
        return str(self.stock) + ' ' + str(self.date)


class BankOrders(models.Model):
    """
        cooperate = 'co'
    problem_buying = 'pb'
    ask_game = 'ag'
    others = 'o'

    options = (
        (cooperate, 'همکاری'), (problem_buying, 'مشکل در خرید'), (ask_game, 'درخواست بازی'), (others, 'موارد دیگر'))
    issue_options = models.CharField(choices=options, default=cooperate, max_length=2)
    """
    Pair_Options = (('USDJPY', 'USDJPY'), ('EURAUD', 'EURAUD'), ('AUDCHF', 'AUDCHF'), ('CHFJPY', 'CHFJPY')
                    , ('NZDCAD', 'NZDCAD'), ('AUDNZD', 'AUDNZD'), ('USDCAD', 'USDCAD'), ('EURCHF', 'EURCHF')
                    , ('CADCHF', 'CADCHF'), ('CADJPY', 'CADJPY'), ('EURUSD', 'EURUSD'),
                    ('EURGBP', 'EURGBP'), ('AUDCAD', 'AUDCAD'), ('GBPCHF', 'GBPCHF'), ('AUDUSD', 'AUDUSD'),
                    ('GBPAUD', 'GBPAUD'))

    Pair = models.CharField(choices=Pair_Options, default='', max_length=100)
    Bank_Options = (('Goldman Sachs', 'Goldman Sachs'), ('Credit Suisse', 'Credit Suisse'), ('Citi Bank', 'Citi Bank'),
                    ('Nomura Holdings', 'Nomura Holdings'),
                    ('Deutsche Bank', 'Deutsche Bank'), ('TD Bank', 'TD Bank'), ('Morgan Stanley', 'Morgan Stanley'),
                    ('Barclays', 'Barclays'),
                    ('UOB', 'UOB'), ('Bofa Merrill Lynch', 'Bofa Merrill Lynch'),
                    ('Credit Agricole', 'Credit Agricole'),
                    ('Danske', 'Danske'),
                    ('Thomson Reuters IFR', 'Thomson Reuters IFR'),)
    Bank = models.CharField(choices=Bank_Options, default='', max_length=100)
    Date = models.DateField()
    Order_Options = (('Sell', 'Sell'), ('Sell Limit', 'Sell Limit'), ('Sell Stop', 'Sell Stop'), ('Buy', 'Buy'),
                     ('Buy Limit', 'Buy Limit'), ('Buy Stop', 'Buy Stop'),
                     )

    Order = models.CharField(choices=Order_Options, default='', max_length=100)
    Status_Options = (('Active', 'Active'), ('Pending', 'Pending'))

    Status = models.CharField(choices=Status_Options, default='Pending', max_length=100)

    Entry = models.CharField(max_length=50)
    Take_Profit = models.CharField(max_length=50)
    Stop_Loss = models.CharField(max_length=50)

    def __str__(self):
        return self.Bank + ' ' + 'Order: ' + self.Order + ' ' + 'Date: ' + str(
            self.Date) + ' ' + 'Take_Profit: ' + self.Take_Profit
