from twilio.rest import Client

# Masukkan SID dan Auth Token yang didapat
account_sid = 'AC32ada6b57607523b956b175776dffa48'  # Gantilah dengan Account SID Anda
auth_token = 'b4cd6163c1ecc62bd5fc860ca3204017'  # Gantilah dengan Auth Token Anda

client = Client(account_sid, auth_token)

message = client.messages.create(
    body='Hello, this is a test message from Twilio WhatsApp bot!',
    from_='whatsapp:+14155238886',  # Nomor WhatsApp Sandbox Anda
    to='whatsapp:+628978825442'  # Nomor WhatsApp tujuan
)

print(f"Message SID: {message.sid}")
