/* Copyright 2019. Jeongwon Her. All rights reserved. */
using System;

namespace WebCrawler
{
    // Generate name with previous value
    class NameGen
    {
        int famNum = 0;
        int sexNum = 0;
        int namNum = 0;

        string[] family =
        {
            "김", "이", "박", "최", "정", "강", "조", "윤", "장", "임", "한", "오", "서", "신", "권", "황", "안", "송", "전", "홍"
        };

        string[] mNames =
        {
            "성민", "준호", "민석", "민수", "승현",
            "동현", "준혁", "민재", "준영", "현준", "승민",
            "민준", "서준", "주원", "예준", "시우", "준서", "도윤", "현우", "건우", "지훈"
        };

        string[] fNames =
        {
            "유진", "민지", "수빈", "지원", "지현", "지은", "현지", "은지", "예진", "예지",
            "서연", "민서", "서현", "서영", "수민", "예원",
            "서윤", "지우", "윤서", "채원", "하윤"//, "지아", "은서"
        };

        // Generate random name
        public string randomName()
        {
            Random random = new Random();

            if (random.Next() % 2 == 0)
                return family[random.Next() % family.Length] + mNames[random.Next() % mNames.Length];
            else
                return family[random.Next() % family.Length] + fNames[random.Next() % fNames.Length];
        }

        // Clear state
        public void clearState(int famNum=0, int sexNum=0, int namNum=0)
        {
            this.famNum = famNum;
            this.sexNum = sexNum;
            this.namNum = namNum;
        }

        // Generate name with previous state
        public string getName()
        {
            if (famNum < 0 || sexNum < 0 || namNum < 0)
                clearState();

            if (famNum >= family.Length || sexNum >= 2)
            {
                clearState();
                return null;
            }
            else if (sexNum == 0 && namNum >= mNames.Length)
            {
                sexNum = 1;
                namNum = 0;
            }
            else if (sexNum == 1 && namNum >= fNames.Length)
            {
                sexNum = 0;
                namNum = 0;
                famNum++;
            }

            if (sexNum == 0)
                return family[famNum] + mNames[namNum++];
            else
                return family[famNum] + fNames[namNum++];
        }
        
        // Property of states
        public int LengthFamily() { return family.Length; }
        public int LengthMName() { return mNames.Length; }
        public int LengthFName() { return fNames.Length; }

    }// End of class

}// End of namespace
