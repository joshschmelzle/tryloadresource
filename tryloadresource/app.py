import pkg_resources


def run():
    txt_path = pkg_resources.resource_filename("tryloadresource", "foo.txt")
    print(f"DEBUG: {txt_path}")
    with open(txt_path) as f:
        print(f.read())
