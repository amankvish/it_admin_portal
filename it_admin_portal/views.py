from django.shortcuts import redirect

def home(request):
    # Redirect to the dashboard or render a homepage
    return redirect('it-admin:dashboard')  # Assuming you have a 'dashboard' route under 'it-admin/'
