#include <stdio.h>

int main()
{
  int arr[5] = {0,};
  int i = 0;
  int sum = 0;

  for ( ; i < 5 ; i++ )
  {
    scanf("%d", &arr[i]);
  }

  for ( i = 0 ; i < 5 ; i++ )
  {
    sum += arr[i];
  }

  printf("%d", sum);
}
