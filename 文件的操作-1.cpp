#define _CRT_SECURE_NO_WARNINGS 1
#include<stdio.h>
//int main()
//{
//	FILE* pf = fopen("data.txt", "w");
//	if (pf == NULL)
//	{
//		perror("fopen");
//		return 1;
//	}
//	fputc('a', pf);
//	fputc('b', pf);
//	fputc('c', pf);
//	fputc('d', pf);
//
//	fclose(pf);
//	pf = NULL;//为了防止变成野指针
//
//	return 0;
//}
//int main()
//{
//	FILE* pf = fopen("data1.txt", "w");
//	pf = NULL;
//	if (pf == NULL)
//	{
//		perror("fopen");
//		return 1;
//	}
//
//
//	fclose(pf);
//	pf = NULL;//为了防止变成野指针
//
//	return 0;
//}
//int main()
//{
//	FILE *pf= fopen("..\\datax.txt", "w");
//	if (pf == NULL)
//	{
//		perror("fopen");
//		return 1;
//	}
//	fputc('a', pf);
//	fputc('b', pf);
//	fputc('c', pf);
//	fputc('d', pf);
//	fclose(pf);
//	pf = NULL;
//}
//int main()
//{
//	FILE* pf = fopen("data.txt", "w");
//	if (pf == NULL)
//	{
//		perror("fopen");
//		return 1;
//	}
//	char ch = 0;
//	for (ch = 'a'; ch <= 'z'; ch++)
//	{
//		/*if (ch % 5 == 0)
//			fputc('\n',pf);*/
//		fputc(ch, pf);
//	}
//	fclose(pf);
//	pf == NULL;
//}

//int main()
//{
//	char ch = 0;
//	for (ch = 'a'; ch <= 'z'; ch++)
//	{
//		/*if (ch % 5 == 0)
//			fputc('\n', stdout);*/
//		fputc(ch, stdout);
//	}
//
//	return 0;
//}
//
//
//int main()
//{
//	FILE* pf = fopen("data.txt", "r");
//	if (pf == NULL)
//	{
//		perror("fopen");
//		return 1;
//	}
//	//读文件
//	int ch = 0;
//	while ((ch = fgetc(pf)) != EOF)
//	{
//		printf("%c ", ch);
//	}
//	int ch1 = fgetc(pf);
//	printf("%c ", ch1);
//
//	ch1= fgetc(pf);
//	printf("%c ", ch1);
//
//	ch1 = fgetc(pf);
//	printf("%c ", ch1);
//
//	ch1 = fgetc(pf);
//	printf("%c ", ch1);
//
//	fclose(pf);
//	pf = NULL;
//
//	return 0;
//}
//
//int main()
//{
//	FILE* pf = fopen("data.txt", "w");
//	if (pf == NULL)
//	{
//		perror("fopen");
//		return 1;
//	}
//	//写文件
//	//fputs("hello", pf);
//	char arr[] = "hello";
//	fputs(arr, pf);
//	fputs("world", pf);
//
//	fclose(pf);
//	pf = NULL;
//
//	return 0;
//}
int main()
{
	FILE* pf = fopen("data.txt", "r");
	if (pf == NULL)
	{
		perror("fopen");
		return 1;
	}
	//读文件
	char arr[100] = { 0 };
	fgets(arr, 10, pf);
	printf("%s", arr);
	printf("\n");
	fgets(arr, 10, pf);
	printf("%s", arr);
	printf("\n");
	fgets(arr, 100, pf);
	printf("%s", arr);
	fclose(pf);
	pf = NULL;

	return 0;
}
