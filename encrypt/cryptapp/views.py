from django.shortcuts import render, redirect
from .crypto import generate_key, encrypt_text, decrypt_text
from .models import EncryptedText

def home(request):
    return render(request, 'home.html')

def encrypt(request):
    if request.method == 'POST':
        plain_text = request.POST.get('plain_text')
        key = generate_key()
        encrypted_text = encrypt_text(key, plain_text)
        EncryptedText.objects.create(encrypted_text=encrypted_text)
        return render(request, 'encrypt_result.html', {'key': key.decode()})
    return render(request, 'encrypt.html')

def decrypt(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        encrypted_text = EncryptedText.objects.first().encrypted_text

        try:
            decrypted_text = decrypt_text(key.encode(), encrypted_text)
            return render(request, 'decrypt_result.html', {'decrypted_text': decrypted_text})
        except Exception as e:
            return render(request, 'decrypt_result.html', {'error': str(e)})

    return render(request, 'decrypt.html')
