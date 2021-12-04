package com.app.jkorp;

import androidx.appcompat.app.AppCompatActivity;


import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.simple.parser.JSONParser;
import org.json.simple.JSONObject;
import org.json.simple.JSONArray;
import org.json.simple.parser.ParseException;


public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        // ---------- BLOQUE PARA CONSEGUIR JSON DE CURSOS
        final TextView textView = (TextView) findViewById(R.id.text);
        // ...

        // Instantiate the RequestQueue.
        RequestQueue queue = Volley.newRequestQueue(this);
        String url = "http://190.236.90.87:25565/api-roadmaps";

        // Request a string response from the provided URL.
        StringRequest stringRequest = new StringRequest(Request.Method.GET, url,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        // Display the first 500 characters of the response string.
                        textView.setText("Response is: "+ response);
                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Log.println(Log.ERROR,"errr",error.toString());
                textView.setText(error.toString());
            }
        });

        // Add the request to the RequestQueue.
        queue.add(stringRequest);

        //----------- ACA TERMINA

        // ------------- Bloque para agregar views con los cursos
        ScrollView objetivo = (ScrollView) findViewById(R.id.desplazar);

        JSONParser parser = new JSONParser();
        JSONObject object = null;
        int tamano = 0;
        try {
            object = (JSONObject) parser.parse(stringRequest.toString());
            tamano = (int) object.get("tamano");
        } catch (ParseException e) {
            Toast.makeText(getApplicationContext(), "No se pudo crear json", Toast.LENGTH_SHORT).show();
            e.printStackTrace();
        }

        if(tamano!=0){
            TextView[] cursos = new TextView[tamano];
            JSONArray jsonCursos = (JSONArray)object.get("curso");
            for (int i = 0; i<tamano; i++){
                JSONObject curso = (JSONObject) jsonCursos.get(i);
                String titulo = curso.get("titulo").toString();
                String descripcion = curso.get("descripcion").toString();
                cursos[i].setText(titulo + "\n" + descripcion);
                cursos[i].setLayoutParams(new LinearLayout.LayoutParams(
                        LinearLayout.LayoutParams.MATCH_PARENT,
                        LinearLayout.LayoutParams.WRAP_CONTENT));

                objetivo.addView(cursos[i]);
            }
        }


        //----------- ACA TERMINA
    }
}