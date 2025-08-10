from tools.sendMail import readExcel,send_mail

records = readExcel.invoke({})
print("Loded records")

print(records)
for r in records:
    try:
        send_mail.invoke({
            "recieverMail":r["Email"],
            "title" : r["Title"],
            "company":r["Company"]
        })
        print("sent")
    except Exception as e:
        print(e)
# print(f"Email sent to {r['Mail']}")