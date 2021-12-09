package com.utec.mcroquet.jkorp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.graphics.drawable.AnimationDrawable;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.TextView;

import com.utec.mcroquet.jkorp.ui.dashboard.DashboardFragment;
import com.utec.mcroquet.jkorp.ui.login.LoginActivity;

public class desktop extends AppCompatActivity {

    private LinearLayout rootLayout;
    private AnimationDrawable animDrawable;
    Button roadmaps;


    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_desktop);

        rootLayout = findViewById(R.id.root);
        animDrawable = (AnimationDrawable) rootLayout.getBackground();

        animDrawable.setEnterFadeDuration(10);
        animDrawable.setExitFadeDuration(5000);
        animDrawable.start();

    }

    public void goToDescription(View view) {
        Intent i = new Intent(this, LoginActivity.class);
        startActivity(i);
    }





}