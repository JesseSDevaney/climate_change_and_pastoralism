import os
import re
import textract

source_directory = "../surveys/word/"
output_directory = "../surveys/plain_txt/"

for process_file in os.listdir(source_directory):
    # do not include locked .docx files in the program
    if re.search(r".docx#", process_file) is None:
        file_name = process_file.split(".")[0]
        dest_file_path = file_name + '.txt'

        # extract text from the file
        content = textract.process(os.path.join(source_directory, process_file))

        # We create and open the new and we prepare to write the Binary Data
        # which is represented by the wb - Write Binary
        write_text_file = open(os.path.join(output_directory, dest_file_path),
                               "wb")

        # write the content and close the newly created file
        write_text_file.write(content)
        write_text_file.close()
