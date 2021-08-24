from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)  # 문자 필드 - max_len은 필수 인수
    pub_date = models.DateTimeField("date published") # 날짜 필드 - 각 필드의 자료형을 지정할 수 있다.


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    # SQL에서 많이 보던건데...
                                                                        # Foreign key 부모 테이블과 연동하는 외래 키
                                                                        # on_delete_cascade: 부모 데이터 삭제시 삭제
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

