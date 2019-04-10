/* Copyright 2019. Jeongwon Her. All rights reserved. */
using System;
using System.IO;
using System.Collections.Generic;

namespace WebCrawler
{
    class WebCrawlerMain
    {
        // Release state . Weeknum Month Date
        public const string version = "0.030409";

        // Detect error
        public static bool error = false;

        // Command input will be updated

        public static void Main()
        {
            Console.WriteLine("/* Copyright 2019. Jeongwon Her. All rights reserved. */");
            Console.WriteLine("WebCrawler Version : " + version);

            // Arguments = (fam, sex, num, rep)
            int[] arguments = new int[4];
            for (int i = 0; i < 3; i++)
                arguments[i] = 0;
            // Infinite loop (search all names)
            arguments[3] = -1;
            
            // Create name generator
            NameGen nameGen = new NameGen();

            // Input
            while (true)
            {
                error = false;
                Console.Write("Just enter or set state(fam, sex, num, rep) : ");
                string input = Console.ReadLine();
                string[] inputs = input.Split(' ');
                if (input == "")
                    break;
                else
                {
                    if (inputs.Length < 4)
                    {
                        Console.WriteLine("Input Error in arguments");
                        continue;
                    }

                    if (!int.TryParse(inputs[0], out arguments[0]) || arguments[0] < 0 || arguments[0] >= nameGen.LengthFamily())
                    {
                        Console.WriteLine("Input Error in argument family");
                        error = true;
                    }
                    if (!int.TryParse(inputs[1], out arguments[1]) || arguments[1] < 0 || arguments[1] >= 2)
                    {
                        Console.WriteLine("Input Error in argument sex");
                        error = true;
                    }
                    if (!int.TryParse(inputs[2], out arguments[2]) || arguments[2] < 0 ||
                        (arguments[1] == 0 && arguments[2] > nameGen.LengthMName()) ||
                        (arguments[1] == 1 && arguments[2] > nameGen.LengthFName()))
                    {
                        Console.WriteLine("Input Error in argument name");
                        error = true;
                    }
                    if (!int.TryParse(inputs[3], out arguments[3]))
                    {
                        Console.WriteLine("Input Error in argument repeat");
                        error = true;
                    }

                    if (!error)
                    {
                        if (inputs.Length > 4)
                            Console.WriteLine("Ignored from the 5");
                        break;
                    }
                    
                }
            }// End of input

            // Create WebRequest
            WebRequest web = new WebRequest();

            // Initialize name generator
            nameGen.clearState(arguments[0], arguments[1], arguments[2]);
            string name = nameGen.getName();

            // For readability
            int cnt = arguments[3];

            // Check out file path and clear
            string path = @"out.txt";
            if (File.Exists(path))
            {
                Console.WriteLine("Delete existing file...");
                File.Delete(path);
            }

            // Create the file.
            StreamWriter output = new StreamWriter(path);

            // Crawling
            for (; name != null && cnt!=0; name = nameGen.getName(), cnt--)
            {
                // Search id by name
                Console.WriteLine("{0} 검색 결과", name);
                output.WriteLine("{0} 검색 결과", name);
                List<string> iDs = web.GetIDonFacebook(name);

                if (iDs != null)
                    foreach (string id in iDs)
                    {
                        // Search likes by id
                        Console.WriteLine("{0}의 Likes", id);
                        output.WriteLine("{0}의 Likes", id);
                        List<string> Likes = web.GetLikeonFacebook(id);

                        // Print console and file
                        if (Likes != null)
                        {
                            foreach (string like in Likes)
                            {
                                Console.WriteLine(like);
                                output.WriteLine(like);
                            }
                        }
                        else
                            error = true;
                        Console.WriteLine();
                        //break;
                    }
                else
                    error = true;
                //break;
            }// End of Crawl

            // Close the file
            output.Close();

            // End messege
            if (error)
                Console.Write("알 수 없는 에러 발생. ");
            else
                Console.Write("결과 저장됨. ");
            Console.Write("계속하려면 아무 키나 누르십시오...");

            Console.ReadLine();
        }// End of main

    }// End of class

}// End of namespace
