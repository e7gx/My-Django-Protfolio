from django.shortcuts import render
from django.core.mail import send_mail
from .models import Message

def home(request):
    success = False
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message_text = request.POST.get("message")

        if name and email and message_text:
            Message.objects.create(
                name=name,
                email=email,
                message=message_text,
            )
            html_message = f"""
                            <html>
                            <body style="margin:0; padding:0; background-color:#f0f2f5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
                                <table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="background-color:#f0f2f5; padding: 30px 0;">
                                <tr>
                                    <td align="center">
                                    <table role="presentation" cellpadding="0" cellspacing="0" width="600" style="background-color:#ffffff; border-radius:12px; box-shadow:0 4px 12px rgba(0,0,0,0.1); padding: 30px; border-collapse: separate;">
                                        <tr>
                                        <td style="background-color:#004aad; border-radius:12px 12px 0 0; padding: 20px; text-align:center;">
                                            <h1 style="color:#ffffff; font-size:24px; margin:0; font-weight:700;">📩 New Portfolio Message</h1>
                                        </td>
                                        </tr>
                                        <tr>
                                        <td style="padding: 25px 30px; color:#333333; font-size:16px; line-height:1.5;">
                                            <p style="margin: 0 0 15px 0;"><strong style="color:#004aad;">Name:</strong> {name}</p>
                                            <p style="margin: 0 0 15px 0;"><strong style="color:#004aad;">Email:</strong> {email}</p>
                                            <p style="margin: 0 0 10px 0; font-weight: bold; color:#004aad;">Message:</p>
                                            <p style="margin: 0; white-space: pre-wrap;">{message_text}</p>
                                        </td>
                                        </tr>
                                        <tr>
                                        <td style="padding: 20px 30px; font-size: 12px; color: #888888; text-align: center; border-top: 1px solid #e0e0e0; border-radius: 0 0 12px 12px;">
                                            This message was sent from your portfolio website.
                                        </td>
                                        </tr>
                                    </table>
                                    </td>
                                </tr>
                                </table>
                            </body>
                            </html>
"""
            send_mail(
                subject=f"Portfolio Message from {name}",
                message=f"From: {email}\n\n{message_text}",
                from_email="saqerappdjango@gmail.com",  # must match EMAIL_HOST_USER
                recipient_list=["abdullah.i.alghamdi23@gmail.com"],
                fail_silently=False,
                html_message=html_message,
            )
            success = True

    return render(request, "main/home.html", {"success": success})