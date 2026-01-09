from django.shortcuts import render, redirect
from django.contrib import messages   # Flash messages uchun
from .models import Contact
from .forms import ContactSubmissionForm
from home.models import SocialMediaCard
import telegram

# Telegram konfiguratsiyasi
BOT_TOKEN = '7972750760:AAGMWwgmDJ6Gzcl9KrMYcfO9JfTc1shPkss'
CHAT_ID = '7251438309'

def contact_view(request):
    contacts = Contact.objects.all()
    social_media = SocialMediaCard.objects.all()
    form = ContactSubmissionForm()

    if request.method == 'POST':
        form = ContactSubmissionForm(request.POST)
        if form.is_valid():
            # Form ma'lumotlarini olish
            full_name = form.cleaned_data['full_name']
            age = form.cleaned_data['age']
            region = form.cleaned_data['region']
            phone_number = form.cleaned_data['phone_number']

            # Telegramga yuboriladigan xabar
            message = (
                f"📝 Yangi murojaat:\n\n"
                f"👤 Ism: {full_name}\n"
                f"🎂 Yosh: {age}\n"
                f"📍 Hudud: {region}\n"
                f"📞 Tel: {phone_number}"
            )

            # Bot orqali yuborish
            bot = telegram.Bot(token=BOT_TOKEN)
            bot.send_message(chat_id=CHAT_ID, text=message)

            # Flash message qo‘shish
            messages.success(request, "✅ Murojaatingiz muvaffaqiyatli yuborildi!")

            return redirect('contact')  # Sahifa yangilanadi

    return render(request, 'contact/contact.html', {
        'contacts': contacts,
        'social_media': social_media,
        'form': form,
    })
