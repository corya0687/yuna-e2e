package app;

import java.sql.Connection;

public class Vuln {
    public void query(Connection c, String name) throws Exception {
        c.createStatement().executeQuery("SELECT * FROM users WHERE name = '" + name + "'");
    }
}
