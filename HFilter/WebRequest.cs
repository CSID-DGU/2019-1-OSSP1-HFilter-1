using Android.Net;
using Java.IO;
using Java.Net;
using System;
using System.Collections.Generic;
using System.IO;
using System.Net;
using System.Runtime.Remoting.Contexts;
using System.Threading.Tasks;

namespace TestApp
{
    class WebRequest
    {
        public static async Task<List<string>> GetLikeOnFacebook(string id)
        {
            HttpWebRequest request = (HttpWebRequest)HttpWebRequest.Create("https://www.facebook.com/"+id);

            // Set the credentials.  
            request.Credentials = CredentialCache.DefaultCredentials;
            //Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Safari/537.36
            request.UserAgent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Safari/537.36";
            //request.Method = "POST";
            //request.ContentType = "application/json";
            //request.Headers.Add("User-Agent: AnonymousClient");

            HttpWebResponse response = null;
            try
            {
                response = (HttpWebResponse)await request.GetResponseAsync();
            }
            catch
            {
                return null;
            }

            if (response == null || response.StatusCode != HttpStatusCode.OK) return null;
            Stream dataStream = response.GetResponseStream();
            StreamReader reader = new StreamReader(dataStream);

            string output = await reader.ReadToEndAsync();

            // Parsing.
            int ptr = output.IndexOf("기타");
            if (ptr == -1)
            {
                reader.Close();
                response.Close();
                return null;
            }
            ptr = output.IndexOf("<a", ptr);
            ptr = output.IndexOf("\">", ptr) + 2;

            // Return Value
            List<string> LikeList = new List<string>();

            // Parsing.
            for (;
                ptr < output.Length && ptr != -1;
                ptr = output.IndexOf("\">", ptr) + 2)
            {
                if (ptr == -1) break;
                if (ptr == output.IndexOf("<", ptr))
                    break;

                // "Like"</a>
                string like = output.Substring(ptr, output.IndexOf("<", ptr) - ptr);

                if (like == "더 보기" || like == ", " || like == "Facebook에 로그인")
                    continue;

                LikeList.Add(like);
            }

            reader.Close();
            response.Close();

            return LikeList;
        }
    }// end of class


}// end of namespace

//public static async Task<List<string>> GetLikeOnFacebook(string id)
//{
//    HttpWebRequest request = (HttpWebRequest)HttpWebRequest.Create("https://www.facebook.com/" + id);

//    // Set the credentials.  
//    request.Credentials = CredentialCache.DefaultCredentials;
//    //Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Safari/537.36
//    request.UserAgent = "Anonymous Client";
//    //request.Method = "POST";
//    //request.ContentType = "application/json";
//    request.MaximumResponseHeadersLength = 64;

//    HttpWebResponse response = null;
//    try
//    {
//        response = (HttpWebResponse)await request.GetResponseAsync();
//    }
//    catch
//    {
//        return null;
//    }

//    if (response == null || response.StatusCode != HttpStatusCode.OK) return null;
//    Stream dataStream = response.GetResponseStream();
//    StreamReader reader = new StreamReader(dataStream);

//    string output = await reader.ReadToEndAsync();

//    // Parsing.
//    int ptr = output.IndexOf("기타");
//    if (ptr == -1)
//    {
//        reader.Close();
//        response.Close();
//        return null;
//    }
//    ptr = output.IndexOf("<a", ptr);
//    ptr = output.IndexOf("\">", ptr) + 2;

//    // Return Value
//    List<string> LikeList = new List<string>();

//    // Parsing.
//    for (;
//        ptr < output.Length && ptr != -1;
//        ptr = output.IndexOf("\">", ptr) + 2)
//    {
//        if (ptr == -1) break;
//        if (ptr == output.IndexOf("<", ptr))
//            break;

//        // "Like"</a>
//        string like = output.Substring(ptr, output.IndexOf("<", ptr) - ptr);

//        if (like == "더 보기" || like == ", " || like == "Facebook에 로그인")
//            continue;

//        LikeList.Add(like);
//    }

//    reader.Close();
//    response.Close();

//    return LikeList;
//}