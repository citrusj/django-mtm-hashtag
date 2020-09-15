# Django Hashtag
##### 서강 멋쟁이사자처럼 Many-to-Many Model, Hashtag 강의자료

* 게시물 Create, Update, Read, Delete
* 게시물에 댓글 달기/삭제
* 게시물에 해시태그 추가, 삭제
* 해시태그별로 딸린 게시물 모아보기, 게시물 개수 보여주기

### Related Code
* Django model ManyToManyField 활용
```
class Content(models.Model):
  title=models.CharField(max_length=200)
  pub_date = models.DateTimeField(default=timezone.now)
  body = models.TextField(default='')
  tags = models.ManyToManyField('Tag', blank=True)
  def __str__(self):
    return self.title

class Comment(models.Model):
  post = models.ForeignKey('Content', on_delete=models.CASCADE)
  text = models.TextField(default='')
  created_date = models.DateTimeField(default=timezone.now)

class Tag(models.Model):
  name = models.CharField(max_length=10)
  def __str__(self):
    return self.name
```

* Django query set : 데이터베이스에서 가져온 data객체 목록
```
content = Cotent.objects.get(pk=3)
content.tags.all()
content.tags.add(tag) -> 게시물에 tag 추가
content.tags.remove(tag) -> 게시물에서 tag 삭제

tag = Tag.objects.get(pk=7)
tag.cotent_set.all()-> 하나의 tag에 연결된 모든 게시물 목록
tag.delete() -> tag 객체 삭제

Tag.objects.order_by('name') -> name 필드 기준으로 정렬
Tag.objects.filter(name__contains="번째") -> 특정값을 포함하는 query set 가져오기
```
