from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect

from contacts.models import Contact


def submit_message(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "You have already made an enquiry for this listing")
                return redirect('/listings/' + listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone,
                          message=message, user_id=user_id)
        contact.save()

        # Send email to the realtor (requires that the details are filled in settings.py
        # send_mail("Listing enquiry", "There has been an ebquiry for " + listing +
        #           ". Sign into the admin panel for more information", "zargindustriesuk@gmail.com",
        #           [realtor_email, "samcarty311@gmail.com"], fail_silently=False)

        messages.success(request, "Your enquiry has been sent to the realtor who'll get back to you shortly!")

        return redirect('/listings/' + listing_id)
