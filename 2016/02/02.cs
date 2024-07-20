public class Day2
{
	static string[] input = File.ReadAllText("./02/input.txt").Trim().Split();
	// static string[] input = File.ReadAllText("./02/test-input.txt").Trim().Split();
	static int[][] keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
	static int[] coords = new int[] { 1, 1 };

	public static void Part1()
	{
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
}
