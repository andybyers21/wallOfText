import re

def title_process(title):
    if len(title) == 0:
        title = "your wall of text"
    output_title = ""
    list_of_words = title.split()
    for elem in list_of_words:
        if len(output_title) > 0:
            output_title = output_title + " " + elem.strip().capitalize()
        else:
            output_title = elem.capitalize()
    if not output_title:
        return title
    else:
        return output_title


def text_process(text):
    """ 
    Process user input text.

    text, takes user sumitted plain text and formats it as per the WoT
    specification.
    """
    # FIXME: if last line does not have a . it gets ignored.
    text = re.sub("\r\n\r\n", "<hr>", text)
    text_list = re.findall('.*?[.!\?]+', text, re.IGNORECASE)
    # TODO: also need to check for speach in text ""
    new_list = []

    for item in text_list:
        new_string = item.lstrip()
        new_string = new_string.capitalize()
        new_string = "<li>" + new_string + "</li>"
        new_string = re.sub('<li><hr>', '<hr><br><li>', new_string)
        # FIXME: edge case, this does not capatalize first letter on new line
        # due to additional <hr> tags at start of list item.:w
        new_list.append(new_string)
    
    str1 = ""  
    
    for ele in new_list:  
        str1 += ele   
    
    return str1 

