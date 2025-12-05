class FileProcessing:
    def append_and_print(self, input_file):
        with open(input_file, "a", encoding="utf-8") as f:
            f.write("End of File")

        with open(input_file, "r", encoding="utf-8") as f:
            content = f.read()
            print(content)

if __name__ == "__main__":

    object = FileProcessing()

    input_file = r"C:\\Users\\Albert\\Documents\\1_Yoobee Files\\1_Professional Software Development\\Week 3\\demo_text.txt"
    object.append_and_print(input_file)