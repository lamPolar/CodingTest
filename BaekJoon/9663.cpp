#include <iostream>
using namespace std;

int check_here(int row, int col, int *map)
{
	int other_row;
	int other_col;

	other_row = 0;
	while (map[other_row] != -1 && other_row < row)
	{
		other_col = map[other_row];
		if (other_col == col || other_row == row)
			return (0);
		if ((other_row - other_col) == (row - col))
			return (0);
		if ((other_row + other_col) == (row + col))
			return (0);
		other_row += 1;
	}
	return (1);
}

void put_queen(int row, int N, int *total, int *map)
{
	int col;

	if (row == N)
	{
		*total += 1;
		return ;
	}
	col = 0;
	while (row < N && col < N)
	{
		if (check_here(row, col, map))
		{
			map[row] = col;
			put_queen(row + 1, N, total, map);
			map[row] = -1;
		}
		col += 1;
	}
}

int main(void)
{
	int N;
	int total;
	int *map;
	int i;

	cin >> N;
	map = new int[N];
	i = 0;
	while (i < N)
	{
		map[i] = -1;
		i += 1;
	}
	total = 0;
	put_queen(0, N, &total, map);
	cout << total;
}
