from django.db import models
import uuid

# Create your models here.


class CourseCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    cover_image_url = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(null=True, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Course Categories"
        db_table = "course_categories"

    def __str__(self):
        return self.name


class GradeCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(null=True, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "grade_categories"

    def __str__(self):
        return self.name


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_id = models.PositiveIntegerField(unique=True, default=-1)
    title = models.CharField(max_length=255)
    description = models.TextField()
    course_category = models.ForeignKey(
        CourseCategory, null=True, blank=True, on_delete=models.SET_NULL
    )
    grade_category = models.ForeignKey(
        GradeCategory, null=True, blank=True, on_delete=models.SET_NULL
    )
    course_image_url = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField(null=True, blank=True)
    teacher_id = models.UUIDField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_purchasable = models.BooleanField(null=True, default=True)
    is_active = models.BooleanField(null=True, default=True)

    class Meta:
        db_table = "courses"

    def save(self, *args, **kwargs):
        if not self.course_id:
            max_id = Course.objects.aggregate(max_id=models.Max("course_id"))["max_id"]
            self.course_id = (max_id or 0) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lesson_id = models.PositiveIntegerField(unique=True, default=-1)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    is_locked = models.BooleanField(null=True, default=False)
    status = models.IntegerField(null=True, blank=True)
    video_url = models.TextField(null=True, blank=True)
    schedule_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "lessons"

    def save(self, *args, **kwargs):
        if not self.lesson_id:
            max_id = Lesson.objects.aggregate(max_id=models.Max("lesson_id"))["max_id"]
            self.lesson_id = (max_id or 0) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "teachers"

    def __str__(self):
        return self.name
