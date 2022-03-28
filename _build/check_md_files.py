import os
from bs4 import BeautifulSoup

def read_yaml_header(arrLines, yaml):
    for line in arrLines:
        parsing_done = False

        # YAML 헤더 파싱이 모두 끝났다면 나머지 내용은 본문에 넣는다.
        if yaml["YAML_END"] == "---\n":
            yaml["BODY"] = yaml["BODY"] + line
            continue

        # "---" 문자열이 나오면 YAML START인지 YAML END인지 판별한다.
        if line == "---\n":
            if yaml["YAML_START"] == "":
                print("YAML header started!")
                yaml["YAML_START"] = line
                continue
            elif yaml["YAML_END"] == "":
                print("YAML header end!")
                yaml["YAML_END"] = line
                continue
            else
                yaml["BODY"] = yaml["BODY"] + line
                continue

        # YAML 헤더를 파싱한다.
        for key in yaml.keys():
            if line.startswith(key):
                if not yaml_flag:
                    # "---" 없이 YAML 헤더가 시작됨
                    print("Invalid YAML header :", line)
                    return 1
                yaml[key] = line
                print(yaml[key])
                parsing_done = True
                break

        # YAML 헤더 목록에 없는 항목이 발견됨
        if not parsing_done:
#            print("Not defined YAML header :", line)
            yaml["YAML_START"] = "---\n"
            yaml["YAML_END"] = "---\n"
            yaml["BODY"] = yaml["BODY"] + line

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
            "PADDING" : "\n\n"
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
        print( "file : {}".format(path) )
        if file.endswith(".md"):
#            print("  Check md file")
            check_md_file(path)
        elif os.path.isdir(path):
            iterate_directory(path)

def main():
    iterate_directory("..")

if __name__ == '__main__':
    main()
