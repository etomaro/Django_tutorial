import datetime

from django.test import TestCase
from django.utils import timezone
from django.utils import reverse
from .models import Question


"""
Modelのテスト
"""
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        pub_dateが未来の日付になってないか
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
    
    def test_was_published_recently_with_old_question(self):
        """
        pub_dateが現在時刻より1日前の場合
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recently_question(self):
        """
        pub_dateが現在時刻より1日以内の場合
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recently_question = Question(pub_date=time)
        self.assertIs(recently_question.was_published_recently(), True)

"""
Viewのテスト
"""
def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)



