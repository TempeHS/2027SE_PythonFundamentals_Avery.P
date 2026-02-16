def main():
    file = input("Name your file type: ")
    filecheck(file)


def filecheck(i):
    if i.endswith("gif"):
        print("image/gif")
    elif i.endswith("jpg") or i.endswith("jpeg"):
        print("image/jpeg")
    elif i.endswith("png"):
        print("image/png")
    elif i.endswith("pdf"):
        print("application/pdf")
    elif i.endswith("txt"):
        print("text/txt")
    elif i.endswith("zip"):
        print("file/zip")
    else:
        print("application/octet-stream")


main()
