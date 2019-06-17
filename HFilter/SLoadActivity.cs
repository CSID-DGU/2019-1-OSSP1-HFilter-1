using Android.App;
using Android.Content;
using Android.OS;
using Android.Support.V7.App;
using Android.Widget;
using System.Threading.Tasks;

namespace HFilter
{
    [Activity(Label = "@string/app_name", Theme = "@style/MyTheme.SLoad", NoHistory =true)]
    public class SLoadActivity : AppCompatActivity
    {
        //static readonly string TAG = "X:" + typeof(SplashActivity).Name;

        public override void OnCreate(Bundle savedInstanceState, PersistableBundle persistentState)
        {
            base.OnCreate(savedInstanceState, persistentState);
            //Log.Debug(TAG, "SplashActivity.OnCreate");
        }

        // Launches the startup task
        protected override void OnResume()
        {
            base.OnResume();
            Task startupWork = new Task(() => { SimulateStartup(); });
            startupWork.Start();
        }

        // Simulates background work that happens behind the splash screen
        async void SimulateStartup()
        {
            //await Task.Delay(200);
            Module.Init(Assets);

            Task<int> read = Module.ReadModule();
            int result = await read;

            Task<int> list = Module.ReadTotal();
            result += await read;

            Task<int> near = Module.ReadNear();
            result += await near;

            Task<int> flavor = Module.ReadFlavor();
            result += await flavor;

            if (result!=0)
            {
                Android.App.AlertDialog.Builder alert = new Android.App.AlertDialog.Builder(this);
                alert.SetTitle("Error");
                alert.SetMessage("Error to initialize");
                alert.SetPositiveButton("Ok", (senderAlert, args) =>
                {
                    FinishAffinity();
                });
                Dialog dialog = alert.Create();
                dialog.Show();
            }

            StartActivity(new Intent(Application.Context, typeof(MainActivity)));
            Finish();
        }
    }
}