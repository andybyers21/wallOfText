def text_process(text):
    """ 
    Process user input text.
    """
    # Identify line breaks and insert <hr> tag 
    # NOTE: the last line will also have an orphan <p> tag
    # NOTE: this assumes proper use of full stops in the input text
    ### text_a = text.removeprefix('"').removesuffix('"')
    text_b = "<p>" + text
    new_text = text_b.replace('.', '.</p>\n<p>')


    # Add bullet point to first line
    
    # Split lines at full stop and add bullet point

    return new_text


