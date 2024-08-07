public class Day2
{
	static string[] input = File.ReadAllText("./02/input.txt").Trim().Split();
	// static string[] input = File.ReadAllText("./02/test-input.txt").Trim().Split();

	public static void Part1()
	{
		int[][] keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
		int[] coords = new int[] { 1, 1 };
		Console.Write("2.1: ");
		foreach (string line in input)
		{
			foreach (char direction in line.ToCharArray())
			{
				switch (direction)
				{
					case 'U':
						if (coords[0] > 0) coords[0]--;
						break;
					case 'D':
						if (coords[0] < 2) coords[0]++;
						break;
					case 'L':
						if (coords[1] > 0) coords[1]--;
						break;
					case 'R':
						if (coords[1] < 2) coords[1]++;
						break;
				}
			}
			Console.Write(keypad[coords[0]][coords[1]]);
		}
		Console.WriteLine();
	}

	public static void Part2()
	{
		int?[][] keypad = [[null, null, 1, null, null], [null, 2, 3, 4, null], [5, 6, 7, 8, 9], [null, 'A', 'B', 'C', null], [null, null, 'D', null, null]];
		int[] coords = new int[] { 2, 0 };
		Console.Write("2.2: ");
		foreach (string line in input)
		{
			foreach (char direction in line.ToCharArray())
			{
				switch (direction)
				{
					case 'U':
						if (coords[0] > 0 && keypad[coords[0] - 1][coords[1]] != null) coords[0]--;
						break;
					case 'D':
						if (coords[0] < 4 && keypad[coords[0] + 1][coords[1]] != null) coords[0]++;
						break;
					case 'L':
						if (coords[1] > 0 && keypad[coords[0]][coords[1] - 1] != null) coords[1]--;
						break;
					case 'R':
						if (coords[1] < 4 && keypad[coords[0]][coords[1] + 1] != null) coords[1]++;
						break;
				}
			}
			int? key = keypad[coords[0]][coords[1]];
			if (key > 9) Console.Write(Convert.ToChar(key));
			else Console.Write(key);
		}
		Console.WriteLine();
	}
}
