from twilio.rest import Client

# Masukkan SID dan Auth Token yang didapat
account_sid = 'AC32ada6b57607523b956b175776dffa48'  # Gantilah dengan Account SID Anda
auth_token = 'a8a968dba53f504a89d1c6ed4914e22a'  # Gantilah dengan Auth Token Anda

client = Client(account_sid, auth_token)

message = client.messages.create(
    body='sok asik lo bangsat!',
    from_='whatsapp:+14155238886',  # Nomor WhatsApp Sandbox Anda
    to='whatsapp:+62895359611122'  # Nomor WhatsApp tujuan
)

print(f"Message SID: sok asik lo bangsat")
