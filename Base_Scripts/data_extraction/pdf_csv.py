import tabula
import os
from tqdm import tqdm

cur_dir = os.getcwd()
directory = cur_dir + "/data/arrests/"
folder = directory + "/tables/"


def save_file(file):
    print(file)
    # tables = tabula.read_pdf(directory + file, pages="all") # This loads the pdf into tabula
    tables = directory + file
    # print("Read")

    folder_name = folder + file.replace(
        ".pdf", "/"
    )  # Converts the file's name into a folder

    # save them in a folder

    if not os.path.isdir(folder):
        print("Making folder")
        os.makedirs(folder)

    # iterate over extracted tables and export as excel individually
    for table in enumerate(
        tqdm(tables, desc="Tables", position=1, leave=True), start=1
    ):
        try:
            # print("Working... this may take a while")
            tabula.io.convert_into(
                tables, folder_name, output_format="csv", pages="all"
            )
        except tabula.errors.JavaNotFoundError:
            print("Make sure that Java 8+ JRE or JDK is in your PATH")
        # except ValueError:
        # print("This seems to mean that the end of the file is reached. Not sure why it isn't handled")
        # table.to_excel(os.path.join(folder_name, f"table_{i}.xlsx"), index=False)


# Count number of files
pdf_count = 0
for file in os.listdir(directory):
    if file.endswith(".pdf"):
        pdf_count += 1
print("Total PDFS: " + str(pdf_count))


# read PDF file
print("Working... this may take a while")
for file in tqdm(os.listdir(directory), desc="Files", position=0, leave=True):
    if file.endswith(".pdf"):
        save_file(file)
