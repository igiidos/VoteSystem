from django.conf import settings
from django.db import models


# Create your models here.


class VoteSubject(models.Model):
	whose = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subject')
	image = models.ImageField(upload_to='gong_go/image', blank=True)
	stater = models.CharField(max_length=100, blank=True)
	subject = models.CharField(max_length=255)
	text = models.TextField(blank=True)
	status = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.subject


DONG = (
	('100', '동선택'),
	('101', '101'),
	('102', '102'),
	('103', '103'),
	('104', '104'),
	('105', '105'),
	('106', '106'),
	('107', '107'),
	('108', '108'),
	('109', '109'),
	('110', '110'),
	('111', '111'),
	('112', '112'),
	('113', '113'),
	('114', '114'),
	('115', '115'),
	('116', '116'),
	('117', '117'),
	('118', '118'),
	('119', '119'),
)


class Vote(models.Model):
	which = models.ForeignKey(VoteSubject, on_delete=models.CASCADE, related_name='vote')
	dong = models.CharField(choices=DONG, max_length=3, default='100')
	ho = models.PositiveIntegerField()
	name = models.CharField(max_length=15)
	tel1 = models.PositiveSmallIntegerField()
	voting = models.BooleanField(blank=True)
	signature = models.CharField(max_length=255)

	def __str__(self):
		return self.which.subject

