def main():
    faces = input("How are you feeling today? ")
    convert(faces)


def convert(faces):
    faces = faces.replace(":)", "😀")
    faces = faces.replace(":l", "😐")
    faces = faces.replace(":|", "😐")
    faces = faces.replace(":I", "😐")
    faces = faces.replace(":(", "☹️")
    print(faces)


main()
