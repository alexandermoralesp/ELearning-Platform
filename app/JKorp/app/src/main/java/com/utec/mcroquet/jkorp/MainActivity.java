package com.utec.mcroquet.jkorp;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.LinearLayout;
import android.widget.ProgressBar;
import android.widget.TextView;
import android.widget.EditText;
import android.util.Log;
import android.widget.Toast;
import com.google.android.material.bottomnavigation.BottomNavigationView;
import androidx.appcompat.app.AppCompatActivity;
import androidx.navigation.NavController;
import androidx.navigation.Navigation;
import androidx.navigation.ui.AppBarConfiguration;
import androidx.navigation.ui.NavigationUI;
import com.utec.mcroquet.jkorp.databinding.ActivityMainBinding;
import java.util.ArrayList;
import java.util.List;
import java.util.Timer;
import java.util.TimerTask;
import java.util.Vector;

public class MainActivity extends AppCompatActivity implements View.OnClickListener{

    private ActivityMainBinding binding;

    ProgressBar progressBar;
    LinearLayout classLayout;
    int value;
    Button addClass;
    Vector<Course> classes = new Vector<>(0);


    @SuppressLint("WrongViewCast")
    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        binding = ActivityMainBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());


        BottomNavigationView navView = findViewById(R.id.nav_view);
        // Passing each menu ID as a set of Ids because each
        // menu should be considered as top level destinations.
        AppBarConfiguration appBarConfiguration = new AppBarConfiguration.Builder(
                R.id.navigation_home, R.id.navigation_dashboard, R.id.navigation_notifications)
                .build();
        NavController navController = Navigation.findNavController(this, R.id.nav_host_fragment_activity_main);
        NavigationUI.setupActionBarWithNavController(this, navController, appBarConfiguration);
        NavigationUI.setupWithNavController(binding.navView, navController);

        classLayout = findViewById(R.id.layout_cursos_id);
        addClass = findViewById(R.id.crear_curso_id);

        addClass.setOnClickListener(this);

        for(int i = 0; i < classes.size(); i++){
            View buttonView = getLayoutInflater().inflate(R.layout.new_class, null, false);
            View gap = getLayoutInflater().inflate(R.layout.new_class_layout, null, false);

            TextView changeClassName = buttonView.findViewById(R.id.title_class_id);
            TextView changeDescName = buttonView.findViewById(R.id.decription_class_id);


            changeClassName.setText(classes.get(i).getName());
            changeDescName.setText(classes.get(i).getDescription());

            classLayout.addView(buttonView);
            classLayout.addView(gap);
        }

    }


    class Course{
        private String name;
        private String description;

        public Course(String n, String d){
            name = n;
            description = d;
        }

        public String getName(){
            return name;
        }
        public String getDescription(){
            return description;
        }
        public void setName(String name){
            this.name = name;
        }
        public void setDescription(String description){
            this.description = description;
        }
    }

    public void onClick(View v){
        addView();
    }

    private void addView(){
        View buttonView = getLayoutInflater().inflate(R.layout.new_class, null, false);
        View gap = getLayoutInflater().inflate(R.layout.new_class_layout, null, false);
        EditText className = findViewById(R.id.name_of_course);
        EditText classDesc = findViewById(R.id.description_of_course_in);
        String cName = className.getText().toString();
        String cDesc = classDesc.getText().toString();

        Course nuevo = new Course(cName, cDesc);

        TextView changeClassName = buttonView.findViewById(R.id.title_class_id);
        TextView changeDescName = buttonView.findViewById(R.id.decription_class_id);

        changeClassName.setText(cName);
        changeDescName.setText(cDesc);

        nuevo.setName(cName);
        nuevo.setDescription(cDesc);

        classes.add(nuevo);

        classLayout.addView(buttonView);
        classLayout.addView(gap);

    }

    private void removeView(View v){

    }

}