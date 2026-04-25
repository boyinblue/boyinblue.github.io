#!/usr/bin/env python3

import os
from datetime import datetime
from urllib import parse

HOMEPAGE_URL = "boyinblue.github.io"

# INPUT
SITEMAP_LIQUID = "../../sitemap-liquid.txt"

# OUTPUT
SITEMAP_XML_FILE = "../../sitemap.xml"
SITEMAP_TXT_FILE = "../../sitemap.txt"

#############################################
# 체커가 돌지 않도록 제외할 경로 설정
#############################################
exclude_dir_starts_with = [
        "../../.",
        "../../_build",
        "../../_posts",
        "../../_drafts",
        "../../test/",
        "../../docs/"
        ]

exclude_dir_match_with = [
#        "../../README.md",
        "../../index.md",
        "../../google62fdc652437cf301.html",
        "../../naverd4f8a457876d1cbdba15ad126ccbf06a.html",
        "../../404.html"
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

def get_perma_link(filename):
    front_matter = parse_front_matter(filename)
    return front_matter.get("permalink")

def _strip_yaml_value(value):
    value = value.strip()
    if len(value) >= 2 and ((value[0] == '"' and value[-1] == '"') or (value[0] == "'" and value[-1] == "'")):
        return value[1:-1]
    return value

def parse_front_matter(filename):
    """간단한 YAML front matter 파서 (top-level key만 사용)."""
    metadata = {}

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if not lines or lines[0].strip() != '---':
        return metadata

    for line in lines[1:]:
        stripped = line.strip()
        if stripped == '---':
            break
        if not stripped or stripped.startswith('#'):
            continue
        if ':' not in line:
            continue

        key, value = line.split(':', 1)
        key = key.strip()
        if not key:
            continue

        metadata[key] = _strip_yaml_value(value)

    return metadata

def get_lastmod(filename, front_matter=None):
    """lastmod 우선순위: last_modified_at > sitemap.lastmod > date > created_at > 파일 수정시각"""
    front_matter = front_matter or parse_front_matter(filename)

    for key in ("last_modified_at", "lastmod", "date", "created_at"):
        value = front_matter.get(key)
        if value:
            return value

    modified_ts = os.path.getmtime(filename)
    return datetime.fromtimestamp(modified_ts).astimezone().isoformat(timespec='seconds')

def write_url(url, fp_xml, fp_txt, lastmod=None):
    encoded_url=parse.quote(url.replace('\n',''))
    fp_xml.write("<url>\n")
    fp_xml.write("<loc>https://{}</loc>\n".format(encoded_url))
    if lastmod:
        fp_xml.write("<lastmod>{}</lastmod>\n".format(lastmod.strip()))
    fp_xml.write("</url>\n")

    fp_txt.write(encoded_url+"\n")

def iterate_directory(dir, fp_xml, fp_txt):
    """디렉토리를 순회한다."""
    print("iterate_directory :", dir)

    files = os.listdir(dir)
    files.sort(reverse=True)

    for file in files:
        path = "{}/{}".format(dir, file)
#        print( "file : {}".format(path) )
        if is_exclude_path(path):
            print("  Excluding :", path)
            continue
        elif os.path.isdir(path):
            iterate_directory(path, fp_xml, fp_txt)
            continue
        elif file.endswith(".md"):
            front_matter = parse_front_matter(path)
            permalink = front_matter.get("permalink")
            lastmod = get_lastmod(path, front_matter)
            if permalink == None:
                write_url(HOMEPAGE_URL + path[2:], fp_xml, fp_txt, lastmod)
            else:
                write_url(HOMEPAGE_URL + permalink, fp_xml, fp_txt, lastmod)

def main():
    # File Open
    fp_xml = open(SITEMAP_XML_FILE, "w")
    fp_txt = open(SITEMAP_TXT_FILE, "w")

    # Header
    fp_xml.write("---\n")
    fp_xml.write("layout: null\n")
    fp_xml.write("---\n")
    fp_xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    fp_xml.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

    # liquid scripts for posts
    f_rd = open( SITEMAP_LIQUID, "r" )
    lines = f_rd.readlines()
    f_rd.close()
    for line in lines:
        fp_xml.write(line)

    # URLs
    iterate_directory("../..", fp_xml, fp_txt)

    # Tail
    fp_xml.write('</urlset>\n')

    # File Close
    fp_xml.close()
    fp_txt.close()

if __name__ == '__main__':
    main()
