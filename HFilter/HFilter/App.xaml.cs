using System;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

[assembly: XamlCompilation(XamlCompilationOptions.Compile)]
namespace HFilter
{
    public partial class App : Application
    {
        public App()
        {
            InitializeComponent();

            switch (Device.Idiom)
            {
                case TargetIdiom.Desktop:
                    MainPage = new MainPage_Desktop();
                    break;
                case TargetIdiom.Phone:
                default:
                    MainPage = new MainPage();
                    break;
            }
        }

        protected override void OnStart()
        {
            // Handle when your app starts
        }

        protected override void OnSleep()
        {
            // Handle when your app sleeps
        }

        protected override void OnResume()
        {
            // Handle when your app resumes
        }
    }
}
