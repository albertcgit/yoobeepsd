class FileProcessing:
    def read_and_print(self, input_file):
        content = input_file.read()
        print(content)
        input_file.close()

    def count_asterisk(self, input_file):
        content = input_file.read()
        print(f"The number of * is {content.count("*")}")
        input_file.close()

if __name__ == "__main__":

    object = FileProcessing()
    input_file = open("C:\\Users\\Albert\\Documents\\1_Yoobee Files\\1_Professional Software Development\\Week 3\\demo_file.txt", "r", encoding="utf-8")
    object.read_and_print(input_file)
    input_file = open("C:\\Users\\Albert\\Documents\\1_Yoobee Files\\1_Professional Software Development\\Week 3\\demo_file.txt", "r", encoding="utf-8")
    object.count_asterisk(input_file)