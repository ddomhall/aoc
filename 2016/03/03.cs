public class Day3
{
	static string[] triangles = File.ReadAllText("./03/input.txt").Trim().Split("\n");
	// static string[] triangles = File.ReadAllText("./03/test-input.txt").Trim().Split("\n");
	static int count;

	public static void Part1()
	{
		count = 0;
		foreach (string line in triangles)
		{
			if (ValidTriangle(SplitAndConvert(line))) count++;
		}
		Console.WriteLine(count);
	}

	public static void Part2()
	{
		count = 0;
		List<int> row0 = new List<int>();
		List<int> row1 = new List<int>();
		List<int> row2 = new List<int>();

		for (int row = 0; row < triangles.Count(); row++)
		{
			List<int> t = SplitAndConvert(triangles[row]);
			row0.Add(t[0]);
			row1.Add(t[1]);
			row2.Add(t[2]);
			if (row2.Count() == 3)
			{
				if (ValidTriangle(row0)) count++;
				if (ValidTriangle(row1)) count++;
				if (ValidTriangle(row2)) count++;
				row0.Clear();
				row1.Clear();
				row2.Clear();
			}
		}
		Console.WriteLine(count);
	}

	static List<int> SplitAndConvert(string input) => input.Trim().Split().Where(x => !string.IsNullOrEmpty(x)).Select(Int32.Parse).ToList();
	static bool ValidTriangle(List<int> input) => (input[0] + input[1] > input[2] && input[0] + input[2] > input[1] && input[1] + input[2] > input[0]);
}
