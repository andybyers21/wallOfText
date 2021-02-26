def text_process(text):
    """ 
    Process user input text.
    """
    # NOTE: the last line will also have an orphan <p> tag
    # NOTE: this assumes proper use of full stops in the input text
    
    # Identify line breaks and insert <hr> tag 
    text = text.replace("\n", "<hr>" )

    # Add bullet point and <p> tag to first line
    text = "<p>- " + text

    # Split lines at full stop and add bullet point
    text = text.replace('.', '.</p>\n<p>- ')

    # Remove the orphan bullet point and <p> tag

    return text


