from django.db import models

from django_ckeditor_5.fields import CKEditor5Field
from cloudinary.models import CloudinaryField


class Testimonial(models.Model):
    text = models.TextField(help_text="The testimonial text.", blank=True, null=True)
    author = models.CharField(
        max_length=255, help_text="The name of the testimonial author."
    )

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return f"{self.author} - {self.text[:50]}..."


class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField()
    profile_picture = CloudinaryField("volunteers", blank=True, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        ("upcoming", "Upcoming"),
        ("past", "Past"),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    event_type = models.CharField(max_length=10, choices=EVENT_TYPE_CHOICES)
    location = models.CharField(max_length=255, null=True, blank=True)
    image = CloudinaryField("events", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-date"]  # Order events by date (newest first)


class PartnershipSubmission(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    organisation = models.CharField(max_length=100, blank=True)
    date_submitted = models.DateTimeField(auto_now_add=True)
    message = models.TextField(null=True, blank=True)

    partnership_category = models.CharField(
        max_length=50,
        choices=[
            ("Corporate Partnerships", "Corporate Partnerships"),
            ("NGO Collaborations", "NGO Collaborations"),
            (
                "Individual Donors and Philanthropists",
                "Individual Donors and Philanthropists",
            ),
            ("Community Engagement", "Community Engagement"),
        ],
    )
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.partnership_category}"


class Video(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=500)

    def __str__(self):
        return self.title


class Publication(models.Model):
    title = models.CharField(max_length=200)
    cover_image = CloudinaryField("publications/covers")
    file = models.FileField(upload_to="publications/files")
    date = models.DateField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"


class News(models.Model):
    title = models.CharField(max_length=200)
    image = CloudinaryField("news_images")
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def short_content(self):
        """Returns a short snippet of the content for display."""
        return self.content[:100] + "..." if len(self.content) > 100 else self.content

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return self.title


class Trustee(models.Model):
    # Name of the trustee
    name = models.CharField(max_length=255)

    # Avatar/profile picture
    picture = CloudinaryField("trustee_avatars", blank=True, null=True)

    # Position or role of the trustee
    position = models.CharField(max_length=255, blank=True, null=True)

    bio = CKEditor5Field("Bio", config_name="default", blank=True, null=True)

    class Meta:
        verbose_name = "Trustee"
        verbose_name_plural = "Board of Trustee"

    def __str__(self):
        return self.name


class Team(models.Model):
    # Name of the team member
    name = models.CharField(max_length=255)

    # Role of the team member
    role = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

    def __str__(self):
        return self.name


class Donation(models.Model):
    # Options for the Partnership Category dropdown
    PARTNERSHIP_CATEGORIES = [
        ("Corporate Partnerships", "Corporate Partnerships"),
        ("NGO Collaborations", "NGO Collaborations"),
        (
            "Individual Donors and Philanthropists",
            "Individual Donors and Philanthropists",
        ),
        ("Community Engagement", "Community Engagement"),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    organization = models.CharField(max_length=200, blank=True, null=True)
    partnership_category = models.CharField(
        max_length=50, choices=PARTNERSHIP_CATEGORIES
    )
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
