using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using Android.App;
using Android.Content;
using Android.OS;
using Android.Runtime;
using Android.Views;
using Android.Views.Animations;
using Android.Widget;

namespace HFilter
{

    [Activity(Label = "@string/app_name", Theme = "@style/MyTheme.NoTitle", NoHistory =true)]
    class SelectActivity:Activity
    {
        Button endBtn;
        ListView selectLV;
        Alert alert;
        SelectListView selectListView;
        System.Security.Cryptography.SHA256 sHA256;

        float[] big;
        string[] like;
        List<string> clicked;
        bool longclick;

        protected override void OnCreate(Bundle savedInstanceState)
        {
            base.OnCreate(savedInstanceState);

            // select layout
            SetContentView(Resource.Layout.activity_select);
        
            alert = new Alert(this);
            if (init() != 0)
            {
                alert.show("Error", "init failed");
            }
        }

        private int init()
        {
            Module.weights = new float[Module.weightLen];

            //View view = LayoutInflater.Inflate(Resource.Layout.activity_select, null);
            endBtn = FindViewById<Button>(Resource.Id.endBtn);
            endBtn.Click += endBtn_Click;
            endBtn.Enabled = false;

            selectLV = FindViewById<ListView>(Resource.Id.selectLV);
            
            selectListView = new SelectListView(this);
            selectLV.Adapter = selectListView;
            selectLV.ItemClick += SelectLV_ItemClick;
            selectLV.LongClick += SelectLV_LongClick;

            sHA256 = System.Security.Cryptography.SHA256.Create();

            big = new float[Module.weightLen];
            like = new string[Module.weightLen];
            clicked = new List<string>();
            
            return 0;
        }

        private void SelectLV_LongClick(object sender, View.LongClickEventArgs e)
        {
            longclick = true;
        }

        private void SelectLV_ItemClick(object sender, AdapterView.ItemClickEventArgs e)
        {
            var item = (Java.Util.ArrayList)selectLV.Adapter.GetItem(e.Position);

            // get item name
            string key = item.ToString();
            // return [text]
            key = key.Substring(1, key.Length - 2);
            clicked.Add(key);

            // hash
            byte[] keyB = Encoding.UTF8.GetBytes(key);
            string keyH = BitConverter.ToString(sHA256.ComputeHash(keyB)).Replace("-", string.Empty);
            float[] tmp;
            bool err = Module.module.TryGetValue(keyH, out tmp);
            if (!err) return;

            //add weight
            for (int i= 0; i<tmp.Length; i++)
            {
                Module.weights[i] += tmp[i];
            }

            //add big love
            for(int i=0; i<big.Length; i++)
            {
                if (big[i] < tmp[i])
                {
                    big[i] = tmp[i];
                    like[i] = key;
                }
            }

            //Animation anim = AnimationUtils.LoadAnimation(ApplicationContext, Resource.Animation.abc_fade_in);
            //e.View.Animation = anim;
            //selectLV.StartAnimation(anim);
            selectListView.Remove(e.Position);
            selectListView.AddNear(e.Position);

            endBtn.Enabled = true;
            //Toast debug = Toast.MakeText(this, key+tmp, ToastLength.Long);
            //debug.Show();

            if (longclick)
            {
                Toast.MakeText(this, "long", ToastLength.Short).Show();
                longclick = false;
            }
        }

        private void endBtn_Click(object sender, EventArgs e)
        {
            string result = string.Empty;
            //define gender
            float female = Module.weights[0];
            float male = Module.weights[1];
            if (female > 1 && male < 1)
            {
                result += "당신은 여성분이시군요? '";
                result += like[0] + "' 으로 알았어요\n";
            }
            else if(male>1 && female < 1)
            {
                result += "당신은 남성분이시군요? '";
                result += like[1] + "' 으로 알았어요\n";
            }
            else
            {
                result += "당신은 중성적인 매력을 지니고 있어요...\n";
            }

            //add biggest love
            float tmp = 0;
            int index = 0;
            for(int i=0; i<big.Length; i++)
            {
                if (tmp < big[i])
                {
                    tmp = big[i];
                    index = i;
                }
            }
            if (tmp < 1)
            {
                result += "이렇게 많은 것중에 좋아하는게 없다니... 실화?\n";
                result += "취미를 가져보는게 어떤가요?\n";
            }
            else
            {
                string flavor = Module.flavor[index].Substring(0, Module.flavor[index].IndexOf(' '));
                result += "당신은 '" + flavor + "'에 관심이 많군요.\n'";
                result += like[index] + "'를 좋아한다면 백방이죠\n";
                flavor = Module.flavor[index].Substring(Module.flavor[index].IndexOf(' ')+1);
                result += flavor+"\n";
                result += "당신과 비슷한 사람은 ";
                var except = Module.nears[index].Except(clicked).ToArray();
                for(int i=0; i<except.Length&&i<3; i++)
                {
                    result += "'" + except[i] + "' ";
                }
                result += "도 좋아했어요\n";
            }
            result += "제가 많이 맞췄나요?";

            //for (int i=0; i<Module.weightLen; i++)
            //{
            //    result += Module.weights[i].ToString() + "\n";
            //}

            string[] okButton = new string[1];
            okButton[0] = "ok";
            EventHandler<DialogClickEventArgs>[] end = new EventHandler<DialogClickEventArgs>[1];
            end[0]= delegate
            {
                Finish();
            };
            alert.show("당신은...", result, okButton, end);
            
        }
    }
}