/* Copyright 2019. Jeongwon Her. All rights reserved. */
using System;
using System.IO;
using System.Collections.Generic;

namespace WebCrawler
{
    class WebCrawlerMain
    {
        // Release state . Weeknum Month Date
        public const string version = "0.040420";

        // Detect error
        public static bool error = false;

        public static void Main(string[] args)
        {
            int status;

            if (args.Length != 0)
            {
                status=commandLine(args);
                endMsg(status, "commandLine");
                return;
            }

            Console.WriteLine("/* Copyright 2019. Jeongwon Her. All rights reserved. */");
            Console.WriteLine("WebCrawler Version : " + version);

            // Arguments = (fam, sex, num, rep)
            int[] arguments;

            // Input
            while (true)
            {
                error = false;
                Console.Write("Just enter or set state(fam, sex, num, rep) : ");
                string input = Console.ReadLine();

                arguments=ParamParse.InputParser(input);
                if (arguments != null) break;
            }// End of input

            status = normExcute(arguments);

            // End messege
            Console.Write("Press any key to continue...");
            Console.Read();
        }// End of main


        // When Commandline input
        static int commandLine(string[] args)
        {
            // Create name generator
            NameGen nameGen = new NameGen();
            // Create WebRequest
            WebRequest web = new WebRequest();

            string[] var = ParamParse.ArgParser(args);
            if (var == null) return 3;

            // Check out file path and clear
            if (File.Exists(var[1]))
            {
                Console.WriteLine("Delete existing file...");
                File.Delete(var[1]);
            }

            // Create the file
            StreamWriter writer=new StreamWriter(var[var.Length-1]);

            List<string> Likes = null;
            // Random name
            if (var[0] == "r")
            {
                string name = nameGen.randomName();
                Console.WriteLine("{0} 검색 결과", name);
                writer.WriteLine("{0} 검색 결과", name);
                List<string> iDs = web.GetIDonFacebook(name);
                if (iDs != null)
                {
                    int rand = new Random().Next() % iDs.Count;
                    Console.WriteLine("{0}의 Likes", iDs[rand]);
                    writer.WriteLine("{0}의 Likes", iDs[rand]);
                    Likes = web.GetLikeonFacebook(iDs[rand]);
                }
                else
                {
                    writer.Close();
                    return 1;
                }
            }
            // Specified name
            else if (var[0] == "s")
            {
                Console.WriteLine("{0}의 Likes", var[1]);
                writer.WriteLine("{0}의 Likes", var[1]);
                Likes = web.GetLikeonFacebook(var[1]);
            }

            // Print console and file
            if (Likes != null)
            {
                foreach (string like in Likes)
                {
                    Console.WriteLine(like);
                    writer.WriteLine(like);
                }
            }
            else
            {
                writer.Close();
                return 1;
            }

            writer.Close();
            return 0;
        }//End of commandLine



        // When normal excute
        public static int normExcute(int[] arguments)
        {
            // Create name generator
            NameGen nameGen = new NameGen();
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

            // Create the fileWriter
            StreamWriter writer = new StreamWriter(path);

            // Crawling
            for (; name != null && cnt != 0; name = nameGen.getName(), cnt--)
            {
                // Search id by name
                Console.WriteLine("{0} 검색 결과", name);
                writer.WriteLine("{0} 검색 결과", name);
                List<string> iDs = web.GetIDonFacebook(name);

                if (iDs != null)
                    foreach (string id in iDs)
                    {
                        // Search likes by id
                        Console.WriteLine("{0}의 Likes", id);
                        writer.WriteLine("{0}의 Likes", id);
                        List<string> Likes = web.GetLikeonFacebook(id);

                        // Print console and file
                        if (Likes != null)
                        {
                            foreach (string like in Likes)
                            {
                                Console.WriteLine(like);
                                writer.WriteLine(like);
                            }
                        }
                        Console.WriteLine();
                    }
                else
                {
                    // Close the file
                    writer.Close();
                    return 1;
                }

            }// End of Crawling

            // Close the file
            writer.Close();
            return 0;
        }


        public static void endMsg(int status, string func)
        {
            switch (status)
            {
                case -1:
                    Console.WriteLine("Error Code : {0}, NULL in {1}", status, func);
                    break;
                case 0:
                    break;
                case 1://network series
                    Console.WriteLine("Error Code : {0}, Network Error in {1}", status, func);
                    break;
                case 2://file series
                    Console.WriteLine("Error Code : {0}, File path in {1}", status, func);
                    break;
                case 3://input series
                    Console.WriteLine("Error Code : {0}, Wrong input in {1}", status, func);
                    break;
                default:
                    Console.WriteLine("Error Code : {0}, Unkown Error in {1}", status, func);
                    break;
            }
        }

    }// End of class

}// End of namespace
