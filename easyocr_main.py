import easyocr


def text_from_image(file_path, text_file_name="result.txt"):
    reader = easyocr.Reader(["en"])
    result = reader.readtext(file_path, detail=0, paragraph=True)

    with open(text_file_name, "w") as file:
        for line in result:
            file.write(f"{line}\n")

    return f"Result wrote into {text_file_name}"


def main():
    file_path = input("Enter a file path: ")
    print(text_from_image(file_path=file_path, text_file_name="new_file_name"))


if __name__ == "__main__":
    main()
