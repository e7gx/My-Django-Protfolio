from django.shortcuts import render
from django.core.mail import send_mail
from django.utils import timezone
from django.template.loader import render_to_string
from .models import Message
import html

def home(request):
    success = False
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message_text = request.POST.get("message")

        if name and email and message_text:
            # Save to database
            Message.objects.create(
                name=name,
                email=email,
                message=message_text,
            )
            
            # Get current time
            current_time = timezone.now().strftime("%B %d, %Y at %I:%M %p")
            
            # HTML Email Template with exact color palette
            html_message = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <title>Portfolio Message</title>
                <!--[if mso]>
                <style type="text/css">
                    table {{ border-collapse: collapse; }}
                    .fallback-font {{ font-family: Arial, sans-serif !important; }}
                </style>
                <![endif]-->
                <style>
                    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700&display=swap');
                    
                    * {{
                        margin: 0;
                        padding: 0;
                        box-sizing: border-box;
                    }}
                    
                    body {{
                        font-family: 'Cairo', Arial, sans-serif;
                        background-color: #E6EDF4;
                        margin: 0;
                        padding: 0;
                        -webkit-font-smoothing: antialiased;
                        -moz-osx-font-smoothing: grayscale;
                    }}
                    
                    .email-wrapper {{
                        background-color: #E6EDF4;
                        padding: 20px 0;
                        width: 100%;
                        min-height: 100vh;
                    }}
                    
                    .email-container {{
                        max-width: 600px;
                        margin: 0 auto;
                        background-color: #ffffff;
                        border-radius: 12px;
                        overflow: hidden;
                        box-shadow: 0 10px 30px rgba(11, 54, 86, 0.15);
                        border: 2px solid #0B3656;
                    }}
                    
                    .header {{
                        background: linear-gradient(135deg, #0B3656 0%, #387580 100%);
                        padding: 30px 20px;
                        text-align: center;
                        color: #E6EDF4;
                    }}
                    
                    .header-icon {{
                        font-size: 32px;
                        margin-bottom: 10px;
                        display: block;
                    }}
                    
                    .header h1 {{
                        color: #BB9875;
                        font-size: 24px;
                        font-weight: 600;
                        margin: 0;
                        font-family: 'Cairo', Arial, sans-serif;
                    }}
                    
                    .content {{
                        padding: 30px 25px;
                        background-color: #E6EDF4;
                    }}
                    
                    .field-row {{
                        margin-bottom: 25px;
                        border: 2px solid #387580;
                        border-radius: 12px;
                        overflow: hidden;
                        background-color: #ffffff;
                    }}
                    
                    .field-header {{
                        background-color: #0B3656;
                        color: #E6EDF4;
                        padding: 15px 20px;
                        font-size: 14px;
                        font-weight: 600;
                        text-transform: uppercase;
                        letter-spacing: 0.5px;
                    }}
                    
                    .field-content {{
                        padding: 20px;
                        background-color: #ffffff;
                    }}
                    
                    .field-value {{
                        font-size: 16px;
                        color: #171A2C;
                        line-height: 1.5;
                        word-wrap: break-word;
                        font-weight: 500;
                    }}
                    
                    .message-field {{
                        border-color: #8C3C2C;
                    }}
                    
                    .message-field .field-header {{
                        background-color: #8C3C2C;
                        color: #E6EDF4;
                    }}
                    
                    .message-content {{
                        white-space: pre-wrap;
                        font-size: 15px;
                        line-height: 1.6;
                        color: #171A2C;
                        background-color: #E6EDF4;
                        padding: 18px;
                        border-radius: 8px;
                        border-left: 5px solid #BB9875;
                        margin-top: 12px;
                        border: 1px solid #BB9875;
                    }}
                    
                    .footer {{
                        background-color: #171A2C;
                        padding: 25px;
                        text-align: center;
                        border-top: 3px solid #BB9875;
                        color: #E6EDF4;
                    }}
                    
                    .footer-text {{
                        font-size: 13px;
                        margin: 0 0 10px 0;
                        font-weight: 500;
                        color: #E6EDF4;
                    }}
                    
                    .timestamp {{
                        font-size: 12px;
                        color: #BB9875;
                        font-style: italic;
                    }}
                    
                    .divider {{
                        height: 3px;
                        background: linear-gradient(90deg, #BB9875, #387580);
                        margin: 0 auto 15px auto;
                        width: 80px;
                        border-radius: 2px;
                    }}
                    
                    /* Mobile Responsive */
                    @media only screen and (max-width: 600px) {{
                        .email-container {{
                            margin: 0 10px;
                            border-radius: 8px;
                        }}
                        
                        .header {{
                            padding: 25px 15px;
                        }}
                        
                        .header h1 {{
                            font-size: 20px;
                        }}
                        
                        .content, .footer {{
                            padding: 25px 15px;
                        }}
                        
                        .field-content {{
                            padding: 15px;
                        }}
                    }}
                    
                    /* Dark mode support */
                    @media (prefers-color-scheme: dark) {{
                        .email-wrapper {{
                            background-color: #171A2C !important;
                        }}
                        
                        .email-container {{
                            background-color: #0B3656 !important;
                            border-color: #BB9875 !important;
                        }}
                        
                        .content {{
                            background-color: #0B3656 !important;
                        }}
                        
                        .field-content {{
                            background-color: #171A2C !important;
                        }}
                        
                        .field-value {{
                            color: #E6EDF4 !important;
                        }}
                    }}
                </style>
            </head>
            <body>
                <div class="email-wrapper">
                    <table cellpadding="0" cellspacing="0" border="0" width="100%">
                        <tr>
                            <td align="center">
                                <div class="email-container">
                                    <div class="header">
                                        <span class="header-icon">📧</span>
                                        <h1>رسالة جديدة من الموقع</h1>
                                    </div>
                                    
                                    <div class="content">
                                        <div class="field-row">
                                            <div class="field-header"> اسم المرسل</div>
                                            <div class="field-content">
                                                <div class="field-value">{html.escape(name)}</div>
                                            </div>
                                        </div>
                                        
                                        <div class="field-row">
                                            <div class="field-header"> البريد الإلكتروني</div>
                                            <div class="field-content">
                                                <div class="field-value">
                                                    <a href="mailto:{html.escape(email)}" style="color: #0B3656; text-decoration: none; font-weight: 600;">
                                                        {html.escape(email)}
                                                    </a>
                                                </div>
                                            </div>
                                        </div>
                                        
                                        <div class="field-row message-field">
                                            <div class="field-header"> نص الرسالة</div>
                                            <div class="field-content">
                                                <div class="message-content">{html.escape(message_text)}</div>
                                            </div>
                                        </div>
                                    </div>
                                    
                                    <div class="footer">
                                        <div class="divider"></div>
                                        <p class="footer-text">تم إرسال هذه الرسالة من موقع البورتفوليو الخاص بك</p>
                                        <div class="timestamp">
                                            تم الاستلام في {current_time}
                                        </div>
                                    </div>
                                </div>
                            </td>
                        </tr>
                    </table>
                </div>
            </body>
            </html>
            """
            
            # Plain text version for email clients that don't support HTML
            plain_message = f"""
رسالة جديدة من موقع البورتفوليو

الاسم: {name}
البريد الإلكتروني: {email}

الرسالة:
{message_text}

---
تم الاستلام في {current_time}
            """
            
            try:
                send_mail(
                    subject=f"ذيبان وصلتك رسالة من {name}",
                    message=plain_message,  # Plain text fallback
                    from_email="saqerappdjango@gmail.com",
                    recipient_list=["abdullah.i.alghamdi23@gmail.com"],
                    fail_silently=False,
                    html_message=html_message,  # HTML version
                )
                success = True
            except Exception as e:
                print(f"Email sending failed: {e}")
                success = False

    return render(request, "main/home.html", {"success": success})