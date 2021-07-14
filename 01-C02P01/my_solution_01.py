def reduce_file_path(path):
    result = []
    split_path = path.split("/")

    for s in split_path:
        if s not in ['/','.','', '..']:
            result.append(s)
        if s == '..' and len(result) > 0:
            result.pop()

    result = "/" + "/".join(result)

    return result




tests = [
    ("/home//user/courses/./Programming101-Python/week01/../", "/home/user/courses/Programming101-Python"),
    ("/", "/"),
    ("/srv/../", "/"),
    ("/srv/www/htdocs/wtf/", "/srv/www/htdocs/wtf"),
    ("/srv/www/htdocs/wtf", "/srv/www/htdocs/wtf"),
    ("/srv/./././././", "/srv"),
    ("/etc//wtf/", "/etc/wtf"),
    ("/etc/../etc/../etc/../", "/"),
    ("//////////////", "/"),
    ("/../", "/")
    ]

for test in tests:
    in_path, expected = test
    result = reduce_file_path(in_path)
    print(result, result == expected)