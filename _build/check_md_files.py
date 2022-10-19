#!/usr/bin/env python3

import os


#############################################
# 체커가 돌지 않도록 제외할 경로 설정
#############################################
exclude_dir_starts_with = [
        "../009_upbit/2022",
        "../.",
        "../_",
        "../test/"
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

#############################################
# 추가를 하려는 경로가 이미 존재하는지 확인
#############################################
def is_exist_file(lines, file):
    for line in lines:
        if line.find(file) != -1:
            return True
    return False

#############################################
# MD 파일 공통 작업 (ex : 편집 링크 추가)
#############################################
EDIT_URL = "https://www.github.com/boyinblue/boyinblue.github.io/edit/main/"

def check_md_file(dir, file):
    print("check_md_file({},{})".format(dir, file))
    path = dir + "/" + file

    edit_url = EDIT_URL + path
    if path[0:3] == "../":
        edit_url = EDIT_URL + path[3:]

    if not os.path.isfile(path):
        return
    elif is_exclude_path(path):
        return

    f_rd = open(path, "r")
    lines = f_rd.readlines()
    f_rd.close()

    if is_exist_file(lines, EDIT_URL):
        return

    f_wr = open(path, "w")
    f_wr.writelines(lines)

    f_wr.write("\n\n".format(file))
    f_wr.write("[✏️ ]({} \'수정하기\')\n".format(edit_url))
    f_wr.write("\n")

#############################################
# 새로운 디렉토리를 추가
#############################################
def add_link_to_index(dir, filename):
    print("add_link_to_index({},{})".format(dir, filename))
    path = dir + "/" + filename

    files = os.listdir(dir)
    files.sort(reverse=True)

    if not os.path.isfile(path):
        print("There is no file", filename)
        return
    elif is_exclude_path(path):
        return

    f_rd = open(path, "r")
    lines = f_rd.readlines()
    f_rd.close()

    f_wr = open(path, "w")
    f_wr.writelines(lines)

    for file in files:
        html_file = file.replace(".md",".html")
        path2 = "{}/{}".format(dir, file)
        if file == filename:
#            print("Skip : Self :", path2)
            continue
        elif is_exclude_path(path2):
#            print("Skip : Exclude Dir :", path2)
            continue
        elif is_exist_file(lines, html_file):
#            print("Skip : Exists : ", path2)
            continue
        elif os.path.isdir(path2) and os.path.isfile(path2+"/index.md"):
            yaml = get_yaml_header(path2 + "/index.md")
            f_wr.write("\n\n".format(file))
            f_wr.write("[✔️  {}]({} \'{}\')\n---\n\n\n".format(
                    yaml['title: '][7:-1],
                    file,
                    yaml['description: '][13:-1]))
            f_wr.write(yaml['description: '][13:-1])
            f_wr.write("\n")
        elif file.endswith(".md"):
            yaml = get_yaml_header(path2)
            file = "{}.html".format(file[:-3])
            f_wr.write("\n\n".format(file))
            f_wr.write("[✔️  {}]({} \'{}\')\n---\n\n\n".format(
                    yaml['title: '][7:-1],
                    file,
                    yaml['description: '][13:-11]))
            f_wr.write(yaml['description: '][13:-1])
            f_wr.write("\n")
            
    f_wr.close()

#############################################
# md 파일에 이전글 다음글 추가
#############################################
def add_link_to_md(dir, filename, prev, next):
    print("add_link_to_md({},{})".format(dir, filename))
    path = dir + "/" + filename
    if filename == "index.md":
        index = None
    else:
        index = "index.md"

    if is_exclude_path(path):
        return

    f_rd = open(path, "r")
    lines = f_rd.readlines()
    f_rd.close()

    f_wr = open(path, "w")
    f_wr.writelines(lines)

    files = [ prev, next, index ]
    for file in files:
        if file is None:
            continue

        path2 = "{}/{}".format(dir, file)
        if is_exclude_path(path2):
#            print("Skip : Exclude Dir :", path2)
            continue

        html_file = file.replace(".md",".html")
        if is_exist_file(lines, html_file):
#            print("Skip : Exists : ", path2)
            continue

        if file == prev:
            kind = "🔼 이전글"
        elif file == next:
            kind = "🔽 다음글"
        elif file == index:
            kind = "⬅️ 이 카테고리 글 전체보기"

        yaml = get_yaml_header(path2)
        file = "{}.html".format(file[:-3])
        f_wr.write("\n\n".format(file))
        f_wr.write("[{} : {}]({} \'{}\')\n---\n\n\n".format(
                kind,
                yaml['title: '][7:-1],
                file,
                yaml['description: '][13:-11]))
        f_wr.write(yaml['description: '][13:-1])
        f_wr.write("\n")
            
    f_wr.close()

def add_line_into_body(yaml, line):
    """ YAML 헤더가 아닌 본문은 "BODY" 항목에 누적한다. """
    """ 공란일 경우는 누적하지 않는다. """
    """ 공란은 PADDING 항목으로 고정되도록 하기 위함이다. """
    """ 공란이 아닌 데이터가 한 번이라도 누적되면 """
    """ 그 이후의 공란으로 저장된다."""
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

def iterate_directory(dir):
    """디렉토리를 순회한다."""
    print("iterate_directory :", dir)

    """ 실행 파일이 있으면 미리 실행한다."""
    if os.path.isfile("_build.py"):
        os.system("pushd {}".format(dir))
        os.system("_build.py")
        os.system("popd")

    files = os.listdir(dir)
    files.sort(reverse=True)

    files2 = []

    for file in files:
        path = "{}/{}".format(dir, file)
#        print( "file : {}".format(path) )
        if is_exclude_path(path):
            print("  Excluding :", path)
            continue
        elif os.path.isdir(path):
            add_link_to_index(path,"index.md")
            check_md_file(path,"index.md")
            iterate_directory(path)
            continue
        elif file == "index.md":
            continue
        elif file.endswith(".md"):
#            print("  Check md file", file)
            files2.append(file)

    prev = None
    for idx in range(len(files2)):
        next = None
        file = files2[idx]
        if idx > 1:
            prev = files2[idx-1]
        if idx < len(files2) - 1:
            next = files2[idx+1]
        path = "{}/{}".format(dir, file)
        yaml = get_yaml_header(path)
        check_yaml_header(yaml, dir + "/" + file)
        add_link_to_md(dir,file,prev,next)
        check_md_file(dir,file)

def main():
    iterate_directory("..")

if __name__ == '__main__':
    main()
