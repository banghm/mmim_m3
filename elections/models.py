from django.db import models

# Create your models here.
# 이름, 아이디, 비밀번호, 주소, 전화번호, 주민번호
class MMIM(models.Model):
    name = models.CharField(max_length=10, verbose_name='이름')
    user_id = models.CharField(max_length=10)
    user_pw = models.CharField(max_length=10)
    adr1 = models.CharField(max_length=30)
    pn = models.CharField(max_length=20)
    jm = models.CharField(max_length=20) # 주민번호
    choice = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class contract(models.Model):
    #employer = models.CharField(max_length=10, verbose_name='고용주')
    #employee = models.CharField(max_length=10, verbose_name='근로자')
    employer = models.ForeignKey('elections.MMIM', on_delete=models.CASCADE, related_name='employer', verbose_name="고용주")
    employee = models.ForeignKey('elections.MMIM', on_delete=models.CASCADE, related_name='employee', verbose_name="근로자")
    start_date = models.DateField(verbose_name="근로 시작 기간")
    end_date = models.DateField(verbose_name="근로 종료 기간")
    start_time = models.TimeField(null=True, verbose_name="근로 시작 시간")
    end_time = models.TimeField(null=True, verbose_name="근로 마감 시간")
    workday = models.CharField(max_length=6, verbose_name="근무일")
    holiday = models.CharField(max_length=6, verbose_name="휴일")
    work_place = models.CharField(max_length=30, verbose_name='근무 장소')
    work_content = models.CharField(max_length=50, verbose_name='업무내용')
    salary = models.IntegerField(default=0, verbose_name="월급")
    year_holiday = models.IntegerField(default=0, verbose_name="연차 유급 휴가")




