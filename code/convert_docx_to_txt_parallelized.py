import os
import re
import textract
import multiprocessing as mp

source_directory = "../surveys/word/"
output_directory = "../surveys/plain_txt/"


def process_file(file_name):
    if re.search(r".docx#", file_name) is None:
        try:
            file_string = file_name.split(".")[0]
            dest_file_path = file_string + '.txt'

            # extract text from the file
            content = textract.process(os.path.join(source_directory,
                                                    file_name))

            # We create and open the new and we prepare to write the
            # Binary Data which is represented by the wb - Write Binary
            write_text_file = open(os.path.join(output_directory,
                                                dest_file_path),
                                   "wb")

            # write the content and close the newly created file
            write_text_file.write(content)
            write_text_file.close()
        except:
            print(f"Error converting: {file_name}")


if __name__ == '__main__':
    file_list = os.listdir(source_directory)

    with mp.Pool(mp.cpu_count()) as p:
        p.map(process_file, file_list)