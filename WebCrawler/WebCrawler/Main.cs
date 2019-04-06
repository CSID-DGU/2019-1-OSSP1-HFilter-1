/* Copyright 2019. Jeongwon Her. All rights reserved. */
using System;
using System.IO;
using System.Collections.Generic;

namespace WebCrawler
{
    class WebCrawlerMain
    {
        // release state . weeknum month date
        static string version = "0.20407";

        // Command input will be updated

        public static void Main()
        {
            Console.WriteLine("/* Copyright 2019. Jeongwon Her. All rights reserved. */");
            Console.WriteLine("WebCrawler Version : " + version);
            Console.Write("Just enter or set state(fam, sex, num, rep) : ");

            string input = Console.ReadLine();
            string[] inputs = input.Split(' ');

            int[] arguments = new int[4];
            for (int i = 0; i < 3; i++)
                arguments[i] = 0;
            arguments[3] = -1;

            if (input != "")
            {
                int i;
                for (i = 0; i < 4 && i<inputs.Length; i++)
                {
                    if (!int.TryParse(inputs[i], out arguments[i]))
                    {
                        Console.WriteLine("Input Error in argument {0}", i + 1);
                    }
                }

                if (inputs.Length > 4)
                    Console.WriteLine("Ignored from the 5");
            }

            WebRequest web = new WebRequest();
            NameGen nameGen = new NameGen();

            nameGen.clearState(arguments[0], arguments[1], arguments[2]);
            string name = nameGen.getName();
            int cnt = arguments[3];

            string path = @"out.txt";
            if (File.Exists(path))
            {
                File.Delete(path);
            }

            //Create the file.
            StreamWriter output = new StreamWriter(path);

            for (; name != null && cnt!=0; name = nameGen.getName(), cnt--)
            {

                Console.WriteLine("{0} 검색 결과", name);
                output.WriteLine("{0} 검색 결과", name);
                List<string> iDs = web.GetIDonFacebook(name);

                if (iDs != null)
                    foreach (string id in iDs)
                    {

                        Console.WriteLine("{0}의 Likes", id);
                        output.WriteLine("{0}의 Likes", id);
                        List<string> Likes = web.GetLikeonFacebook(id);
                        if (Likes != null)
                        {
                            foreach (string like in Likes)
                            {
                                Console.WriteLine(like);
                                output.WriteLine(like);
                            }
                        }
                        Console.WriteLine();

                        //break;
                    }
                
                //break;
            }

            output.Close();

        }//end of main


    }//end of class
}//end of namespace
