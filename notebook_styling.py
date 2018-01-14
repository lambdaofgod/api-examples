from IPython.display import Markdown, display

def print_bold(string):
    display(Markdown("**{}**".format(string)))
