using HFilter;
using HFilter.UWP;

using Xamarin.Forms;
using Xamarin.Forms.Platform.UWP;

[assembly: ExportRenderer(typeof(CustomView), typeof(CustomView_window))]

namespace HFilter.UWP
{
    public class CustomView_window : ViewRenderer<CustomView, Xamarin.Forms.Platform.UWP.EntryCellTextBox>
    {
        protected override void OnElementChanged(ElementChangedEventArgs<CustomView> e)
        {
            base.OnElementChanged(e);

            var box = new Xamarin.Forms.Platform.UWP.EntryCellTextBox();

            SetNativeControl(box);
        }
    }
}