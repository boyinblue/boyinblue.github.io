import os

# 홈 디렉토리 경로 가져와서 토큰 파일 경로명 구하기
home_dir = os.path.expanduser('~')
token_file = "{}/.git-credentials".format(home_dir)

# 토큰 파일이 존재하지 않는 경우 예외 처리
if not os.path.exists(token_file):
    print("Token File Not exists :", token_file)
    exit

# 토큰 파일 열기
fp = open(token_file, 'r')

# 라인 파싱하기
lines = fp.readlines()

for line in lines:
    # "https://"로 시작하는 부분 제거
    # 기존 : https://{user}:{token}@github.com
    # 변경 : {user}:{token}@github.com
    line = line.replace("https://", "")

    # '@' 이하 부분 제거
    # 기존 : {user}:{token}@github.com
    # 변경 : {user}:{token}
    idx = line.index('@')
    line = line[0:idx]

    # username 가져오기
    idx = line.index(':')
    github_user = line[0:idx]
    github_token = line[idx+1:]

    # 출력하기
    print("github_user :", github_user)
    print("github_token :", github_token)
