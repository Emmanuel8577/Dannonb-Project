from django.core.paginator import Paginator
from .models import (
    Contact,
    News,
    Publication,
    Team,
    Testimonial,
    Trustee,
    Video,
    Event,
    Volunteer,
)


from django.shortcuts import get_object_or_404, render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm, DonationForm, PartnershipForm


def index(request):
    news_list = News.objects.all().order_by("-published_date")  # Get latest news
    paginator = Paginator(news_list, 6)  # Show 6 news items per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "website/index.html", {"page_obj": page_obj})


def about(request):
    return render(request, "website/about.html")


def news_list(request):
    news_items = News.objects.all().order_by(
        "-published_date"
    )  # Adjust 'date' field as per your model
    paginator = Paginator(news_items, 20)  # 20 items per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "website/news_list.html", {"page_obj": page_obj})


def news_detail(request, pk):
    news = News.objects.get(pk=pk)
    return render(request, "website/news_detail.html", {"news": news})


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            phone_number = form.cleaned_data["phone_number"]
            message = form.cleaned_data["message"]

            contact = Contact(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                message=message,
            )
            contact.save()

            # Send an email to the admin
            send_mail(
                f"Contact Us Message from {first_name} {last_name}",
                message,
                email,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            return redirect(
                "contact_success"
            )  # Redirect to a success page or the same contact page
    else:
        form = ContactForm()

    return render(request, "website/contact.html", {"form": form})


def programmes(request):
    return render(request, "website/programmes.html")


def health_programme(request):
    return render(request, "website/health_programme.html")


def emergency_relief(request):
    return render(request, "website/emergency_relief.html")


def education_programme(request):
    return render(request, "website/education.html")


def projects_supported(request):
    return render(request, "website/projects_supported.html")


def skills_development(request):
    return render(request, "website/skills_development.html")


def advocacy_awareness(request):
    return render(request, "website/advocacy_awareness.html")


def board_of_trustees(request):
    trustees = Trustee.objects.all()
    return render(request, "website/board_of_trustees.html", {"trustees": trustees})


def trustee_detail(request, pk):
    trustee = get_object_or_404(Trustee, pk=pk)
    return render(request, "website/trustee_detail.html", {"trustee": trustee})


def team(request):
    team_members = Team.objects.all()
    return render(request, "website/team.html", {"team_members": team_members})


def donation_view(request):
    if request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save()

            # Send email
            subject = "New Donation Submission"
            message = (
                f"New Donation Submission:\n\n"
                f"Name: {donation.first_name} {donation.last_name}\n"
                f"Email: {donation.email}\n"
                f"Phone Number: {donation.phone_number}\n"
                f"Organization: {donation.organization}\n"
                f"Partnership Category: {donation.partnership_category}\n\n"
                f"Message:\n{donation.message}"
            )
            send_mail(
                subject,
                message,
                donation.email,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            return redirect("donation_success")  # Redirect to a success page

    else:
        form = DonationForm()

    return render(request, "website/donation.html", {"form": form})


def donation_success(request):
    return render(request, "website/success.html")


def contact_success(request):
    return render(request, "website/contact_success.html")


def publication_list(request):
    publication_list = Publication.objects.all().order_by(
        "-date"
    )  # Order by date, most recent first
    paginator = Paginator(publication_list, 20)  # Show 20 publications per page
    page_number = request.GET.get("page")  # Get the current page number
    page_obj = paginator.get_page(page_number)  # Get the page object for pagination

    return render(request, "website/publication_list.html", {"page_obj": page_obj})


def video_list(request):
    video_list = Video.objects.all()
    paginator = Paginator(video_list, 20)  # Show 20 videos per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "website/video_list.html", {"page_obj": page_obj})


def scholarship(request):
    return render(request, "website/scholarship.html")


def annual_grant(request):
    return render(request, "website/annual_grant.html")


def discretionary_grant(request):
    testimonials = Testimonial.objects.all()
    return render(
        request, "website/discretionary_grant.html", {"testimonials": testimonials}
    )


def partnership_collaboration(request):
    if request.method == "POST":
        form = PartnershipForm(request.POST)
        if form.is_valid():
            # Save form data to the database
            submission = form.save()

            # Send an email notification
            send_mail(
                subject="New Partnership Submission",
                message=(
                    f"New partnership request:\n\n"
                    f"Name: {submission.first_name} {submission.last_name}\n"
                    f"Email: {submission.email}\n"
                    f"Phone: {submission.phone_number}\n"
                    f"Organisation: {submission.organisation}\n"
                    f"Category: {submission.partnership_category}\n"
                    f"Message:\n{submission.message}"
                ),
                from_email=submission.email,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            return redirect("thank_you_page")  # Replace with your thank-you page URL
    else:
        form = PartnershipForm()

    return render(request, "website/partnership_collaboration.html", {"form": form})


def thank_you_view(request):
    return render(request, "website/thank_you.html")


def event_list(request):
    events = Event.objects.all()  # Get all events

    # Filter events based on upcoming or past
    upcoming_events = events.filter(event_type="upcoming")
    past_events = events.filter(event_type="past")

    # Paginate the lists
    paginator_upcoming = Paginator(upcoming_events, 5)  # 5 events per page
    paginator_past = Paginator(past_events, 5)

    page_number_upcoming = request.GET.get("page_upcoming")
    page_number_past = request.GET.get("page_past")

    upcoming_page = paginator_upcoming.get_page(page_number_upcoming)
    past_page = paginator_past.get_page(page_number_past)

    return render(
        request,
        "website//event_list.html",
        {
            "upcoming_page": upcoming_page,
            "past_page": past_page,
        },
    )


def volunteer_list(request):
    volunteers = Volunteer.objects.all()
    return render(request, "website/volunteer_list.html", {"volunteers": volunteers})
