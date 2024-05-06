#include <stdio.h>

int main(){
    int fru, len, temp;
    int arr[10000];
    scanf("%d %d", &fru ,&len);

    for(int i = 0; i < fru; i++)
    {
        scanf("%d", &arr[i]);
    }

    for (int i = 0; i < fru; i++)
    {
        for (int j = 0; j < fru-1; j++)
        {
            if (arr[j] > arr[j+1]) {
                temp = arr [j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }

    for (int i = 0; i < fru; i++)
    {
        if (len >= arr[i]){
            len++;
        }
        else {
            break;
        }
    }
    printf("%d", len);
    return 0;
}
