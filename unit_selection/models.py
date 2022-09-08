from django.db import models


class Departemant(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Instructor(models.Model):
    name = models.CharField(max_length=255)
    dept_name = models.ForeignKey(
        Departemant, on_delete=models.CASCADE, related_name="instructors")

    def __str__(self) -> str:
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255)
    credits = models.PositiveIntegerField(default=1)
    status = models.BooleanField(default=False)
    dept_name = models.ForeignKey(Departemant, on_delete=models.CASCADE, null=True, related_name="courses")
    exam_date = models.CharField(max_length=10, default="0")
    exam_time = models.CharField(max_length=10, default="0")

    def __str__(self) -> str:
        return self.name


class Section(models.Model):
    GENDER_CHOICES = (
        ("مختلط", "مختلط"),
        ("مرد", "مرد"),
        ("زن", "زن"),
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="sections")
    instructor = models.ForeignKey(
        Instructor, on_delete=models.CASCADE, related_name="sections")
    code = models.CharField(max_length=255, default="0")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="مختلط")

    def __str__(self) -> str:
        return f"{self.course} {self.code[-2:]}"

    def group(self):
        return self.code[-2:]


class Time_Slot(models.Model):

    DAY_CHOICES = (
        ("شنبه", "شنبه"),
        ("یکشنبه", "یکشنبه"),
        ("دوشنبه", "دوشنبه"),
        ("سشنبه", "سشنبه"),
        ("چهارشنبه", "چهارشنبه"),
    )

    START_CHOICES = (
        ("8", "8"),
        ("10", "10"),
        ("13.5", "13.5"),
        ("15.5", "15.5"),
        ("17.5", "17.5"),

    )
    END_CHOICES = (
        ("9.5", "9.5"),
        ("11.5", "11.5"),
        ("15", "15"),
        ("17", "17"),
        ("19", "19"),

    )
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name="times")
    day = models.CharField(max_length=10, choices=DAY_CHOICES,
                           default="شنبه")
    start = models.CharField(max_length=10, choices=START_CHOICES,
                             default="8")
    end = models.CharField(max_length=10, choices=END_CHOICES,
                           default="9.5")

    def __str__(self) -> str:
        return f"{self.section} {self.day} {self.start}-{self.end}"
