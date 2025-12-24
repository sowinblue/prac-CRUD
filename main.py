file_name = "to_minamkong.txt"

def create_m(text):
    with open("to_minamkong.txt","w",encoding="utf-8") as f:
        f.write("안녕하세요 강사님")
    print("메세지 생성")