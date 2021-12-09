package com.utec.mcroquet.jkorp;

import android.util.JsonReader;
import android.util.Log;
import android.widget.TextView;

import androidx.annotation.NonNull;

import org.w3c.dom.Text;

import java.io.IOException;
import java.util.Objects;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class API {
    final OkHttpClient client = new OkHttpClient();

    // Funcion declarar
    void run(String url, TextView text) throws IOException {
        Request request = new Request.Builder()
                .url(url)
                .build();

        client.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(@NonNull Call call, @NonNull IOException e) {
                e.printStackTrace();
            }

            @Override
            public void onResponse(@NonNull Call call, @NonNull Response response) throws IOException {
                if (response.isSuccessful())
                {
                    Log.i("prueba", response.body().string());
                    final String myResponse = response.body().toString();

                }
            }
        });
    }
}
