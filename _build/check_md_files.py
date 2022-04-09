import os

# 체커가 돌지 않도록 제외할 경로 설정
exclude_dir_starts_with = [
#        "../009_upbit/2022",
        "../.",
        "../_"
        ]

exclude_dir_match_with = [
#        "../README.md",
        "../index.md",
        "../google62fdc652437cf301.html",
        "../naverd4f8a457876d1cbdba15ad126ccbf06a.html",
        "../404.html"
        ]

def is_exclude_path(path):
    """ 제외할 경로인지 확인 """
    for keyword in exclude_dir_starts_with:
        if path.startswith(keyword):
            return True
    for keyword in exclude_dir_match_with:
        if keyword == path:
            return True
    return False

def add_line_into_body(yaml, line):
    """ YAML 헤더가 아닌 본문은 "BODY" 항목에 누적한다. """
    """ 공란일 경우는 누적하지 않는다. """
    """ 공란은 PADDING 항목으로 고정되도록 하기 위함이다. """
    """ 공란이 아닌 데이터가 한 번이라도 누적되면 그 이후의 공란으 저장된다."""
    if yaml["BODY"] == "" and line == "\n":
        return
    
    yaml["BODY"] = yaml["BODY"] + line

def read_yaml_header(arrLines, yaml):
    """ md 파일로부터 YAML 헤더 정보를 가져온다. """
    for line in arrLines:
        parsing_done = False

        # YAML 헤더 파싱이 모두 끝났다면 나머지 내용은 본문에 넣는다.
        if yaml["YAML_END"] == "---\n":
            add_line_into_body(yaml, line)
            continue

        # "---" 문자열이 나오면 YAML START인지 YAML END인지 판별한다.
        if line == "---\n":
            if yaml["YAML_START"] == "":
#                print("YAML header started!")
                yaml["YAML_START"] = line
                continue
            elif yaml["YAML_END"] == "":
#                print("YAML header end!")
                yaml["YAML_END"] = line
                continue
            else:
                add_line_into_body(yaml, line)
                continue

        # YAML 헤더를 파싱한다.
        for key in yaml.keys():
            if line.startswith(key):
                if yaml["YAML_START"] != "---\n":
                    # "---" 없이 YAML 헤더가 시작됨
                    print("Invalid YAML header :", line)
                    return 1
                yaml[key] = line
#                print(yaml[key])
                parsing_done = True
                break

        # YAML 헤더 목록에 없는 항목이 발견됨
        if not parsing_done:
#            print("Not defined YAML header :", line)
            yaml["YAML_START"] = "---\n"
            yaml["YAML_END"] = "---\n"
            add_line_into_body(yaml, line)

    return 0

def check_yaml_header(yaml, filename):
    """YAML 헤더에 누락된 부분이 있으면 기본 정보를 추가한다."""
    if yaml["YAML_START"] == "":
        yaml["YAML_START"] = "---\n"
    if yaml["title: "] == "":
        yaml["title: "] = "title: Need To Update\n"
    if yaml["description: "] == "":
        yaml["description: "] = "description: Need To Update\n"
    if yaml["YAML_END"] == "":
        yaml["YAML_END"] = "---\n"

    """YAML 헤더 내용과 본문 내용을 대체한다"""
    f = open(filename, 'w')
    f.write(yaml["YAML_START"])
    f.write(yaml["title: "])
    f.write(yaml["description: "])
    f.write(yaml["YAML_END"])
    f.write(yaml["PADDING"])
    f.write(yaml["BODY"])
    f.close()

def get_yaml_header(filename):
    """MD 파일을 읽어와서 파싱하고 변환한다."""
    arrLines = []
    yaml = { "YAML_START" : "",
            "title: " : "",
            "description: " : "",
            "YAML_END" : "",
            "PADDING" : "\n\n",
            "BODY" : "" }

    cnt = 0

    f = open(filename, 'r')
    while True:
        line = f.readline()
        if line == '':
            break

        arrLines.append(line)
        cnt = cnt + 1

#    print( "{} lines read".format(cnt))
    f.close()

    if read_yaml_header(arrLines, yaml):
        return null

    return yaml

def make_md_file_add_link(fp, title, desc, file):
    print("make_md_file_add_link({}, {}, {})".format
            (title, desc, file))
    if len(file) > 3 and file[-3:] == ".md":
        file = "{}.html".format(file[:-3])
    fp.write("\n\n[{}]({} '{}')\n".format(
        title, file, desc))
    fp.write("---\n\n\n")
    fp.write("{}\n".format(desc))

def make_md_file(dir):
    """_README.md 파일로부터 README.md 파일을 작성한다."""
    print("make_md_file :", dir)
    f_wr = open(dir + "/README.md", 'w')
    f_rd = open(dir + "/_README.md", 'r')

    lines = f_rd.readlines()
    f_wr.writelines(lines)
    f_rd.close()

    files = os.listdir(dir)
    files.sort()
    for file in files:
        path = "{}/{}".format(dir, file)
#        print( "path :", path)
        if is_exclude_path(path):
            print("  Excluding :", path)
            continue
        elif file[-9:] == "README.md" or file[-8:] == "index.md":
            continue
        elif len(file) > 3 and file[-3:] == ".md":
            yaml = get_yaml_header(path)
#            print(yaml)
            make_md_file_add_link(f_wr,
                    yaml['title: '][7:-1],
                    yaml['description: '][13:-1],
                    file)
        elif len(file) > 5 and file[-5:] == ".html":
            f_wr.write("\n\n[{}]({})\n".format(file, file))
        elif os.path.isdir(path):
            index_path = path + "/index.md"
            readme_path = path + "/README.md"
            link_path = file + "/index.html"
            if not os.path.exists(index_path):
                if not os.path.exists(readme_path):
                    continue
                os.symlink("README.md", index_path)

            yaml = get_yaml_header(index_path)
            make_md_file_add_link(f_wr,
                    yaml['title: '][7:-1],
                    yaml['description: '][13:-1],
                    link_path)
#        else:
#            print("skip! {} {}".format(len(file), file[-3:]))

def iterate_directory(dir):
    """디렉토리를 순회한다."""
    print("iterate_directory :", dir)
    files = os.listdir(dir)
    files.sort()
    for file in files:
        path = "{}/{}".format(dir, file)
#        print( "file : {}".format(path) )
        if file == "_README.md":
            print("  Make README.md")
            make_md_file(dir)
        elif is_exclude_path(path):
            print("  Excluding :", path)
            continue
        elif file.endswith(".md"):
#            print("  Check md file")
            yaml = get_yaml_header(path)
            check_yaml_header(yaml, dir + "/" + file)
        elif os.path.isdir(path):
            iterate_directory(path)

def main():
    iterate_directory("..")

if __name__ == '__main__':
    main()
