#!/usr/bin/env python3

import os
from urllib import parse

HOMEPAGE_URL = "boyinblue.github.io"

# INPUT
SITEMAP_LIQUID = "../sitemap-liquid.txt"

# OUTPUT
SITEMAP_XML_FILE = "../sitemap.xml"
SITEMAP_TXT_FILE = "../sitemap.txt"

#############################################
# 체커가 돌지 않도록 제외할 경로 설정
#############################################
exclude_dir_starts_with = [
        "../.",
        "../_build",
        "../_posts",
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

def get_perma_link(filename):
    f = open(filename, 'r')
    while True:
        line = f.readline()
        if line == '':
            break
        elif line.startswith("permalink: "):
            permalink = line[11:]
            return permalink
    return None

def write_url(url, fp_xml, fp_txt):
    encoded_url=parse.quote(url.replace('\n',''))
    fp_xml.write("<url>")
    fp_xml.write("<loc>https://{}</loc>".format(encoded_url))
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
            permalink = get_perma_link(path)
            if permalink == None:
                write_url(HOMEPAGE_URL + path[2:], fp_xml, fp_txt)
            else:
                write_url(HOMEPAGE_URL + permalink, fp_xml, fp_txt)

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
    iterate_directory("..", fp_xml, fp_txt)

    # Tail
    fp_xml.write('</urlset>\n')

    # File Close
    fp_xml.close()
    fp_txt.close()

if __name__ == '__main__':
    main()
