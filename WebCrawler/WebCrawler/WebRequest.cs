/* Copyright 2019. Jeongwon Her. All rights reserved. */
using System;
using System.Collections.Generic;
using System.IO;
using System.Net;

namespace WebCrawler
{
    class WebRequest
    {
        //GetID by name
        public List<string> GetIDonFacebook(string name)
        {
            // Create a request for the URL.
            System.Net.WebRequest request = System.Net.WebRequest.Create("http://www.facebook.com/public/" + name);

            // Set the credentials.  
            request.Credentials = CredentialCache.DefaultCredentials;
            ((HttpWebRequest)request).UserAgent = "Anonymous Client";

            WebResponse response;
            try
            {
                // Get the response.
                response = request.GetResponse();
                // (1048ms)
            }
            catch(Exception e)
            {
                // Handling an Error.
                Console.WriteLine("Request Error : " + e.ToString());
                //response.Close();
                return null;
            }
            
            // Get the stream containing content returned by the server.  
            Stream dataStream = response.GetResponseStream();
            // Open the stream using a StreamReader for easy access.  
            StreamReader reader = new StreamReader(dataStream);
            // Read the content.  
            string responseFromServer = reader.ReadToEnd();
            // (65ms)

            // Parsing.
            int ptr = responseFromServer.IndexOf("<body");
            ptr = responseFromServer.IndexOf(name, ptr) + name.Length;
            ptr = responseFromServer.IndexOf(name, ptr);

            // Return Value.
            List<string> IDList = new List<string>();
            string ID;
            // To check it is valid id.
            long tmp;

            // Parsing.
            for (;
                ptr < responseFromServer.Length && ptr != -1;
                ptr = responseFromServer.IndexOf(name, ptr))
            {
                if (ptr == -1) break;

                // 100033756312152"><span>"name"
                //                        ^ptr
                ptr -= 15 + 8;

                // ID is fifteen digit
                ID = responseFromServer.Substring(ptr, 15);

                // Is number?
                if (long.TryParse(ID, out tmp))
                {
                    IDList.Add(ID);
                }

                // Move ptr.
                ptr += 15 + 8 + name.Length;
            }
            // (4ms)

            // Clean up the streams and the response.  
            reader.Close();
            response.Close();

            return IDList;
        }

        //GetLike by id
        public List<string> GetLikeonFacebook(string id)
        {
            // Create a request for the URL.
            System.Net.WebRequest request = System.Net.WebRequest.Create("http://www.facebook.com/" + id);

            // Set the credentials.  
            request.Credentials = CredentialCache.DefaultCredentials;
            ((HttpWebRequest)request).UserAgent = "Anonymous Client";

            WebResponse response;
            try
            {
                // Get the response.
                response = request.GetResponse();
                // (???ms)
            }
            catch (Exception e)
            {
                // Handling an Error.
                Console.WriteLine("Request Error : " + e.ToString());
                //response.Close();
                return null;
            }

            // Get the stream containing content returned by the server.  
            Stream dataStream = response.GetResponseStream();
            // Open the stream using a StreamReader for easy access.  
            StreamReader reader = new StreamReader(dataStream);
            // Read the content.  
            string responseFromServer = reader.ReadToEnd();
            // (???ms)

            // Parsing.
            int ptr = responseFromServer.IndexOf("기타");
            if (ptr == -1)
            {
                reader.Close();
                response.Close();
                return null;
            }
            ptr = responseFromServer.IndexOf("<a", ptr);
            ptr = responseFromServer.IndexOf("\">", ptr) + 2;

            // Return Value.
            List<string> LikeList = new List<string>();

            // Parsing.
            for (;
                ptr < responseFromServer.Length && ptr != -1;
                ptr = responseFromServer.IndexOf("\">", ptr) + 2)
            {
                if (ptr == -1) break;
                if (ptr == responseFromServer.IndexOf("<", ptr))
                    break;

                // "Like"</a>
                string like = responseFromServer.Substring(ptr, responseFromServer.IndexOf("<", ptr) - ptr);

                if (like == "더 보기" || like == ", " || like == "Facebook에 로그인")
                    continue;

                LikeList.Add(like);
            }
            // (???ms)

            // Clean up the streams and the response.  
            reader.Close();
            response.Close();

            return LikeList;
        }

        /* Incomplete method of ip bypass
         * 
         * HTTP request headers
         * IP address  x
         * Long URLs   x
         * Cookies     ?
         * Login information (authentication)
         */
        public List<string> captcha(string id)
        {
            System.Net.WebRequest request = System.Net.WebRequest.Create("http://www.facebook.com/" + id);

            //자격 증명
            CredentialCache cache = new CredentialCache();
            cache.Add(new Uri("http://example.com"), "NTLM", new NetworkCredential("UserName", "Password", "Domain"));
            request.Credentials = cache; //CredentialCache.DefaultCredentials;
            ((HttpWebRequest)request).UserAgent = "client";

            //프록시 설정
            WebProxy proxy = new WebProxy("http://www.proxysite.com:80/");
            //proxy.BypassProxyOnLocal = false;
            proxy.Credentials = System.Net.CredentialCache.DefaultCredentials;
            //request.Proxy = proxy;
            /////////////////////////////////////////////////////////////////////Error!

            // Policy.
            System.Net.Cache.HttpRequestCachePolicy policy =
                new System.Net.Cache.HttpRequestCachePolicy(System.Net.Cache.HttpCacheAgeControl.MaxAge, TimeSpan.MinValue);
            request.CachePolicy = policy;

            //request header
            //request.Headers.Add("");

            // Get the response.
            WebResponse response = request.GetResponse();
            // (???ms)

            // Handling an Error.
            if (((HttpWebResponse)response).StatusCode != HttpStatusCode.OK)
            {
                Console.WriteLine("Request Error : {0}", ((HttpWebResponse)response).StatusCode);
                response.Close();
                return null;
            }
            // Get the stream containing content returned by the server.  
            Stream dataStream = response.GetResponseStream();
            // Open the stream using a StreamReader for easy access.  
            StreamReader reader = new StreamReader(dataStream);
            // Read the content.  
            string responseFromServer = reader.ReadToEnd();
            // (???ms)

            return null;
        }

    }// End of class

}// End of namespace
