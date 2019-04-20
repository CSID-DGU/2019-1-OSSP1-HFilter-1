using System;
using System.IO;

namespace WebCrawler
{
    public static class ParamParse
    {
        public static int[] InputParser(string input)
        {
            // Arguments = (fam, sex, num, rep)
            int[] arguments = new int[4];
            for (int i = 0; i < 3; i++)
                arguments[i] = 0;
            // Infinite loop (search all names)
            arguments[3] = -1;

            bool error = false;

            string[] inputs = input.Split(' ');
            // Return Default if it has no inputs
            if (inputs[0] != "")
            {
                if (inputs.Length >= 4)
                {
                    if (!int.TryParse(inputs[0], out arguments[0]) || arguments[0] < 0)
                    {
                        Console.WriteLine("Input Error in argument family");
                        error = true;
                    }
                    if (!int.TryParse(inputs[1], out arguments[1]) || arguments[1] < 0 || arguments[1] >= 2)
                    {
                        Console.WriteLine("Input Error in argument sex");
                        error = true;
                    }
                    if (!int.TryParse(inputs[2], out arguments[2]) || arguments[2] < 0)
                    {
                        Console.WriteLine("Input Error in argument name");
                        error = true;
                    }
                    if (!int.TryParse(inputs[3], out arguments[3]))
                    {
                        Console.WriteLine("Input Error in argument repeat");
                        error = true;
                    }
                }
                else
                {
                    Console.WriteLine("Input Error in arguments");
                    error = true;
                }
            }
                
            if (!error)
            {
                if (inputs.Length > 4)
                    Console.WriteLine("Ignored from the 5");
                return arguments;
            }
            else
                return null;
        }

        // When initial input
        public static string[] ArgParser(string[] args)
        {
            
            bool error = false;

            string[] ret=null; 

            int pathLoc = 1;

            if (args.Length != 0)
            {
                switch (args[0])
                {
                    // Get random name
                    case "-R":
                    case "-r":
                        ret = new string[2];
                        ret[0] = "r";
                        break;

                    // Get specified name
                    case "-S":
                    case "-s":
                        ret = new string[3];
                        ret[0] = "s";
                        pathLoc = 2;

                        // Check valid ID
                        ret[1] = args[1];
                        long check;
                        if (!long.TryParse(ret[1], out check))
                        {
                            Console.WriteLine("Invalid ID");
                            error = true;
                        }
                        break;

                    // Normal mode
                    case "-N":
                    case "-n":
                        // will be update
                        ret = new string[4];
                        error = true;
                        break;

                    default:
                        error = true;
                        break;
                }

                // Out file path
                // Not specified path
                if (args.Length <= pathLoc)
                    ret[pathLoc] = System.IO.Directory.GetCurrentDirectory() + @"\out.txt";
                // Specified path
                else
                    ret[pathLoc] = args[pathLoc];
            }
            else
                error = true;

            if (error)
            {
                Console.WriteLine("Please enter right command.");
                Console.WriteLine("Usage:   -r <path>");
                Console.WriteLine("         -s <ID> <path>");
                return null;
            }

            return ret;
        }
    }
}
