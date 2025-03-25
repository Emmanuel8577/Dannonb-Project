from django.contrib import admin

from website.models import (
    Event,
    News,
    Publication,
    Team,
    Testimonial,
    Trustee,
    Donation,
    Contact,
    Video,
    PartnershipSubmission,
    Volunteer,
)

admin.site.register(Volunteer)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("author", "text")
    search_fields = ("author", "text")


class VolunteerAdmin(admin.ModelAdmin):
    list_display = ("name", "info")
    search_fields = ("name", "info")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "date", "event_type", "location")
    list_filter = ("event_type", "date")
    search_fields = ("name", "description", "location")


@admin.register(PartnershipSubmission)
class PartnershipRequestAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "partnership_category",
    )
    list_filter = ("partnership_category",)
    search_fields = ("first_name", "last_name", "email", "organization")


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "url")
    search_fields = ("title",)


class PublicationAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "cover_image", "file")
    search_fields = ("title", "date")
    list_filter = ("date",)


admin.site.register(Publication, PublicationAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "date_submitted",
    )
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("date_submitted",)


admin.site.register(Contact, ContactAdmin)


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "partnership_category",
        "submitted_at",
    )
    list_filter = ("partnership_category", "submitted_at")
    search_fields = ("first_name", "last_name", "email", "organization")


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "published_date")
    search_fields = ("title", "content")
    ordering = ("-published_date",)


class TrusteeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "position",
    )  # Display name, avatar, and position in the admin list view
    search_fields = ("name", "position")  # Allows search by trustee name or position


admin.site.register(Trustee, TrusteeAdmin)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "role")
    search_fields = ("name", "role")
