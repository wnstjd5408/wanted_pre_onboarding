from django.db import models


# Create your models here.
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    cp_name = models.CharField(max_length=100)
    cp_country = models.CharField(max_length=50)
    cp_area = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.cp_name

    class Meta:
        verbose_name = "회사"
        verbose_name_plural = f"{verbose_name} 목록"
        ordering = ["-id"]


class Job_Posting(models.Model):
    id = models.AutoField(primary_key=True)
    jp_position = models.CharField(max_length=200)
    jp_content = models.TextField()
    jp_compensation = models.PositiveIntegerField(default=0)
    jp_technology = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, related_name="companys", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "{}번".format(str(self.id))

    class Meta:
        verbose_name = "채용공고"
        verbose_name_plural = f"{verbose_name} 목록"
        ordering = ["-id"]
