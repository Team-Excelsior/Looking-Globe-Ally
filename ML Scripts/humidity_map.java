import sun.net.www.http.HttpClient;
import sun.rmi.transport.proxy.HttpReceiveSocket;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

public class humidity_map {

    URL url;
    public humidity_map() {
        try {
            url = new URL("https://weather.cit.api.here.com/weather/1.0/report.json?product=observation&latitude=52.516&longitude=13.389&oneobservation=true&app_id=Yzd1hH5IOppt9cttpCvL&app_code=wiDCHLDcJlt3aUAD8pAJkQ");
            HttpURLConnection conn = (HttpURLConnection)url.openConnection();
            conn.setRequestMethod("GET");

            BufferedReader reader = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            StringBuilder sb = new StringBuilder();
            char[] buff = new char[1024];
            while(reader.read(buff)>0){
                sb.append(new String(buff));
            }
            System.out.println(sb.toString());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /*public static void main(String[] args){
        new humidity_map();
    }*/

}
