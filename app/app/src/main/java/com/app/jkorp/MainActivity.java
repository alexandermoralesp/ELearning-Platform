package com.app.jkorp;

import androidx.appcompat.app.AppCompatActivity;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

import android.os.Bundle;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        /*String jdbcURL = "jdbc:postgresql://190.236.90.243:5432/jkorp";
        String user = "postgres";
        String password = "root";

        try {
            Class.forName("org.postgresql.Driver");
        } catch (ClassNotFoundException e) {
            Toast.makeText(getApplicationContext(),"Error getting driver", Toast.LENGTH_SHORT).show();
            e.printStackTrace();
        }

        try {
            Connection connection = DriverManager.getConnection(jdbcURL, user, password);
            Toast.makeText(getApplicationContext(),"Connected To DB", Toast.LENGTH_SHORT).show();

            connection.close();
        } catch (SQLException throwables) {
            Toast.makeText(getApplicationContext(),"Error Connecting To DB", Toast.LENGTH_SHORT).show();
            throwables.printStackTrace();
        }*/

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


    }
}