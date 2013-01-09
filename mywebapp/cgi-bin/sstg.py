from string import Template

def start_response(resp="text/html"):
    return "Content-type: " + resp + "\n\n"

def include_header(the_title):
    with open("templates/header.html") as header_file:
        header_text = header_file.read()
    header = Template(header_text)
    return header.substitute(title=the_title)

def start_form(the_method, the_action):
    return "<form method=\"" + the_method + "\" action=\"" + the_action + "\">"


def radio_buttons(a_name, list_items):
    s = ""
    for each_item in list_items:
        s += radio_button(a_name, each_item) + "<br/>"
    return s


def radio_button(a_name, a_value):
    return '<input type="radio" name="%s" value="%s">%s</input>' % (a_name, a_value, a_value)

def end_form():
    return "<input type=\"submit\" name=\"Submit\"></form>"

def include_footer(the_links):
    with open("templates/footer.html") as footer_file:
        footer_text = footer_file.read()
    link_string = "<table><tr>"
    for key in the_links:
        link_string +=  "<td><a href=\"" + the_links[key] + "\">" + key + "</a></td>"
    link_string += "</tr></table>"
    footer = Template(footer_text)
    return footer.substitute(links=link_string)


if __name__ == '__main__':
    ll = ["rakesh","eats","monkeys"]

    print radio_buttons("whatsup",ll)




























