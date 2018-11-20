#!/usr/bin/env python
# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
from smtplib import SMTP_SSL

def enviar_correo(correo_creado):
    from_address = "loginproyecto2018@gmail.com"
    to_address = correo_creado
    message = "Su usuario ha sido creado "

    mime_message = MIMEText(message, "plain")
    mime_message["From"] = from_address
    mime_message["To"] = to_address
    mime_message["Subject"] = "Registro exitoso"

    smtp = SMTP_SSL(host="smtp.gmail.com",port=465) 
    smtp.ehlo()
    smtp.login(from_address, "programacion1")

    smtp.sendmail(from_address, to_address, mime_message.as_string())
    smtp.quit()
