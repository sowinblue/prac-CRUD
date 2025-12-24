file_name = "to_minamkong.txt"

def newcreate_m(text):
    with open("to_minamkong.txt","w",encoding="utf-8") as f:
        f.write(text)
        print("메세지 생성")



# def addcreate_m(addtext):
#     with open("to_ninamkong","r",enconding="utf-8") as f:
#         f.write(addtext)
#         print("메세지 추가")


newcreate_m("안녕하세요 강사님")
