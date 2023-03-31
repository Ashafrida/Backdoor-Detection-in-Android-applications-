public class ReportGeneratorReceiver extends BroadcastReceiver {

    @Override
    public void onReceive(Context context, Intent intent) {
        // Retrieve user data from SharedPreferences
        SharedPreferences sharedPreferences = context.getSharedPreferences("registration_data", Context.MODE_PRIVATE);
        String name = sharedPreferences.getString("name", "");
        String email = sharedPreferences.getString("email", "");
        int hour = sharedPreferences.getInt("hour", 0);
        int minute = sharedPreferences.getInt("minute", 0);

        // Generate report
        // ...

        // Send report to user's email address
        // ...
    }
