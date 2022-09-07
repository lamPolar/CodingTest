#include <iostream>
using namespace std;

int check_pairs(int i, int num, int *print)
{
	int j;

	j = 0;
	while (j < i && print[j] != -1)
	{
		if (print[j] > num)
			return (0);
		j += 1;
	}
	return (1);
}


void make_pairs(int i, int N, int M, int *print)
{
	int num;
	int j;

	if (i == M)
	{
		j = 0;
		while (j < M)
		{
			if (j != M - 1)
				cout << print[j] << ' ';
			else
				cout << print[j] << "\n";
			j += 1;
		}
		return ;
	}
	num = 1;
	while (i < M && num <= N)
	{
		if (check_pairs(i, num, print))
		{
			print[i] = num;
			make_pairs(i + 1, N, M, print);
			print[i] = -1;
		}
		num += 1;
	}
}


int main(void)
{
	int N;
	int M;
	int *print;
	int i;

	cin >> N >> M;
	print = new int[M];
	i = 0;
	while (i < N)
	{
		print[i] = -1;
		i += 1;
	}
	make_pairs(0, N, M, print);
}