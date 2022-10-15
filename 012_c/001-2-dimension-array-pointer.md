---
title: C언어에서 2차원 배열 포인터 사용 방법
description: C언어에서 2차원 배열 포인터를 사용하는 방법에 대해서 설명합니다.
---


C언어에서 2차원 배열 포인터 사용 방법
===


본 페이지에서는 C언어에서 2차원 배열 포인터를 사용하는 방법에 대해서 설명합니다.


2차원 배열 포인터란?
---


C언어를 처음 배우는 사람들에게 가장 어려운 것 중의 하나를 꼽으라면, 
단연 포인터라고 할 수 있겠습니다. 


단순한 단일 변수의 포인터는 큰 어려움이 없지만, 
배열 포인터나 함수 포인터 등을 접하기 시작하면 
굉장히 복잡하게 느껴지고 헷갈리기 마련입니다. 


특히, <code>배열 포인터</code>와 <code>포인터 배열</code>은 
굉장히 헷갈리면서도 혼동하기 쉬운 개념이라고 믿어 의심치 않습니다. 


### 1. 2차원 배열 선언


2차원 배열 포인터에 대해서 설명하기에 앞서서, 
2차원 배열을 먼저 생각해 보겠습니다. 


<code>int a[2][3] = { 100, 101, 102, 103, 104, 105 };</code>


위의 코드를 통해서 우리는 2차원 배열을 선언하고, 사용할 수 있습니다. 


|   | Col #0 | Col #1 | Col #2 |
|--|--|--|--|
| Row #0 | 100 | 101 | 102 |
| Row #1 | 103 | 104 | 105 |


위와 같이 선언한 이후에 배열을 액세스 하는 것은 아주 쉽습니다. 


### 2. 2차원 배열 포인터 선언


2차원 배열을 가리키는 포인터는 어떻게 선언해야 할까요? 


```c
void main(void)
{
  int arr[2][3] = { 100, 101, 102, 103, 104, 105 };

  int (*p)[3] = arr;

  printf("%d", p[1][2]);
}
```


[소스 코드](https://www.github.com/boyinblue/test/c/419212090/2dim_pointer1.c)


<code>int arr[2][3];</code>을 
<code>int (*p)[3];</code>과 같은 형식으로 변환해주면 됩니다. 


프로그래밍 언어를 배우는 많은 사람들이 
문법을 왜 그렇게 만들었는지 그 이유에 대해서 궁금해하곤 합니다. 


우리가 영어를 배우면서 영어 문법을 배울때, 문법을 왜 그렇게 만들었는지에 대해서 
묻고 따지지 않는 것처럼 프로그래밍 언어 역시도 문법을 그렇게 정해놨기 때문에 
"문법을 왜 이렇게 만들어 놨지?"라고 의문을 가지는 것은 큰 의미가 없습니다.


### 3. 2차원 배열 포인터를 함수 포인터로 넘기는 방법


하지만 위의 배열의 포인터를 함수 인자로 넘겨야 한다면 어떻게 해야 할까요? 


```c
void dump_data( int iRows, int iCols, int (*arr)[3] )
{
  int i = 0;
  int j = 0;

  for ( i = 0 ; i < iRows ; i++ )
  {
    for ( j = 0 ; j < iCols ; j++ )
    {
      printf("%d ", arr[i][j]);
    }
    printf("\n");
  }  
}

void main(void)
{
  int arr[2][3] = { 100, 101, 102, 103, 104, 105 };

  dump_data( 2, 3, arr);
}
```


[소스 코드](https://www.github.com/boyinblue/test/c/419212090/2dim_pointer2.c)


위와 같이 작성하고 빌드해서 실행하면 아래와 같은 결과가 나옵니다. 


```
100 101 102 
103 104 105
```


2차원 배열 포인터를 활용한 간단한 예제
---


```c
#include <stdio.h>
#define MAX_STU 100
#define MAX_COURSE 10
#define MAX_NAME_SIZE 10

void temp_score(int nstu, int ncrs, int s[MAX_STU][MAX_COURSE+2],int ss[MAX_STU]){
    for (int i = 0; i < nstu; i++) {
        for (int j = 0; j < (nstu - 1) - i; j++) {
            if (ss[j] < ss[j + 1]) {   

                int temp2 = ss[j];
                ss[j] = ss[j+1];
                ss[j + 1] = temp2;

                for (int k = 0; k < ncrs; k++) {
                    int temp = s[j][k];
                    s[j][k] = s[j + 1][k];
                    s[j + 1][k] = temp;
                }
            }
        }
    }
}

void input_scores(int nstu, int ncrs, char (*name)[MAX_NAME_SIZE], int s[MAX_STU][MAX_COURSE+2],int ss[MAX_STU]){
    for(int i=0;i<nstu;i++){
	    printf("학번 : ");
        scanf("%d", &s[i][0]);
        printf("이름 : ");
        scanf("%s", name[i]);
    }
    
    for(int n=0;n<ncrs;n++){
        for(int stu=0;stu<nstu;stu++){
            printf("점수 : ");
            scanf("%d",&s[stu][n+1]);
            ss[stu] += s[stu][n+1];
        }
    }
}

void printf_scores(int nums,int ncrs, char (*name)[MAX_NAME_SIZE], int s[MAX_STU][MAX_COURSE+2],int ss[MAX_STU]){
    int sum[MAX_STU]={0};
    printf("이름\t학번\t");
    for(int crs=1;crs<=ncrs;crs++){
        printf("과목%d\t",crs);
        if (crs == ncrs) {
            printf("총합");
        }
    }
    printf("\n");
    for(int stu=0;stu<nums;stu++){
        printf("%s\t", name[stu]);
    	for(int crs=0;crs<=ncrs;crs++){  
            printf("%d\t",s[stu][crs]);
    	}

    	printf("%d", ss[stu]);       
    	printf("\n");
    }
}

int main()
{
    int score[MAX_STU][MAX_COURSE+2];
    int numStu; //학생수
    int numCourse;//과목수 
    int score_sum[MAX_STU] = { 0 };
    char names[MAX_STU][MAX_NAME_SIZE];
    
    if(scanf("%d%d",&numStu,&numCourse) !=2){
        printf("입력오류\n");
        return 1;
    }

    //크기 check
    input_scores(numStu, numCourse, names, score, score_sum);
    temp_score(numStu,numCourse, score,score_sum);
    printf_scores(numStu,numCourse, names, score,score_sum);
}
```


[전체 소스 코드](https://raw.githubusercontent.com/boyinblue/test/main/c/419212090/score.c)


이상입니다. 






[✔️  C Language](index.html 'C 언어에 대한 내용을 기록')
---


C 언어에 대한 내용을 기록하는 페이지입니다.


[✏️ ](https://www.github.com/boyinblue/boyinblue.github.io/edit/main/012_c/001-2-dimension-array-pointer.md '수정하기')

