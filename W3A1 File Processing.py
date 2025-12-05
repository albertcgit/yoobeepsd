class FileProcessing:
    def read_and_print(self, input_file):
        with open(input_file, "r", encoding="utf-8") as f:
            content = f.read()
            print(content)

    def count_asterisk(self, input_file):
        with open(input_file, "r", encoding="utf-8") as f:
            content = f.read()
            print(f"The number of * is {content.count("*")}")

if __name__ == "__main__":

    object = FileProcessing()

    input_file = r"C:\\Users\\Albert\\Documents\\1_Yoobee Files\\1_Professional Software Development\\Week 3\\demo_file.txt"
    object.read_and_print(input_file)
    object.count_asterisk(input_file)