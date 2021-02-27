import re

def text_process(text):
    """ 
    Process user input text.

    text, takes user sumitted plain text and formats it as per the WoT
    specification.
    """
#    text = text.replace("\r\n\r\n", "<br><hr><br>")
    text_list = text.split(".")
    new_list = []

    for item in text_list:
        new_string = "<li>" + item + ".</li>"
        new_list.append(new_string)

    new_list = new_list[:-1]
    new_string = re.sub('<li>.</li>', '', new_string)
    new_string = new_string.join(new_list)

    return new_string
