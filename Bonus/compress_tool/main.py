import FreeSimpleGUI as sg 
from zip_creator import make_archive, extract_archive
sg.theme("Black")

label1 = sg.Text("Select files")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
archive_message = sg.Text(key="output", text_color="green")

extract_button = sg.Button("Extract")
extract_message = sg.Text(key="output", text_color="green")

col1 = sg.Column([[label1], [label2]])
col2 = sg.Column([[input1], [input2]])
col3 = sg.Column([[choose_button1], [choose_button2]])
 
window = sg.Window("Archive Extractor",
                   layout=[[col1, col2, col3], [compress_button, archive_message],
                           [extract_button,extract_message]])


while True:
       event, values = window.read()
       print(event, values)
       match event:
              case "Compress":
                     filepaths = values["files"].split(";")
                     folder = values["folder"]
                     make_archive(filepaths, folder)
                     window["output"].update(value="Compression completed!")
              case "Extract":
                     archivepath = values["files"].split(";")
                     dest_dir = values["folder"]
                     extract_archive(archivepath, dest_dir)
                     window["output"].update(value="Compression completed!")
              case sg.WIN_CLOSED:
                     break
                     
                     
window.close()
