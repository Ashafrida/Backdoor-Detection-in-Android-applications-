public class DBHelper extends SQLiteOpenHelper {

    private static final String DATABASE_NAME = "activities.db";
    private static final int DATABASE_VERSION = 1;

    public DBHelper(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        // Create the activities table
        String sql = "CREATE TABLE activities (" +
                "id INTEGER PRIMARY KEY AUTOINCREMENT," +
                "name TEXT," +
                "timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)";
        db.execSQL(sql);
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        // Upgrade the database if necessary
    }
}
// Insert a new activity
ContentValues values = new ContentValues();
values.put("name", "Activity Name");
long id = db.insert("activities", null, values);

// Query the activities table
String[] projection = {"id", "name", "timestamp"};
Cursor cursor = db.query("activities", projection, null, null, null, null, null);

// Update an activity
values.put("name", "New Activity Name");
String selection = "id = ?";
String[] selectionArgs = {String.valueOf(id)};
int count = db.update("activities", values, selection, selectionArgs);

// Delete an activity
String selection = "id = ?";
String[] selectionArgs = {String.valueOf(id)};
int count = db.delete("activities", selection, selectionArgs);
