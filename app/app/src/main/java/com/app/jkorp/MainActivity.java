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
import org.w3c.dom.Text;


public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        // ---------- BLOQUE PARA CONSEGUIR JSON DE CURSOS
        // ...

        // Instantiate the RequestQueue.
        RequestQueue queue = Volley.newRequestQueue(this);
        String url = "http://190.236.90.87:25565/api-roadmaps";

        // Request a string response from the provided URL.
        StringRequest stringRequest = new StringRequest(Request.Method.GET, url,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        // ------------- Bloque para agregar views con los cursos
                        ScrollView objetivo = (ScrollView) findViewById(R.id.desplazar);

                        JSONParser parser = new JSONParser();
                        JSONObject object = null;
                        int tamano = 0;
                        try {
                            object = (JSONObject) parser.parse(response);
                            tamano = Integer.parseInt(object.get("tamano").toString());
                        } catch (ParseException e) {
                            Toast.makeText(getApplicationContext(), "No se pudo crear json", Toast.LENGTH_SHORT).show();
                            e.printStackTrace();
                        }

                        if(tamano!=0){

                            TextView[] cursos = new TextView[tamano];
                            JSONArray jsonCursos = (JSONArray)object.get("curso");
                            for (int i = 0; i<tamano; i++){
                                cursos[i] = new TextView(getApplicationContext());
                                JSONObject curso = (JSONObject) jsonCursos.get(i);
                                String titulo = curso.get("titulo").toString();
                                String descripcion = curso.get("descripcion").toString();
                                System.out.println(titulo + descripcion);
                                //Toast.makeText(getApplicationContext(), titulo+descripcion, Toast.LENGTH_SHORT).show();
                                //cursos[i].setText(titulo + descripcion);
                                String union = titulo + descripcion;
                                cursos[i].setText(union);

                                objetivo.addView(cursos[i]);

                            }
                        }


                        //----------- ACA TERMINA
                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Toast.makeText(getApplicationContext(), "Error en la obtención de datos", Toast.LENGTH_SHORT).show();
                //textView.setText(error.toString());
            }
        });

        // Add the request to the RequestQueue.
        queue.add(stringRequest);

        //----------- ACA TERMINA


    }
}