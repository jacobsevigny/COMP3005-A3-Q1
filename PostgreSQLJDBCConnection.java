import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class PostgreSQLJDBCConnection {
 
    public static void main(String[] args) {
    
        // JDBC & Database credentials
        String url = "jdbc:postgresql://<HOST>:<PORT>/<DATABASE_NAME>";
        String user = "<USERNAME>";
        String password = "<PASSWORD>";

        try {

            Class.forName("org.postgresql.Driver");
            // Connect to the database
            Connection conn = DriverManager.getConnection(url, user, password);
            if (conn != null) {
                System.out.println("Connected to PostgreSQL successfully!");
            } else {
                System.out.println("Failed to establish connection.");
            } 
            conn.close();
            }
            catch (ClassNotFoundException | SQLException e) {
                e.printStackTrace();
            }
    }
}