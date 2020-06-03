from django.contrib import messages
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

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone,
                          message=message, user_id=user_id)
        contact.save()

        messages.success(request, "Your message has been sent to the realtor, who'll get back to you shortly!")

        return redirect('/listings/' + listing_id)
