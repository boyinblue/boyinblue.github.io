import os
from bs4 import BeautifulSoup

# 체커가 돌지 않도록 제외할 경로 설정
exclude_dir_starts_with = [
        "../009_upbit/2022"
        ]

exclude_dir_match_with = [
        "../README.md"
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

    if yaml["YAML_START"] == "":
        yaml["YAML_START"] = "---\n"
    if yaml["title: "] == "":
        yaml["title: "] = "title: Need To Update\n"
    if yaml["description: "] == "":
        yaml["description: "] = "description: Need To Update\n"
    if yaml["YAML_END"] == "":
        yaml["YAML_END"] = "---\n"

    f = open(filename, 'w')
    f.write(yaml["YAML_START"])
    f.write(yaml["title: "])
    f.write(yaml["description: "])
    f.write(yaml["YAML_END"])
    f.write(yaml["PADDING"])
    f.write(yaml["BODY"])
    f.close()

def check_md_file(filename):
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
        return 1

    check_yaml_header(yaml, filename)

def iterate_directory(dir):
    files = os.listdir(dir)
    for file in files:
        path = "{}/{}".format(dir, file)
#        print( "file : {}".format(path) )
        if is_exclude_path(path):
            print("  Excluding :", path)
        elif file.endswith(".md"):
#            print("  Check md file")
            check_md_file(path)
        elif os.path.isdir(path):
            iterate_directory(path)

def main():
    iterate_directory("..")

if __name__ == '__main__':
    main()
