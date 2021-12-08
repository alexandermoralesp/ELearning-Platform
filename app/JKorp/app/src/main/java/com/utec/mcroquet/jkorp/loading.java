package com.utec.mcroquet.jkorp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.ProgressBar;

import com.utec.mcroquet.jkorp.databinding.ActivityMainBinding;

import java.util.Timer;
import java.util.TimerTask;

public class loading extends AppCompatActivity {

    private ActivityMainBinding binding;
    ProgressBar progressBar;
    int value;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_loading);

        progressBar = findViewById(R.id.progressBar);
        Thread thread = new Thread(new Runnable() {
            @Override
            public void run() {
                startProgress();
            }
        });
        thread.start();

    }
    public void startProgress()
    {
        for (value = 0; value < 100; value = value + 1)
        {
            try {
                Thread.sleep(51);
                progressBar.setProgress(value);
            }
            catch (InterruptedException e)
            {
                e.printStackTrace();
            }
        }
        Intent i = new Intent(loading.this, desktop.class);
        startActivity(i);
    }

}


