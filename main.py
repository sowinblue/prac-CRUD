file_name = "to_minamkong.txt"

def newcreate_m(text):
    with open("to_minamkong.txt","w",encoding="utf-8") as f:
        f.write(text)
        print("메세지 생성")



def addcreate_m(addtext):
    with open("to_minamkong.txt","a", encoding="utf-8") as f:
        f.write(addtext)
        print("메세지 추가")


def delete_m(deletetext):
    with open("to_minamkong.txt","w",encoding="utf-9") as f:
        f.write(" ")
        print("메세지 삭제")


newcreate_m("안녕하세요 강사님")
addcreate_m("\n근데 제가 드릴 말씀이 있습니다")
addcreate_m("\n...")
addcreate_m("\n여기까지 하겠습니다.")
addcreate_m("\n하하하")


